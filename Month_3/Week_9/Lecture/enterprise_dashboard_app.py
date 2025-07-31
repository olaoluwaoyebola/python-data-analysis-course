
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from datetime import datetime, timedelta
import time

# Configure page with enterprise settings
st.set_page_config(
    page_title="Olist Business Intelligence Platform",
    page_icon="🏢",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://olist.com/support',
        'Report a bug': 'https://olist.com/bug-report',
        'About': "Olist Business Intelligence Platform v2.1"
    }
)

# Custom CSS for enterprise branding
st.markdown("""
<style>
    /* Corporate Header */
    .main-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 10px;
        color: white;
        margin-bottom: 2rem;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    
    /* Navigation Styling */
    .nav-container {
        background: #f8f9fa;
        padding: 1rem;
        border-radius: 8px;
        border-left: 4px solid #667eea;
        margin-bottom: 1rem;
    }
    
    /* KPI Cards */
    .kpi-card {
        background: white;
        padding: 1.5rem;
        border-radius: 8px;
        border: 1px solid #e0e0e0;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        margin: 0.5rem 0;
    }
    
    /* Status Indicators */
    .status-green {
        background: #d4edda;
        border: 1px solid #c3e6cb;
        color: #155724;
        padding: 0.75rem;
        border-radius: 5px;
        border-left: 4px solid #28a745;
    }
    
    .status-yellow {
        background: #fff3cd;
        border: 1px solid #ffeaa7;
        color: #856404;
        padding: 0.75rem;
        border-radius: 5px;
        border-left: 4px solid #ffc107;
    }
    
    .status-red {
        background: #f8d7da;
        border: 1px solid #f5c6cb;
        color: #721c24;
        padding: 0.75rem;
        border-radius: 5px;
        border-left: 4px solid #dc3545;
    }
    
    /* Chart Containers */
    .chart-container {
        background: white;
        padding: 1rem;
        border-radius: 8px;
        border: 1px solid #e0e0e0;
        margin: 1rem 0;
    }
    
    /* Footer */
    .footer {
        text-align: center;
        color: #666;
        padding: 2rem;
        border-top: 1px solid #e0e0e0;
        margin-top: 3rem;
    }
</style>
""", unsafe_allow_html=True)

# Session state initialization
if 'user_role' not in st.session_state:
    st.session_state.user_role = 'Executive'
if 'selected_page' not in st.session_state:
    st.session_state.selected_page = 'Dashboard Overview'

# Generate comprehensive business data
@st.cache_data(ttl=600)  # Cache for 10 minutes
def generate_enterprise_data():
    """
    Generate comprehensive business data for enterprise dashboard.
    """
    np.random.seed(42)
    
    # Generate 6 months of daily data
    end_date = datetime.now()
    start_date = end_date - timedelta(days=180)
    date_range = pd.date_range(start_date, end_date, freq='D')
    
    # Simulate business growth and seasonality
    base_orders = 1000
    growth_trend = np.arange(len(date_range)) * 2
    seasonal = np.sin(np.arange(len(date_range)) * 2 * np.pi / 30) * 100  # Monthly cycle
    weekly = np.sin(np.arange(len(date_range)) * 2 * np.pi / 7) * 50      # Weekly cycle
    noise = np.random.normal(0, 50, len(date_range))
    
    daily_orders = base_orders + growth_trend + seasonal + weekly + noise
    daily_orders = np.maximum(daily_orders, 100)  # Minimum orders
    
    # Generate correlated business metrics
    revenue_per_order = np.random.normal(85, 15, len(date_range))
    daily_revenue = daily_orders * revenue_per_order
    
    customer_satisfaction = np.random.normal(4.2, 0.4, len(date_range))
    customer_satisfaction = np.clip(customer_satisfaction, 1, 5)
    
    # Create main DataFrame
    df = pd.DataFrame({
        'date': date_range,
        'orders': daily_orders.astype(int),
        'revenue': daily_revenue,
        'customer_satisfaction': customer_satisfaction,
        'new_customers': (daily_orders * np.random.uniform(0.3, 0.7, len(date_range))).astype(int),
        'returning_customers': (daily_orders * np.random.uniform(0.3, 0.7, len(date_range))).astype(int),
        'conversion_rate': np.random.normal(3.8, 0.6, len(date_range)),
        'avg_order_value': revenue_per_order
    })
    
    # Generate department-specific data
    departments = ['Sales', 'Marketing', 'Operations', 'Customer Service', 'Finance']
    dept_data = []
    
    for dept in departments:
        performance = np.random.uniform(0.7, 1.3, len(date_range))
        target_achievement = np.random.normal(95, 10, len(date_range))
        
        dept_df = pd.DataFrame({
            'date': date_range,
            'department': dept,
            'performance_score': performance,
            'target_achievement': np.clip(target_achievement, 60, 130),
            'team_size': np.random.randint(5, 25),
            'budget_utilization': np.random.uniform(0.8, 1.1, len(date_range))
        })
        dept_data.append(dept_df)
    
    dept_df = pd.concat(dept_data, ignore_index=True)
    
    return df, dept_df

