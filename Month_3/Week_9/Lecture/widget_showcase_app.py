
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from datetime import datetime, timedelta

# Configure page
st.set_page_config(
    page_title="Streamlit Widget Showcase",
    page_icon="🎛️",
    layout="wide"
)

st.title("🎛️ Streamlit Widget Showcase")
st.markdown("**Interactive elements for business applications**")

# Create sample business data
@st.cache_data
def generate_business_data():
    """
    Generate realistic e-commerce data for widget demonstrations
    """
    np.random.seed(42)
    
    # Date range for last 2 years
    start_date = datetime.now() - timedelta(days=730)
    dates = pd.date_range(start_date, periods=730, freq='D')
    
    data = {
        'date': np.repeat(dates, 3),  # 3 records per day
        'customer_id': [f"CUST_{i:06d}" for i in range(1, len(dates)*3 + 1)],
        'product_category': np.random.choice([
            'Electronics', 'Fashion', 'Home & Garden', 'Books', 'Sports', 
            'Beauty', 'Automotive', 'Toys', 'Health', 'Food'
        ], len(dates)*3),
        'state': np.random.choice([
            'São Paulo', 'Rio de Janeiro', 'Minas Gerais', 'Bahia', 
            'Paraná', 'Rio Grande do Sul', 'Pernambuco', 'Ceará'
        ], len(dates)*3),
        'order_value': np.random.exponential(100, len(dates)*3),
        'customer_satisfaction': np.random.choice([1, 2, 3, 4, 5], len(dates)*3, 
                                                p=[0.05, 0.1, 0.2, 0.35, 0.3]),
        'shipping_method': np.random.choice([
            'Standard', 'Express', 'Premium', 'Economy'
        ], len(dates)*3, p=[0.4, 0.3, 0.2, 0.1]),
        'payment_method': np.random.choice([
            'Credit Card', 'Debit Card', 'Bank Transfer', 'Digital Wallet'
        ], len(dates)*3, p=[0.45, 0.25, 0.2, 0.1])
    }
    
    return pd.DataFrame(data)

# Load data
df = generate_business_data()

# Sidebar for widgets
st.sidebar.header("🎛️ Widget Controls")
st.sidebar.markdown("Explore different widget types and their applications:")

# Section 1: Selection Widgets
st.sidebar.subheader("📝 Selection Widgets")

# 1. Selectbox - Single selection
selected_category = st.sidebar.selectbox(
    "Product Category:",
    options=['All'] + sorted(df['product_category'].unique()),
    help="Choose a product category to filter data"
)

# 2. Multiselect - Multiple selections
selected_states = st.sidebar.multiselect(
    "Brazilian States:",
    options=sorted(df['state'].unique()),
    default=sorted(df['state'].unique())[:3],
    help="Select one or more states for analysis"
)

# 3. Radio - Single choice from visible options
satisfaction_filter = st.sidebar.radio(
    "Customer Satisfaction Filter:",
    options=['All', 'High (4-5)', 'Medium (3)', 'Low (1-2)'],
    help="Filter customers by satisfaction level"
)

# Section 2: Input Widgets
st.sidebar.subheader("📊 Input Widgets")

# 4. Slider - Numeric range
order_value_range = st.sidebar.slider(
    "Order Value Range (R$):",
    min_value=float(df['order_value'].min()),
    max_value=float(df['order_value'].max()),
    value=(50.0, 500.0),
    step=25.0,
    help="Filter orders by value range"
)

# 5. Date input - Date selection
start_date = st.sidebar.date_input(
    "Analysis Start Date:",
    value=df['date'].min().date(),
    min_value=df['date'].min().date(),
    max_value=df['date'].max().date(),
    help="Choose the start date for analysis"
)

end_date = st.sidebar.date_input(
    "Analysis End Date:",
    value=df['date'].max().date(),
    min_value=df['date'].min().date(),
    max_value=df['date'].max().date(),
    help="Choose the end date for analysis"
)

# 6. Number input - Specific numeric input
min_orders = st.sidebar.number_input(
    "Minimum Orders to Display:",
    min_value=1,
    max_value=100,
    value=10,
    step=5,
    help="Set minimum number of orders for category analysis"
)

# Section 3: Interactive Widgets
st.sidebar.subheader("🔄 Interactive Widgets")

# 7. Checkbox - Boolean toggle
show_trends = st.sidebar.checkbox(
    "Show Trend Analysis",
    value=True,
    help="Toggle trend analysis charts"
)

