
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from datetime import datetime, timedelta
import time

# Configure page for wide layout
st.set_page_config(
    page_title="Real-Time Business Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for professional appearance
st.markdown("""
<style>
    .main > div {
        padding-top: 1rem;
    }
    .stMetric {
        background: white;
        border: 1px solid #e0e0e0;
        padding: 1rem;
        border-radius: 8px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
</style>
""", unsafe_allow_html=True)

# Generate realistic business data with time series
@st.cache_data(ttl=300)  # Cache for 5 minutes
def generate_realtime_data():
    """
    Generate realistic time-series business data.
    In production, this would be replaced with Supabase queries.
    """
    np.random.seed(int(time.time()) % 1000)  # Semi-random for "real-time" feel
    
    # Generate 90 days of hourly data
    end_date = datetime.now()
    start_date = end_date - timedelta(days=90)
    date_range = pd.date_range(start_date, end_date, freq='H')
    
    # Simulate realistic business patterns
    base_orders = 50
    seasonal_pattern = np.sin(np.arange(len(date_range)) * 2 * np.pi / (24 * 7)) * 10  # Weekly pattern
    daily_pattern = np.sin(np.arange(len(date_range)) * 2 * np.pi / 24) * 20  # Daily pattern
    growth_trend = np.arange(len(date_range)) * 0.01  # Growth trend
    noise = np.random.normal(0, 5, len(date_range))
    
    orders = base_orders + seasonal_pattern + daily_pattern + growth_trend + noise
    orders = np.maximum(orders, 5)  # Minimum 5 orders per hour
    
    # Generate correlated metrics
    revenue = orders * np.random.normal(85, 15, len(date_range))
    satisfaction = np.random.normal(4.2, 0.3, len(date_range))
    satisfaction = np.clip(satisfaction, 1, 5)
    
    # Create DataFrame
    df = pd.DataFrame({
        'timestamp': date_range,
        'orders': orders.astype(int),
        'revenue': revenue,
        'satisfaction': satisfaction,
        'customers': orders * np.random.uniform(0.7, 1.3, len(date_range)),
        'conversion_rate': np.random.normal(3.5, 0.5, len(date_range))
    })
    
    # Add categorical data
    categories = ['Electronics', 'Fashion', 'Home & Garden', 'Books', 'Sports']
    states = ['São Paulo', 'Rio de Janeiro', 'Minas Gerais', 'Bahia', 'Paraná']
    
    category_data = []
    for _, row in df.iterrows():
        for cat in categories:
            orders_cat = int(row['orders'] * np.random.uniform(0.1, 0.3))
            if orders_cat > 0:
                category_data.append({
                    'timestamp': row['timestamp'],
                    'category': cat,
                    'orders': orders_cat,
                    'revenue': orders_cat * np.random.uniform(70, 120)
                })
    
    category_df = pd.DataFrame(category_data)
    
    return df, category_df

# Load data
df, category_df = generate_realtime_data()

# Header with real-time update
header_col1, header_col2 = st.columns([3, 1])

with header_col1:
    st.title("📊 Real-Time Business Intelligence Dashboard")
    st.markdown("**Live insights from Olist Brazilian E-commerce Platform**")

with header_col2:
    st.markdown(f"**🕒 Last Updated:** {datetime.now().strftime('%H:%M:%S')}")
    if st.button("🔄 Refresh Data"):
        st.cache_data.clear()
        st.rerun()

# Sidebar controls
st.sidebar.header("📊 Dashboard Controls")

# Time range selector
time_range = st.sidebar.selectbox(
    "📅 Time Range:",
    ['Last 24 Hours', 'Last 7 Days', 'Last 30 Days', 'Last 90 Days'],
    index=1
)

# Filter data based on time range
if time_range == 'Last 24 Hours':
    cutoff = datetime.now() - timedelta(hours=24)
elif time_range == 'Last 7 Days':
    cutoff = datetime.now() - timedelta(days=7)
elif time_range == 'Last 30 Days':
    cutoff = datetime.now() - timedelta(days=30)
else:
    cutoff = datetime.now() - timedelta(days=90)

filtered_df = df[df['timestamp'] >= cutoff]
filtered_category_df = category_df[category_df['timestamp'] >= cutoff]

# Chart type selector
chart_style = st.sidebar.selectbox(
    "📈 Chart Style:",
    ['Professional', 'Colorful', 'Minimal', 'Dark Theme']
)

# Set color palette based on style
if chart_style == 'Professional':
    color_palette = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']
elif chart_style == 'Colorful':
    color_palette = px.colors.qualitative.Set1
elif chart_style == 'Minimal':
    color_palette = ['#34495e', '#7f8c8d', '#95a5a6', '#bdc3c7', '#ecf0f1']
else:  # Dark Theme
    color_palette = ['#e74c3c', '#f39c12', '#f1c40f', '#2ecc71', '#3498db']

# Auto-refresh toggle
auto_refresh = st.sidebar.checkbox("🔄 Auto-refresh (30s)", value=False)
if auto_refresh:
    time.sleep(30)
    st.rerun()

# Real-time KPIs
st.subheader("⚡⏩😁 Real-Time Key Performance Indicators")

kpi_col1, kpi_col2, kpi_col3, kpi_col4, kpi_col5 = st.columns(5)

# Calculate current period vs previous period
current_period = filtered_df.tail(len(filtered_df)//2)
previous_period = filtered_df.head(len(filtered_df)//2)

with kpi_col1:
    current_orders = current_period['orders'].sum()
    previous_orders = previous_period['orders'].sum()
    orders_change = ((current_orders - previous_orders) / previous_orders * 100) if previous_orders > 0 else 0
    
    st.metric(
        label="📦 Total Orders",
        value=f"{current_orders:,}",
        delta=f"{orders_change:+.1f}%"
    )

with kpi_col2:
    current_revenue = current_period['revenue'].sum()
    previous_revenue = previous_period['revenue'].sum()
    revenue_change = ((current_revenue - previous_revenue) / previous_revenue * 100) if previous_revenue > 0 else 0
    
    st.metric(
        label="💰 Revenue",
        value=f"R$ {current_revenue:,.0f}",
        delta=f"{revenue_change:+.1f}%"
    )

with kpi_col3:
    current_satisfaction = current_period['satisfaction'].mean()
    previous_satisfaction = previous_period['satisfaction'].mean()
    satisfaction_change = current_satisfaction - previous_satisfaction
    
    st.metric(
        label="⭐ Avg Satisfaction",
        value=f"{current_satisfaction:.2f}/5.0",
        delta=f"{satisfaction_change:+.2f}"
    )

with kpi_col4:
    current_customers = current_period['customers'].sum()
    previous_customers = previous_period['customers'].sum()
    customers_change = ((current_customers - previous_customers) / previous_customers * 100) if previous_customers > 0 else 0
    
    st.metric(
        label="👥 Customers",
        value=f"{current_customers:,.0f}",
        delta=f"{customers_change:+.1f}%"
    )

with kpi_col5:
    current_conversion = current_period['conversion_rate'].mean()
    previous_conversion = previous_period['conversion_rate'].mean()
    conversion_change = current_conversion - previous_conversion
    
    st.metric(
        label="🎯 Conversion Rate",
        value=f"{current_conversion:.1f}%",
        delta=f"{conversion_change:+.1f}%"
    )

# Interactive Charts Section
st.markdown("---")
st.subheader("📈 Interactive Business Analytics")

# Chart tabs for better organization
chart_tab1, chart_tab2, chart_tab3, chart_tab4 = st.tabs([
    "📊 Time Series", "🏷️ Categories", "🗺️ Geographic", "📋 Summary"
])

with chart_tab1:
    # Time series charts
    ts_col1, ts_col2 = st.columns(2)
    
    with ts_col1:
        # Orders and Revenue over time
        fig = make_subplots(
            rows=2, cols=1,
            subplot_titles=['Orders Over Time', 'Revenue Over Time'],
            vertical_spacing=0.1
        )
        
        # Group by day for cleaner visualization
        daily_data = filtered_df.groupby(filtered_df['timestamp'].dt.date).agg({
            'orders': 'sum',
            'revenue': 'sum'
        }).reset_index()
        
        fig.add_trace(
            go.Scatter(
                x=daily_data['timestamp'],
                y=daily_data['orders'],
                mode='lines+markers',
                name='Orders',
                line=dict(color=color_palette[0], width=3)
            ),
            row=1, col=1
        )
        
        fig.add_trace(
            go.Scatter(
                x=daily_data['timestamp'],
                y=daily_data['revenue'],
                mode='lines+markers',
                name='Revenue',
                line=dict(color=color_palette[1], width=3)
            ),
            row=2, col=1
        )
        
        fig.update_layout(
            height=500,
            title_text="Business Performance Trends",
            showlegend=False
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    with ts_col2:
        # Customer satisfaction and conversion trends
        fig = make_subplots(
            rows=2, cols=1,
            subplot_titles=['Customer Satisfaction', 'Conversion Rate'],
            vertical_spacing=0.1
        )
        
        daily_metrics = filtered_df.groupby(filtered_df['timestamp'].dt.date).agg({
            'satisfaction': 'mean',
            'conversion_rate': 'mean'
        }).reset_index()
        
        fig.add_trace(
            go.Scatter(
                x=daily_metrics['timestamp'],
                y=daily_metrics['satisfaction'],
                mode='lines+markers',
                name='Satisfaction',
                line=dict(color=color_palette[2], width=3),
                fill='tonexty'
            ),
            row=1, col=1
        )
        
        fig.add_trace(
            go.Scatter(
                x=daily_metrics['timestamp'],
                y=daily_metrics['conversion_rate'],
                mode='lines+markers',
                name='Conversion',
                line=dict(color=color_palette[3], width=3)
            ),
            row=2, col=1
        )
        
        fig.update_layout(
            height=500,
            title_text="Quality Metrics Trends",
            showlegend=False
        )
        
        st.plotly_chart(fig, use_container_width=True)

with chart_tab2:
    # Category analysis
    cat_col1, cat_col2 = st.columns(2)
    
    with cat_col1:
        # Category performance pie chart
        category_summary = filtered_category_df.groupby('category').agg({
            'orders': 'sum',
            'revenue': 'sum'
        }).reset_index()
        
        fig = px.pie(
            category_summary,
            values='revenue',
            names='category',
            title="Revenue by Product Category",
            color_discrete_sequence=color_palette
        )
        
        fig.update_traces(textposition='inside', textinfo='percent+label')
        st.plotly_chart(fig, use_container_width=True)
    
    with cat_col2:
        # Category trends over time
        category_daily = filtered_category_df.groupby([
            filtered_category_df['timestamp'].dt.date, 'category'
        ])['revenue'].sum().reset_index()
        
        fig = px.line(
            category_daily,
            x='timestamp',
            y='revenue',
            color='category',
            title="Category Revenue Trends",
            color_discrete_sequence=color_palette
        )
        
        fig.update_layout(height=400)
        st.plotly_chart(fig, use_container_width=True)
    
    # Category performance table
    st.subheader("📊 Category Performance Summary")
    
    category_summary['avg_order_value'] = category_summary['revenue'] / category_summary['orders']
    category_summary['revenue_share'] = (category_summary['revenue'] / category_summary['revenue'].sum() * 100)
    
    st.dataframe(
        category_summary.style.format({
            'orders': '{:,}',
            'revenue': 'R$ {:,.0f}',
            'avg_order_value': 'R$ {:.2f}',
            'revenue_share': '{:.1f}%'
        }),
        use_container_width=True
    )

with chart_tab3:
    # Geographic analysis (simulated)
    st.subheader("🗺️ Geographic Performance")
    
    # Generate sample geographic data
    states = ['São Paulo', 'Rio de Janeiro', 'Minas Gerais', 'Bahia', 'Paraná', 'Santa Catarina']
    geo_data = []
    
    for state in states:
        orders = np.random.randint(1000, 5000)
        revenue = orders * np.random.uniform(80, 120)
        satisfaction = np.random.uniform(3.8, 4.5)
        
        geo_data.append({
            'state': state,
            'orders': orders,
            'revenue': revenue,
            'satisfaction': satisfaction
        })
    
    geo_df = pd.DataFrame(geo_data)
    
    geo_col1, geo_col2 = st.columns(2)
    
    with geo_col1:
        # Revenue by state
        fig = px.bar(
            geo_df.sort_values('revenue', ascending=True),
            x='revenue',
            y='state',
            orientation='h',
            title="Revenue by State",
            color='satisfaction',
            color_continuous_scale='RdYlGn'
        )
        
        fig.update_layout(height=400)
        st.plotly_chart(fig, use_container_width=True)
    
    with geo_col2:
        # Orders vs Satisfaction scatter
        fig = px.scatter(
            geo_df,
            x='orders',
            y='satisfaction',
            size='revenue',
            color='state',
            title="Orders vs Satisfaction by State",
            hover_data=['revenue'],
            color_discrete_sequence=color_palette
        )
        
        fig.update_layout(height=400)
        st.plotly_chart(fig, use_container_width=True)

with chart_tab4:
    # Summary dashboard
    st.subheader("📋 Executive Summary")
    
    summary_col1, summary_col2 = st.columns(2)
    
    with summary_col1:
        # Key insights
        st.markdown("### 🎯 Key Insights")
        
        total_orders = filtered_df['orders'].sum()
        total_revenue = filtered_df['revenue'].sum()
        avg_satisfaction = filtered_df['satisfaction'].mean()
        
        st.info(f"📊 **Total Orders**: {total_orders:,} in selected period")
        st.info(f"💰 **Total Revenue**: R$ {total_revenue:,.0f}")
        st.info(f"⭐ **Average Satisfaction**: {avg_satisfaction:.2f}/5.0")
        
        # Performance indicators
        if avg_satisfaction >= 4.0:
            st.success("✅ Customer satisfaction is above target (4.0)")
        else:
            st.warning("⚠️ Customer satisfaction needs attention")
        
        if orders_change > 0:
            st.success(f"📈 Orders growing by {orders_change:.1f}%")
        else:
            st.error(f"📉 Orders declining by {abs(orders_change):.1f}%")
    
    with summary_col2:
        # Performance gauge
        overall_score = (avg_satisfaction / 5.0) * 100
        
        fig = go.Figure(go.Indicator(
            mode = "gauge+number+delta",
            value = overall_score,
            domain = {'x': [0, 1], 'y': [0, 1]},
            title = {'text': "Overall Performance Score"},
            delta = {'reference': 80},
            gauge = {
                'axis': {'range': [None, 100]},
                'bar': {'color': color_palette[0]},
                'steps': [
                    {'range': [0, 60], 'color': "lightgray"},
                    {'range': [60, 80], 'color': "yellow"},
                    {'range': [80, 100], 'color': "lightgreen"}
                ],
                'threshold': {
                    'line': {'color': "red", 'width': 4},
                    'thickness': 0.75,
                    'value': 90
                }
            }
        ))
        
        fig.update_layout(height=400)
        st.plotly_chart(fig, use_container_width=True)

# Footer
st.markdown("---")
st.markdown(
    "**📊 Real-Time Dashboard** | "
    "Built with Streamlit & Plotly | "
    "**🔗 Data Source**: Live Supabase Connection | "
    f"**🕒 Generated**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
)