# Load enterprise data
main_df, dept_df = generate_enterprise_data()

# Corporate Header
st.markdown("""
<div class="main-header">
    <h1>🏢 Olist Business Intelligence Platform</h1>
    <p>Enterprise Dashboard • Real-time Analytics • Strategic Insights</p>
</div>
""", unsafe_allow_html=True)

# Navigation and Role Selection
nav_col1, nav_col2, nav_col3 = st.columns([2, 2, 1])

with nav_col1:
    st.markdown('<div class="nav-container">', unsafe_allow_html=True)
    user_role = st.selectbox(
        "👤 Select Your Role:",
        ['Executive', 'Manager', 'Analyst', 'Sales Director'],
        index=['Executive', 'Manager', 'Analyst', 'Sales Director'].index(st.session_state.user_role)
    )
    st.session_state.user_role = user_role
    st.markdown('</div>', unsafe_allow_html=True)

with nav_col2:
    st.markdown('<div class="nav-container">', unsafe_allow_html=True)
    
    # Role-based page options
    if user_role == 'Executive':
        page_options = ['Dashboard Overview', 'Strategic Metrics', 'Board Report']
    elif user_role == 'Manager':
        page_options = ['Dashboard Overview', 'Team Performance', 'Operations', 'Budget Analysis']
    elif user_role == 'Analyst':
        page_options = ['Dashboard Overview', 'Data Explorer', 'Custom Reports', 'Export Center']
    else:  # Sales Director
        page_options = ['Dashboard Overview', 'Sales Performance', 'Territory Analysis', 'Customer Insights']
    
    selected_page = st.selectbox(
        "📊 Navigate to:",
        page_options
    )
    st.session_state.selected_page = selected_page
    st.markdown('</div>', unsafe_allow_html=True)

with nav_col3:
    st.markdown('<div class="nav-container">', unsafe_allow_html=True)
    st.markdown(f"**🕒 Last Updated**<br>{datetime.now().strftime('%H:%M:%S')}", unsafe_allow_html=True)
    if st.button("🔄 Refresh"):
        st.cache_data.clear()
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

# Page Content Based on Selection
st.markdown("---")

# Calculate current period metrics
current_month = main_df.tail(30)
previous_month = main_df.iloc[-60:-30]

total_orders_current = current_month['orders'].sum()
total_orders_previous = previous_month['orders'].sum()
orders_growth = ((total_orders_current - total_orders_previous) / total_orders_previous * 100)

total_revenue_current = current_month['revenue'].sum()
total_revenue_previous = previous_month['revenue'].sum()
revenue_growth = ((total_revenue_current - total_revenue_previous) / total_revenue_previous * 100)

avg_satisfaction = current_month['customer_satisfaction'].mean()