include_weekends = st.sidebar.checkbox(
    "Include Weekend Data",
    value=True,
    help="Include Saturday and Sunday in analysis"
)

# 8. Button - Action trigger
refresh_data = st.sidebar.button(
    "🔄 Refresh Analysis",
    help="Refresh data and regenerate charts"
)

# Main content area
st.markdown("---")

# Apply filters to data
filtered_df = df.copy()

# Apply category filter
if selected_category != 'All':
    filtered_df = filtered_df[filtered_df['product_category'] == selected_category]

# Apply state filter
if selected_states:
    filtered_df = filtered_df[filtered_df['state'].isin(selected_states)]

# Apply satisfaction filter
if satisfaction_filter == 'High (4-5)':
    filtered_df = filtered_df[filtered_df['customer_satisfaction'].isin([4, 5])]
elif satisfaction_filter == 'Medium (3)':
    filtered_df = filtered_df[filtered_df['customer_satisfaction'] == 3]
elif satisfaction_filter == 'Low (1-2)':
    filtered_df = filtered_df[filtered_df['customer_satisfaction'].isin([1, 2])]

# Apply order value filter
filtered_df = filtered_df[
    (filtered_df['order_value'] >= order_value_range[0]) & 
    (filtered_df['order_value'] <= order_value_range[1])
]

# Apply date filter
filtered_df = filtered_df[
    (filtered_df['date'].dt.date >= start_date) & 
    (filtered_df['date'].dt.date <= end_date)
]

# Apply weekend filter
if not include_weekends:
    filtered_df = filtered_df[filtered_df['date'].dt.weekday < 5]

# Display filter results
st.subheader("📈 Filtered Data Analysis")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Total Orders", f"{len(filtered_df):,}")

with col2:
    avg_value = filtered_df['order_value'].mean()
    st.metric("Average Order Value", f"R$ {avg_value:.2f}")

with col3:
    avg_satisfaction = filtered_df['customer_satisfaction'].mean()
    st.metric("Average Satisfaction", f"{avg_satisfaction:.2f}/5.0")

with col4:
    total_revenue = filtered_df['order_value'].sum()
    st.metric("Total Revenue", f"R$ {total_revenue:,.2f}")

# Charts section
if show_trends and len(filtered_df) > 0:
    st.markdown("---")
    st.subheader("📊 Visual Analysis")
    
    chart_col1, chart_col2 = st.columns(2)
    
    with chart_col1:
        # Category distribution
        category_data = filtered_df['product_category'].value_counts()
        fig = px.pie(
            values=category_data.values,
            names=category_data.index,
            title="Orders by Product Category"
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with chart_col2:
        # State distribution
        state_data = filtered_df['state'].value_counts()
        fig = px.bar(
            x=state_data.index,
            y=state_data.values,
            title="Orders by State",
            labels={'x': 'State', 'y': 'Number of Orders'}
        )
        fig.update_xaxes(tickangle=45)
        st.plotly_chart(fig, use_container_width=True)

# Data preview
st.markdown("---")
st.subheader("📋 Filtered Data Preview")
st.markdown(f"Showing first 10 records from {len(filtered_df):,} total filtered records")

if len(filtered_df) > 0:
    st.dataframe(
        filtered_df.head(10)[[
            'date', 'customer_id', 'product_category', 'state',
            'order_value', 'customer_satisfaction'
        ]],
        use_container_width=True
    )
else:
    st.warning("⚠️ No data matches your current filter criteria. Try adjusting the filters.")

# Widget status display
st.markdown("---")
st.subheader("🔍 Current Filter Status")

status_col1, status_col2 = st.columns(2)

with status_col1:
    st.markdown("**Active Filters:**")
    st.write(f"• Category: {selected_category}")
    st.write(f"• States: {', '.join(selected_states) if selected_states else 'None'}")
    st.write(f"• Satisfaction: {satisfaction_filter}")
    st.write(f"• Order Value: R$ {order_value_range[0]:.0f} - R$ {order_value_range[1]:.0f}")

with status_col2:
    st.markdown("**Analysis Settings:**")
    st.write(f"• Date Range: {start_date} to {end_date}")
    st.write(f"• Show Trends: {'Yes' if show_trends else 'No'}")
    st.write(f"• Include Weekends: {'Yes' if include_weekends else 'No'}")
    st.write(f"• Minimum Orders: {min_orders}")

# Footer
st.markdown("---")
st.markdown(
    "**🎛️ Widget Demo** | "
    "Built with Streamlit | "
    "**📊 Data:** Simulated E-commerce | "
    f"**🕒 Last Updated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
)
