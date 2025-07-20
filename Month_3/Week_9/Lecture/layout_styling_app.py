
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# Configure page with custom styling
st.set_page_config(
    page_title="Professional Layouts",
    page_icon="🎨",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for professional appearance
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(90deg, #1e3c72, #2a5298);
        padding: 2rem;
        border-radius: 10px;
        color: white;
        margin-bottom: 2rem;
    }
    
    .metric-container {
        background: #f8f9fa;
        padding: 1.5rem;
        border-radius: 8px;
        border-left: 4px solid #007bff;
        margin: 1rem 0;
    }
    
    .status-success {
        background: #d4edda;
        border: 1px solid #c3e6cb;
        color: #155724;
        padding: 1rem;
        border-radius: 5px;
    }
    
    .status-warning {
        background: #fff3cd;
        border: 1px solid #ffeaa7;
        color: #856404;
        padding: 1rem;
        border-radius: 5px;
    }
</style>
""", unsafe_allow_html=True)

# Professional header
st.markdown("""
<div class="main-header">
    <h1>🎨 Professional Layout & Styling</h1>
    <p>Enterprise-grade dashboard design patterns for business applications</p>
</div>
""", unsafe_allow_html=True)

# Sample data
@st.cache_data
def load_sample_metrics():
    return {
        'revenue': 1250000,
        'growth': 15.3,
        'customers': 45230,
        'satisfaction': 4.2,
        'orders': 12450,
        'conversion': 3.8
    }

metrics = load_sample_metrics()

# Executive summary section
st.subheader("📊 Executive Summary")

# Multi-column layout for KPIs
kpi_col1, kpi_col2, kpi_col3, kpi_col4, kpi_col5, kpi_col6 = st.columns(6)

with kpi_col1:
    st.metric(
        label="💰 Revenue",
        value=f"R$ {metrics['revenue']:,.0f}",
        delta=f"+{metrics['growth']:.1f}%"
    )

with kpi_col2:
    st.metric(
        label="👥 Customers",
        value=f"{metrics['customers']:,}",
        delta="+1,234"
    )

with kpi_col3:
    st.metric(
        label="📦 Orders",
        value=f"{metrics['orders']:,}",
        delta="+567"
    )

with kpi_col4:
    st.metric(
        label="⭐ Satisfaction",
        value=f"{metrics['satisfaction']:.1f}/5.0",
        delta="+0.2"
    )

with kpi_col5:
    st.metric(
        label="🎯 Conversion",
        value=f"{metrics['conversion']:.1f}%",
        delta="+0.3%"
    )

with kpi_col6:
    # Status indicator
    if metrics['satisfaction'] > 4.0:
        st.markdown("""
        <div class="status-success">
            <strong>✅ System Status</strong><br>
            All systems operational
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <div class="status-warning">
            <strong>⚠️ System Status</strong><br>
            Attention required
        </div>
        """, unsafe_allow_html=True)

# Tabbed interface for different views
st.markdown("---")
tab1, tab2, tab3, tab4 = st.tabs(["📈 Performance", "🎯 Marketing", "⚙️ Operations", "💰 Finance"])

with tab1:
    st.subheader("Performance Analytics")
    
    # Two-column layout for charts
    perf_col1, perf_col2 = st.columns(2)
    
    with perf_col1:
        # Generate sample time series data
        dates = pd.date_range('2024-01-01', periods=12, freq='M')
        revenue_data = np.random.normal(100000, 15000, 12).cumsum()
        
        fig = px.line(
            x=dates, 
            y=revenue_data,
            title="Monthly Revenue Trend",
            labels={'x': 'Month', 'y': 'Revenue (R$)'}
        )
        fig.update_layout(height=400)
        st.plotly_chart(fig, use_container_width=True)
    
    with perf_col2:
        # Customer acquisition data
        channels = ['Organic', 'Paid Search', 'Social Media', 'Email', 'Direct']
        acquisitions = [1250, 890, 650, 420, 380]
        
        fig = px.bar(
            x=channels,
            y=acquisitions,
            title="Customer Acquisition by Channel",
            labels={'x': 'Channel', 'y': 'New Customers'}
        )
        fig.update_layout(height=400)
        st.plotly_chart(fig, use_container_width=True)

with tab2:
    st.subheader("Marketing Performance")
    
    # Campaign performance table
    campaign_data = pd.DataFrame({
        'Campaign': ['Summer Sale', 'Back to School', 'Holiday Special', 'New Year Promo'],
        'Impressions': [125000, 98000, 156000, 87000],
        'Clicks': [3750, 2940, 4680, 2610],
        'Conversions': [187, 147, 234, 130],
        'Cost (R$)': [12500, 9800, 15600, 8700],
        'ROI (%)': [15.2, 12.8, 18.7, 14.3]
    })
    
    st.dataframe(
        campaign_data.style.format({
            'Impressions': '{:,}',
            'Clicks': '{:,}',
            'Cost (R$)': 'R$ {:,.0f}',
            'ROI (%)': '{:.1f}%'
        }),
        use_container_width=True
    )
    
    # Channel effectiveness
    marketing_col1, marketing_col2 = st.columns(2)
    
    with marketing_col1:
        fig = px.pie(
            values=campaign_data['Conversions'],
            names=campaign_data['Campaign'],
            title="Conversions by Campaign"
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with marketing_col2:
        fig = px.scatter(
            campaign_data,
            x='Cost (R$)',
            y='Conversions',
            size='Impressions',
            color='ROI (%)',
            title="Campaign Cost vs. Conversions",
            hover_data=['Campaign']
        )
        st.plotly_chart(fig, use_container_width=True)

with tab3:
    st.subheader("Operations Dashboard")
    
    # Operational metrics in expandable sections
    with st.expander("📦 Order Processing Metrics", expanded=True):
        ops_col1, ops_col2, ops_col3 = st.columns(3)
        
        with ops_col1:
            st.metric("Orders Today", "1,247", "+12%")
            st.metric("Processing Time", "2.3 hrs", "-0.5 hrs")
        
        with ops_col2:
            st.metric("Fulfillment Rate", "98.7%", "+1.2%")
            st.metric("Return Rate", "2.1%", "-0.3%")
        
        with ops_col3:
            st.metric("Customer Issues", "23", "-5")
            st.metric("Resolution Time", "4.2 hrs", "-1.1 hrs")
    
    with st.expander("🚚 Logistics Performance"):
        # Delivery performance chart
        delivery_data = pd.DataFrame({
            'Region': ['São Paulo', 'Rio de Janeiro', 'Minas Gerais', 'Bahia', 'Paraná'],
            'On-time Delivery (%)': [94.2, 91.5, 89.8, 87.3, 92.1],
            'Average Delivery Time (days)': [2.1, 2.8, 3.2, 4.1, 2.5]
        })
        
        fig = px.bar(
            delivery_data,
            x='Region',
            y='On-time Delivery (%)',
            title="On-time Delivery by Region",
            color='Average Delivery Time (days)',
            color_continuous_scale='RdYlGn_r'
        )
        st.plotly_chart(fig, use_container_width=True)

with tab4:
    st.subheader("Financial Overview")
    
    # Financial summary cards
    fin_col1, fin_col2 = st.columns(2)
    
    with fin_col1:
        st.markdown("""
        <div class="metric-container">
            <h4>💰 Revenue Summary</h4>
            <p><strong>This Month:</strong> R$ 1,250,000</p>
            <p><strong>Last Month:</strong> R$ 1,087,000</p>
            <p><strong>Growth:</strong> +15.0% 📈</p>
            <p><strong>YTD Total:</strong> R$ 12,750,000</p>
        </div>
        """, unsafe_allow_html=True)
    
    with fin_col2:
        st.markdown("""
        <div class="metric-container">
            <h4>💳 Payment Analysis</h4>
            <p><strong>Credit Cards:</strong> 68.5%</p>
            <p><strong>Debit Cards:</strong> 18.2%</p>
            <p><strong>Bank Transfer:</strong> 9.8%</p>
            <p><strong>Digital Wallet:</strong> 3.5%</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Cost breakdown
    cost_data = pd.DataFrame({
        'Category': ['Product Costs', 'Marketing', 'Operations', 'Technology', 'Personnel'],
        'Amount': [650000, 125000, 89000, 67000, 234000],
        'Budget': [680000, 130000, 95000, 70000, 240000]
    })
    
    fig = px.bar(
        cost_data,
        x='Category',
        y=['Amount', 'Budget'],
        title="Actual vs. Budget Spending",
        barmode='group'
    )
    st.plotly_chart(fig, use_container_width=True)

# Sidebar configuration panel
with st.sidebar:
    st.header("🎛️ Dashboard Controls")
    
    # Theme selection
    theme = st.selectbox(
        "Dashboard Theme:",
        ['Professional Blue', 'Corporate Gray', 'Modern Dark', 'Clean White']
    )
    
    # Refresh settings
    auto_refresh = st.checkbox("Auto-refresh data", value=True)
    refresh_interval = st.slider("Refresh interval (minutes)", 1, 60, 5)
    
    # Export options
    st.markdown("---")
    st.subheader("📊 Export Options")
    
    if st.button("📄 Export PDF Report"):
        st.success("PDF report generated!")
    
    if st.button("📊 Export Excel Data"):
        st.success("Excel file downloaded!")
    
    if st.button("📧 Email Summary"):
        st.success("Summary emailed to stakeholders!")
    
    # User preferences
    st.markdown("---")
    st.subheader("👤 User Preferences")
    
    notifications = st.checkbox("Enable notifications", value=True)
    show_tooltips = st.checkbox("Show help tooltips", value=True)
    compact_view = st.checkbox("Compact view mode", value=False)

# Footer with professional styling
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666; padding: 2rem;">
    <p><strong>🏢 Olist Business Intelligence Platform</strong></p>
    <p>Built with Streamlit | Data updated in real-time | 
    <a href="#" style="color: #007bff;">Support</a> | 
    <a href="#" style="color: #007bff;">Documentation</a></p>
</div>
""", unsafe_allow_html=True)