# Dashboard Overview (Common to all roles)
if selected_page == 'Dashboard Overview':
    st.subheader(f"📊 {user_role} Dashboard Overview")
    
    # Role-specific KPIs
    if user_role == 'Executive':
        kpi_col1, kpi_col2, kpi_col3, kpi_col4, kpi_col5 = st.columns(5)
        
        with kpi_col1:
            st.metric(
                "💰 Monthly Revenue",
                f"R$ {total_revenue_current:,.0f}",
                f"{revenue_growth:+.1f}%"
            )
        
        with kpi_col2:
            st.metric(
                "⭐ Customer Satisfaction",
                f"{avg_satisfaction:.2f}/5.0",
                "Target: 4.0+"
            )
        
        with kpi_col3:
            market_share = 23.5  # Simulated
            st.metric(
                "📈 Market Share",
                f"{market_share:.1f}%",
                "+1.2%"
            )
        
        with kpi_col4:
            customer_ltv = 485.50  # Simulated
            st.metric(
                "👥 Customer LTV",
                f"R$ {customer_ltv:.0f}",
                "+5.3%"
            )
        
        with kpi_col5:
            operating_margin = 18.7  # Simulated
            st.metric(
                "💼 Operating Margin",
                f"{operating_margin:.1f}%",
                "+0.8%"
            )
    
    elif user_role == 'Manager':
        kpi_col1, kpi_col2, kpi_col3, kpi_col4 = st.columns(4)
        
        with kpi_col1:
            st.metric(
                "📦 Daily Orders",
                f"{current_month['orders'].iloc[-1]:,}",
                f"{orders_growth:+.1f}%"
            )
        
        with kpi_col2:
            fulfillment_rate = 98.5  # Simulated
            st.metric(
                "🚚 Fulfillment Rate",
                f"{fulfillment_rate:.1f}%",
                "Target: 95%+"
            )
        
        with kpi_col3:
            team_productivity = 87.3  # Simulated
            st.metric(
                "👨‍💼 Team Productivity",
                f"{team_productivity:.1f}%",
                "+2.1%"
            )
        
        with kpi_col4:
            budget_utilization = 94.2  # Simulated
            st.metric(
                "💰 Budget Utilization",
                f"{budget_utilization:.1f}%",
                "On Track"
            )
    
    # Status Dashboard
    st.subheader("🚨 System Status & Alerts")
    
    status_col1, status_col2, status_col3 = st.columns(3)
    
    with status_col1:
        if avg_satisfaction >= 4.0:
            st.markdown("""
            <div class="status-green">
                <strong>✅ Customer Satisfaction</strong><br>
                Above target threshold
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown("""
            <div class="status-yellow">
                <strong>⚠️ Customer Satisfaction</strong><br>
                Below target - attention needed
            </div>
            """, unsafe_allow_html=True)
    
    with status_col2:
        if revenue_growth > 0:
            st.markdown("""
            <div class="status-green">
                <strong>📈 Revenue Growth</strong><br>
                Positive month-over-month growth
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown("""
            <div class="status-red">
                <strong>📉 Revenue Decline</strong><br>
                Immediate attention required
            </div>
            """, unsafe_allow_html=True)
    
    with status_col3:
        system_health = 99.2  # Simulated
        if system_health >= 99:
            st.markdown("""
            <div class="status-green">
                <strong>🔧 System Health</strong><br>
                All systems operational
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown("""
            <div class="status-yellow">
                <strong>⚠️ System Issues</strong><br>
                Minor performance degradation
            </div>
            """, unsafe_allow_html=True)
    
    # Key Performance Charts
    st.subheader("📈 Performance Analytics")
    
    chart_col1, chart_col2 = st.columns(2)
    
    with chart_col1:
        # Revenue trend
        monthly_data = main_df.groupby(main_df['date'].dt.to_period('M')).agg({
            'revenue': 'sum',
            'orders': 'sum'
        }).reset_index()
        monthly_data['date'] = monthly_data['date'].astype(str)
        
        fig = px.line(
            monthly_data,
            x='date',
            y='revenue',
            title="Monthly Revenue Trend",
            labels={'revenue': 'Revenue (R$)', 'date': 'Month'}
        )
        fig.update_traces(line=dict(width=3, color='#667eea'))
        fig.update_layout(height=400)
        st.plotly_chart(fig, use_container_width=True)
    
    with chart_col2:
        # Department performance
        latest_dept = dept_df.groupby('department')['target_achievement'].mean().reset_index()
        
        fig = px.bar(
            latest_dept.sort_values('target_achievement', ascending=True),
            x='target_achievement',
            y='department',
            orientation='h',
            title="Department Target Achievement",
            labels={'target_achievement': 'Target Achievement (%)', 'department': 'Department'},
            color='target_achievement',
            color_continuous_scale='RdYlGn'
        )
        fig.add_vline(x=100, line_dash="dash", line_color="red", 
                     annotation_text="Target")
        fig.update_layout(height=400)
        st.plotly_chart(fig, use_container_width=True)

# Role-specific pages
elif selected_page == 'Strategic Metrics' and user_role == 'Executive':
    st.subheader("🎯 Strategic Business Metrics")
    
    # Executive-level strategic dashboard
    strategy_col1, strategy_col2 = st.columns(2)
    
    with strategy_col1:
        # Customer acquisition funnel
        funnel_data = {
            'Stage': ['Visitors', 'Leads', 'Prospects', 'Customers', 'Repeat Customers'],
            'Count': [100000, 15000, 5000, 1900, 1200],
            'Conversion': [100, 15, 5, 1.9, 1.2]
        }
        funnel_df = pd.DataFrame(funnel_data)
        
        fig = go.Figure(go.Funnel(
            y = funnel_df['Stage'],
            x = funnel_df['Count'],
            textinfo = "value+percent initial"
        ))
        fig.update_layout(title="Customer Acquisition Funnel", height=400)
        st.plotly_chart(fig, use_container_width=True)
    
    with strategy_col2:
        # Market position analysis
        competitors = ['Olist', 'Mercado Livre', 'Amazon Brasil', 'Magazine Luiza', 'Others']
        market_share = [23.5, 35.2, 18.7, 12.1, 10.5]
        
        fig = px.pie(
            values=market_share,
            names=competitors,
            title="Brazilian E-commerce Market Share",
            color_discrete_sequence=px.colors.qualitative.Set3
        )
        fig.update_layout(height=400)
        st.plotly_chart(fig, use_container_width=True)

elif selected_page == 'Team Performance' and user_role == 'Manager':
    st.subheader("👨‍💼 Team Performance Dashboard")
    
    # Team performance metrics
    team_data = dept_df.groupby('department').agg({
        'performance_score': 'mean',
        'target_achievement': 'mean',
        'team_size': 'first',
        'budget_utilization': 'mean'
    }).reset_index()
    
    st.dataframe(
        team_data.style.format({
            'performance_score': '{:.2f}',
            'target_achievement': '{:.1f}%',
            'budget_utilization': '{:.1f}%'
        }),
        use_container_width=True
    )

elif selected_page == 'Data Explorer' and user_role == 'Analyst':
    st.subheader("🔍 Advanced Data Explorer")
    
    # Advanced filtering interface
    filter_col1, filter_col2, filter_col3 = st.columns(3)
    
    with filter_col1:
        date_range = st.date_input(
            "Date Range:",
            value=[main_df['date'].min().date(), main_df['date'].max().date()],
            min_value=main_df['date'].min().date(),
            max_value=main_df['date'].max().date()
        )
    
    with filter_col2:
        metric_selection = st.multiselect(
            "Metrics to Analyze:",
            ['orders', 'revenue', 'customer_satisfaction', 'conversion_rate'],
            default=['orders', 'revenue']
        )
    
    with filter_col3:
        aggregation = st.selectbox(
            "Aggregation Level:",
            ['Daily', 'Weekly', 'Monthly']
        )
    
    # Display filtered data
    if len(date_range) == 2:
        filtered_data = main_df[
            (main_df['date'].dt.date >= date_range[0]) &
            (main_df['date'].dt.date <= date_range[1])
        ]
        
        st.dataframe(filtered_data[['date'] + metric_selection], use_container_width=True)

elif selected_page == 'Sales Performance' and user_role == 'Sales Director':
    st.subheader("💼 Sales Performance Analytics")
    
    # Sales-specific metrics
    sales_col1, sales_col2, sales_col3 = st.columns(3)
    
    with sales_col1:
        quota_achievement = 112.5  # Simulated
        st.metric(
            "🎯 Quota Achievement",
            f"{quota_achievement:.1f}%",
            "+12.5%"
        )
    
    with sales_col2:
        pipeline_value = 2850000  # Simulated
        st.metric(
            "💰 Pipeline Value",
            f"R$ {pipeline_value:,.0f}",
            "Q4 Target"
        )
    
    with sales_col3:
        win_rate = 23.8  # Simulated
        st.metric(
            "🏆 Win Rate",
            f"{win_rate:.1f}%",
            "+1.2%"
        )

# Sidebar Information
with st.sidebar:
    st.header("ℹ️ Dashboard Information")
    
    st.markdown(f"""
    **Current User**: {user_role}  
    **Active Page**: {selected_page}  
    **Data Period**: Last 6 months  
    **Update Frequency**: Real-time  
    **Last Refresh**: {datetime.now().strftime('%H:%M:%S')}
    """)
    
    st.markdown("---")
    st.subheader("📊 Quick Actions")
    
    if st.button("📄 Export Report"):
        st.success("✅ Report exported successfully!")
    
    if st.button("📧 Email Summary"):
        st.success("✅ Summary sent to stakeholders!")
    
    if st.button("⚙️ Settings"):
        st.info("Settings panel would open here")
    
    st.markdown("---")
    st.subheader("🔗 Quick Links")
    st.markdown("""
    - [📊 Full Analytics](https://analytics.olist.com)
    - [📈 Financial Reports](https://finance.olist.com)
    - [👥 HR Dashboard](https://hr.olist.com)
    - [🛠️ Admin Panel](https://admin.olist.com)
    """)

# Footer
st.markdown("""
<div class="footer">
    <p><strong>🏢 Olist Business Intelligence Platform v2.1</strong></p>
    <p>Built with Streamlit | Real-time Supabase Integration | 
    <a href="#" style="color: #667eea;">Support</a> | 
    <a href="#" style="color: #667eea;">Documentation</a> | 
    <a href="#" style="color: #667eea;">API</a></p>
</div>
""", unsafe_allow_html=True)
