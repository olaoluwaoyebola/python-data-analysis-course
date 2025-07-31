
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import os

# Configure page
st.set_page_config(
    page_title="Live Supabase Dashboard",
    page_icon="🔗",
    layout="wide"
)

st.title("🔗 Live Supabase Data Integration")
st.markdown("**Real-time business dashboard with live database connectivity**")

# Supabase connection helper
@st.cache_resource
def init_supabase_connection():
    """
    Initialize Supabase connection using environment variables or Streamlit secrets.
    In production, use st.secrets for secure credential management.
    """
    try:
        # Try to get credentials from Streamlit secrets first
        if hasattr(st, 'secrets') and 'supabase' in st.secrets:
            url = st.secrets['supabase']['url']
            key = st.secrets['supabase']['anon_key']
        else:
            # Fallback to environment variables
            url = os.getenv('SUPABASE_URL')
            key = os.getenv('SUPABASE_ANON_KEY')
        
        if not url or not key:
            st.error("❌ Supabase credentials not found. Please set up your credentials.")
            st.info(
                "Add your Supabase URL and anon key to `.streamlit/secrets.toml` "
                "or set SUPABASE_URL and SUPABASE_ANON_KEY environment variables."
            )
            return None
        
        # Note: In a real application, you would import and use the supabase client here
        # from supabase import create_client, Client
        # supabase: Client = create_client(url, key)
        # return supabase
        
        # For this demo, we'll simulate the connection
        st.success("✅ Supabase connection established!")
        return {'url': url, 'status': 'connected'}
        
    except Exception as e:
        st.error(f"❌ Failed to connect to Supabase: {str(e)}")
        return None

# Data loading functions that would query Supabase
@st.cache_data(ttl=300)  # Cache for 5 minutes
def load_orders_data(supabase_client, limit=1000):
    """
    Load orders data from Supabase.
    In production, this would execute actual Supabase queries.
    """
    if not supabase_client:
        return None
    
    # Simulated query: supabase_client.table('orders').select('*').limit(limit).execute()
    # For demo, generate realistic data
    np.random.seed(42)
    
    dates = pd.date_range('2024-01-01', periods=limit, freq='H')
    
    data = {
        'order_id': [f"ORD_{i:08d}" for i in range(1, limit + 1)],
        'customer_id': [f"CUST_{np.random.randint(1, 10000):06d}" for _ in range(limit)],
        'order_date': dates,
        'product_category': np.random.choice([
            'Electronics', 'Fashion', 'Home & Garden', 'Books', 'Sports',
            'Beauty', 'Automotive', 'Toys', 'Health', 'Food'
        ], limit),
        'order_value': np.random.exponential(100, limit),
        'customer_state': np.random.choice([
            'SP', 'RJ', 'MG', 'BA', 'PR', 'RS', 'PE', 'CE', 'SC', 'GO'
        ], limit),
        'order_status': np.random.choice([
            'completed', 'processing', 'shipped', 'cancelled'
        ], limit, p=[0.8, 0.1, 0.08, 0.02]),
        'satisfaction_score': np.random.choice([1, 2, 3, 4, 5], limit, p=[0.05, 0.1, 0.2, 0.35, 0.3])
    }
    
    df = pd.DataFrame(data)
    df['order_value'] = np.round(df['order_value'], 2)
    
    return df

@st.cache_data(ttl=300)
def load_customer_metrics(supabase_client):
    """
    Load customer metrics from Supabase.
    """
    if not supabase_client:
        return None
    
    # Simulated aggregated metrics query
    metrics = {
        'total_customers': 45230,
        'new_customers_today': 127,
        'customer_ltv': 485.50,
        'churn_rate': 2.3,
        'avg_satisfaction': 4.2,
        'nps_score': 67
    }
    
    return metrics

# Initialize connection
supabase_client = init_supabase_connection()

