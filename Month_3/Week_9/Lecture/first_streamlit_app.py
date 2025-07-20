
# Your First Business Intelligence Dashboard
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Configure the page
st.set_page_config(
    page_title="Olist Business Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Main title
st.title("🇧🇷 Olist E-commerce Business Dashboard")
st.markdown("**Real-time insights from Brazilian marketplace data**")

# Create sample data (we'll replace this with live Supabase data later)
@st.cache_data
def load_sample_data():
    """
    Generate sample e-commerce data for demonstration.
    In production, this will connect to our Supabase database.
    """
    np.random.seed(42)
    dates = pd.date_range('2023-01-01', periods=100, freq='D')
    
    data = {
        'date': dates,
        'revenue': np.random.normal(50000, 10000, 100),
        'orders': np.random.poisson(200, 100),
        'customer_satisfaction': np.random.normal(4.2, 0.5, 100),
        'state': np.random.choice(['SP', 'RJ', 'MG', 'RS', 'PR'], 100)
    }
    
    return pd.DataFrame(data)

# Load data
df = load_sample_data()

# Sidebar filters
st.sidebar.header("🎛️ Dashboard Filters")
selected_state = st.sidebar.selectbox(
    "Select State:",
    options=['All'] + list(df['state'].unique())
)

# Filter data based on selection
if selected_state != 'All':
    filtered_df = df[df['state'] == selected_state]
else:
    filtered_df = df

# Main dashboard metrics
col1, col2, col3, col4 = st.columns(4)

with col1:
    total_revenue = filtered_df['revenue'].sum()
    st.metric(
        label="💰 Total Revenue",
        value=f"R$ {total_revenue:,.0f}",
        delta=f"{(total_revenue/1000000):.1f}M"
    )

with col2:
    total_orders = filtered_df['orders'].sum()
    st.metric(
        label="📦 Total Orders",
        value=f"{total_orders:,}",
        delta=f"{(total_orders/1000):.1f}K"
    )

with col3:
    avg_satisfaction = filtered_df['customer_satisfaction'].mean()
    st.metric(
        label="⭐ Customer Satisfaction",
        value=f"{avg_satisfaction:.2f}/5.0",
        delta=f"{((avg_satisfaction-4.0)/4.0)*100:.1f}%"
    )

with col4:
    avg_order_value = (filtered_df['revenue'] / filtered_df['orders']).mean()
    st.metric(
        label="💳 Average Order Value",
        value=f"R$ {avg_order_value:.0f}",
        delta="vs. last month"
    )

# Charts section
st.markdown("---")
st.subheader("📈 Performance Trends")

chart_col1, chart_col2 = st.columns(2)

with chart_col1:
    st.markdown("**Daily Revenue Trend**")
    fig, ax = plt.subplots(figsize=(10, 4))
    ax.plot(filtered_df['date'], filtered_df['revenue'], linewidth=2, color='#1f77b4')
    ax.set_xlabel('Date')
    ax.set_ylabel('Revenue (R$)')
    ax.tick_params(axis='x', rotation=45)
    plt.tight_layout()
    st.pyplot(fig)

with chart_col2:
    st.markdown("**Customer Satisfaction Distribution**")
    fig, ax = plt.subplots(figsize=(10, 4))
    ax.hist(filtered_df['customer_satisfaction'], bins=20, color='#ff7f0e', alpha=0.7)
    ax.set_xlabel('Satisfaction Score')
    ax.set_ylabel('Frequency')
    ax.axvline(avg_satisfaction, color='red', linestyle='--', 
               label=f'Average: {avg_satisfaction:.2f}')
    ax.legend()
    plt.tight_layout()
    st.pyplot(fig)

# Data preview
st.markdown("---")
st.subheader("📋 Data Preview")
st.markdown(f"Showing {len(filtered_df)} records for {selected_state if selected_state != 'All' else 'all states'}")
st.dataframe(filtered_df.head(10), use_container_width=True)

# Footer
st.markdown("---")
st.markdown(
    "**🔗 Data Source:** Olist Brazilian E-commerce | "
    "**📊 Dashboard:** Built with Streamlit | "
    "**🔄 Last Updated:** Real-time"
)