if supabase_client:
    # Sidebar controls
    st.sidebar.header("🔧 Database Controls")
    
    # Data refresh controls
    if st.sidebar.button("🔄 Refresh Data"):
        st.cache_data.clear()
        st.success("✅ Data refreshed from Supabase!")
        st.rerun()
    
    # Query limit
    query_limit = st.sidebar.slider(
        "Query Limit:",
        min_value=100,
        max_value=5000,
        value=1000,
        step=100,
        help="Limit number of records to fetch for performance"
    )
    
    # Filter controls
    st.sidebar.subheader("📊 Data Filters")
    
    date_filter = st.sidebar.date_input(
        "Orders Since:",
        value=datetime.now().date() - timedelta(days=30),
        help="Filter orders from this date forward"
    )
    
    status_filter = st.sidebar.multiselect(
        "Order Status:",
        ['completed', 'processing', 'shipped', 'cancelled'],
        default=['completed', 'processing', 'shipped']
    )
    
    # Load data
    with st.spinner("🔄 Loading data from Supabase..."):
        orders_df = load_orders_data(supabase_client, query_limit)
        customer_metrics = load_customer_metrics(supabase_client)
    
    if orders_df is not None and customer_metrics is not None:
        # Apply filters
        filtered_orders = orders_df[
            (orders_df['order_date'].dt.date >= date_filter) &
            (orders_df['order_status'].isin(status_filter))
        ]
        
        # Display connection info
        info_col1, info_col2, info_col3 = st.columns(3)
        
        with info_col1:
            st.info(f"🔗 **Connected to Supabase**\n\nRecords loaded: {len(orders_df):,}")
        
        with info_col2:
            st.info(f"📊 **Filtered Dataset**\n\nRecords after filters: {len(filtered_orders):,}")
        
        with info_col3:
            st.info(f"🕒 **Last Updated**\n\n{datetime.now().strftime('%H:%M:%S')}")
        
        # Live KPIs from Supabase
        st.subheader("📊 Live Business Metrics")
        
        kpi_col1, kpi_col2, kpi_col3, kpi_col4, kpi_col5, kpi_col6 = st.columns(6)
        
        with kpi_col1:
            st.metric(
                "👥 Total Customers",
                f"{customer_metrics['total_customers']:,}",
                f"+{customer_metrics['new_customers_today']}"
            )
        
        with kpi_col2:
            total_revenue = filtered_orders['order_value'].sum()
            st.metric(
                "💰 Revenue",
                f"R$ {total_revenue:,.0f}",
                "Live data"
            )
        
        with kpi_col3:
            avg_order_value = filtered_orders['order_value'].mean()
            st.metric(
                "💳 Avg Order Value",
                f"R$ {avg_order_value:.2f}",
                "Real-time"
            )
        
        with kpi_col4:
            st.metric(
                "⭐ Satisfaction",
                f"{customer_metrics['avg_satisfaction']:.1f}/5.0",
                f"NPS: {customer_metrics['nps_score']}"
            )
        
        with kpi_col5:
            st.metric(
                "💼 Customer LTV",
                f"R$ {customer_metrics['customer_ltv']:.2f}",
                "Lifetime Value"
            )
        
        with kpi_col6:
            st.metric(
                "📉 Churn Rate",
                f"{customer_metrics['churn_rate']:.1f}%",
                "Monthly"
            )
        
        # Interactive visualizations
        st.markdown("---")
        st.subheader("📈 Live Data Visualizations")
        
        viz_col1, viz_col2 = st.columns(2)
        
        with viz_col1:
            # Revenue by category
            category_revenue = filtered_orders.groupby('product_category')['order_value'].sum().reset_index()
            category_revenue = category_revenue.sort_values('order_value', ascending=False)
            
            fig = px.bar(
                category_revenue,
                x='product_category',
                y='order_value',
                title="Revenue by Product Category (Live Data)",
                labels={'order_value': 'Revenue (R$)', 'product_category': 'Category'}
            )
            fig.update_xaxes(tickangle=45)
            st.plotly_chart(fig, use_container_width=True)
        
        with viz_col2:
            # Orders by state
            state_orders = filtered_orders['customer_state'].value_counts().reset_index()
            state_orders.columns = ['state', 'orders']
            
            fig = px.pie(
                state_orders.head(8),  # Top 8 states
                values='orders',
                names='state',
                title="Orders by State (Top 8)"
            )
            st.plotly_chart(fig, use_container_width=True)
        
        # Time series analysis
        st.subheader("📊 Time Series Analysis")
        
        # Daily revenue trend
        daily_revenue = filtered_orders.groupby(
            filtered_orders['order_date'].dt.date
        ).agg({
            'order_value': 'sum',
            'order_id': 'count',
            'satisfaction_score': 'mean'
        }).reset_index()
        
        daily_revenue.columns = ['date', 'revenue', 'orders', 'avg_satisfaction']
        
        # Create subplot with secondary y-axis
        fig = go.Figure()
        
        # Revenue line
        fig.add_trace(
            go.Scatter(
                x=daily_revenue['date'],
                y=daily_revenue['revenue'],
                mode='lines+markers',
                name='Daily Revenue',
                line=dict(color='#1f77b4', width=3)
            )
        )
        
        fig.update_layout(
            title="Daily Revenue Trend (Live Supabase Data)",
            xaxis_title="Date",
            yaxis_title="Revenue (R$)",
            height=400
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
        # Data preview
        st.subheader("📋 Live Data Preview")
        
        preview_tabs = st.tabs(["📦 Recent Orders", "📊 Summary Stats", "🔍 Raw Data"])
        
        with preview_tabs[0]:
            # Show recent orders
            recent_orders = filtered_orders.nlargest(10, 'order_date')
            st.dataframe(
                recent_orders[[
                    'order_id', 'order_date', 'product_category',
                    'order_value', 'customer_state', 'order_status'
                ]],
                use_container_width=True
            )
        
        with preview_tabs[1]:
            # Summary statistics
            stats_col1, stats_col2 = st.columns(2)
            
            with stats_col1:
                st.markdown("**📊 Order Statistics**")
                st.write(f"Total Orders: {len(filtered_orders):,}")
                st.write(f"Total Revenue: R$ {filtered_orders['order_value'].sum():,.2f}")
                st.write(f"Average Order Value: R$ {filtered_orders['order_value'].mean():.2f}")
                st.write(f"Median Order Value: R$ {filtered_orders['order_value'].median():.2f}")
            
            with stats_col2:
                st.markdown("**⭐ Quality Metrics**")
                st.write(f"Average Satisfaction: {filtered_orders['satisfaction_score'].mean():.2f}/5.0")
                completion_rate = (filtered_orders['order_status'] == 'completed').mean() * 100
                st.write(f"Completion Rate: {completion_rate:.1f}%")
                st.write(f"Unique Customers: {filtered_orders['customer_id'].nunique():,}")
                st.write(f"Product Categories: {filtered_orders['product_category'].nunique()}")
        
        with preview_tabs[2]:
            # Raw data with search
            search_term = st.text_input("🔍 Search orders (by Order ID or Customer ID):")
            
            if search_term:
                search_results = filtered_orders[
                    (filtered_orders['order_id'].str.contains(search_term, case=False)) |
                    (filtered_orders['customer_id'].str.contains(search_term, case=False))
                ]
                st.dataframe(search_results, use_container_width=True)
            else:
                st.dataframe(filtered_orders.head(20), use_container_width=True)
        
        # Export functionality
        st.markdown("---")
        st.subheader("💾 Data Export")
        
        export_col1, export_col2, export_col3 = st.columns(3)
        
        with export_col1:
            if st.button("📊 Export to CSV"):
                csv = filtered_orders.to_csv(index=False)
                st.download_button(
                    label="⬇️ Download CSV",
                    data=csv,
                    file_name=f"olist_orders_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
                    mime="text/csv"
                )
        
        with export_col2:
            if st.button("📈 Export Summary Report"):
                summary_report = daily_revenue.to_csv(index=False)
                st.download_button(
                    label="⬇️ Download Report",
                    data=summary_report,
                    file_name=f"daily_summary_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
                    mime="text/csv"
                )
        
        with export_col3:
            if st.button("📧 Email Dashboard"):
                st.success("✅ Dashboard summary sent to stakeholders!")
                st.info("📧 Email functionality would be implemented here")
    
    else:
        st.error("❌ Failed to load data from Supabase")
        st.info("Please check your database connection and try again.")

else:
    # Show connection setup instructions
    st.warning("⚠️ Supabase connection not configured")
    
    with st.expander("🔧 Setup Instructions", expanded=True):
        st.markdown("""
        ### Setting up Supabase Connection
        
        To connect this dashboard to live Supabase data:
        
        1. **Create a `.streamlit/secrets.toml` file** in your project root:
        ```toml
        [supabase]
        url = "https://your-project.supabase.co"
        anon_key = "your-anon-key-here"
        ```
        
        2. **Or set environment variables**:
        ```bash
        export SUPABASE_URL="https://your-project.supabase.co"
        export SUPABASE_ANON_KEY="your-anon-key-here"
        ```
        
        3. **Install the Supabase client**:
        ```bash
        pip install supabase
        ```
        
        4. **Ensure your Supabase tables match the expected schema**:
        - `orders` table with columns: order_id, customer_id, order_date, product_category, order_value, customer_state, order_status, satisfaction_score
        - Proper Row Level Security (RLS) policies for data access
        
        5. **Restart your Streamlit app** after configuration
        """)

# Footer
st.markdown("---")
st.markdown(
    "**🔗 Live Supabase Integration** | "
    "Real-time business intelligence with secure database connectivity | "
    "**📚 Next:** Advanced dashboard features and deployment"
)
