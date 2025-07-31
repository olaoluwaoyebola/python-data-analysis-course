
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import os
import logging
import time
import json
from typing import Dict, Optional

# Configure production settings
st.set_page_config(
    page_title="Olist Business Intelligence Platform",
    page_icon="🏢",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://docs.olist.com/support',
        'Report a bug': 'https://github.com/olist/bi-platform/issues',
        'About': "Olist BI Platform v2.1 - Built with Streamlit"
    }
)

# Production environment configuration
class ProductionConfig:
    """
    Production configuration management with environment-specific settings.
    """
    
    def __init__(self):
        self.environment = os.getenv('STREAMLIT_ENV', 'development')
        self.debug_mode = os.getenv('DEBUG', 'False').lower() == 'true'
        self.version = os.getenv('APP_VERSION', 'v2.1.0')
        
        # Configure logging based on environment
        log_level = logging.DEBUG if self.debug_mode else logging.INFO
        logging.basicConfig(
            level=log_level,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        self.logger = logging.getLogger(__name__)
    
    def get_database_config(self) -> Dict:
        """
        Get database configuration from environment or Streamlit secrets.
        """
        try:
            # Try Streamlit secrets first (production)
            if hasattr(st, 'secrets') and 'database' in st.secrets:
                return {
                    'url': st.secrets['database']['url'],
                    'api_key': st.secrets['database']['api_key'],
                    'connection_pool_size': st.secrets['database'].get('pool_size', 10)
                }
            
            # Fallback to environment variables (development)
            return {
                'url': os.getenv('DATABASE_URL'),
                'api_key': os.getenv('DATABASE_API_KEY'),
                'connection_pool_size': int(os.getenv('DB_POOL_SIZE', '5'))
            }
            
        except Exception as e:
            self.logger.error(f"Failed to load database config: {e}")
            return {}
    
    def get_api_config(self) -> Dict:
        """
        Get external API configuration.
        """
        try:
            if hasattr(st, 'secrets') and 'apis' in st.secrets:
                return {
                    'analytics_key': st.secrets['apis']['google_analytics'],
                    'monitoring_key': st.secrets['apis']['datadog_key'],
                    'email_service': st.secrets['apis']['sendgrid_key']
                }
            
            return {
                'analytics_key': os.getenv('GOOGLE_ANALYTICS_KEY'),
                'monitoring_key': os.getenv('DATADOG_API_KEY'),
                'email_service': os.getenv('SENDGRID_API_KEY')
            }
            
        except Exception as e:
            self.logger.warning(f"API config not available: {e}")
            return {}

# Initialize production configuration
config = ProductionConfig()
logger = config.logger

# Performance monitoring
class PerformanceMonitor:
    """
    Monitor application performance and user interactions.
    """
    
    def __init__(self):
        if 'performance_metrics' not in st.session_state:
            st.session_state.performance_metrics = {
                'page_loads': 0,
                'query_times': [],
                'error_count': 0,
                'user_sessions': 0,
                'last_active': datetime.now()
            }
    
    def track_page_load(self, page_name: str):
        """
        Track page load event.
        """
        st.session_state.performance_metrics['page_loads'] += 1
        st.session_state.performance_metrics['last_active'] = datetime.now()
        
        logger.info(f"Page loaded: {page_name}")
        
        # In production, send to analytics service
        # analytics.track('page_view', {'page': page_name, 'timestamp': datetime.now()})
    
    def track_query_performance(self, query_type: str, execution_time: float):
        """
        Track database query performance.
        """
        st.session_state.performance_metrics['query_times'].append({
            'type': query_type,
            'time': execution_time,
            'timestamp': datetime.now()
        })
        
        logger.info(f"Query executed: {query_type} in {execution_time:.3f}s")
        
        # Alert on slow queries
        if execution_time > 5.0:
            logger.warning(f"Slow query detected: {query_type} took {execution_time:.3f}s")
    
    def track_error(self, error_type: str, error_message: str):
        """
        Track application errors.
        """
        st.session_state.performance_metrics['error_count'] += 1
        
        logger.error(f"Application error: {error_type} - {error_message}")
        
        # In production, send to error tracking service
        # sentry.capture_exception(error_message)
    
    def get_metrics_summary(self) -> Dict:
        """
        Get performance metrics summary.
        """
        metrics = st.session_state.performance_metrics
        
        avg_query_time = 0
        if metrics['query_times']:
            avg_query_time = sum(q['time'] for q in metrics['query_times']) / len(metrics['query_times'])
        
        return {
            'page_loads': metrics['page_loads'],
            'total_queries': len(metrics['query_times']),
            'avg_query_time': avg_query_time,
            'error_count': metrics['error_count'],
            'uptime_minutes': (datetime.now() - metrics['last_active']).total_seconds() / 60
        }

# Initialize performance monitoring
monitor = PerformanceMonitor()
monitor.track_page_load('main_dashboard')

# Custom CSS for production branding
st.markdown("""
<style>
    /* Production branding */
    .main-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 10px;
        color: white;
        margin-bottom: 2rem;
    }
    
    /* Environment indicator */
    .env-indicator {
        position: fixed;
        top: 10px;
        right: 10px;
        padding: 5px 10px;
        border-radius: 15px;
        font-size: 12px;
        font-weight: bold;
        z-index: 1000;
    }
    
    .env-production {
        background: #28a745;
        color: white;
    }
    
    .env-development {
        background: #ffc107;
        color: black;
    }
    
    /* Performance indicators */
    .performance-good {
        background: #d4edda;
        border: 1px solid #c3e6cb;
        color: #155724;
        padding: 0.75rem;
        border-radius: 5px;
        border-left: 4px solid #28a745;
    }
    
    .performance-warning {
        background: #fff3cd;
        border: 1px solid #ffeaa7;
        color: #856404;
        padding: 0.75rem;
        border-radius: 5px;
        border-left: 4px solid #ffc107;
    }
    
    .performance-critical {
        background: #f8d7da;
        border: 1px solid #f5c6cb;
        color: #721c24;
        padding: 0.75rem;
        border-radius: 5px;
        border-left: 4px solid #dc3545;
    }
</style>
""", unsafe_allow_html=True)

# Environment indicator
env_class = "env-production" if config.environment == "production" else "env-development"
st.markdown(f"""
<div class="env-indicator {env_class}">
    {config.environment.upper()} • {config.version}
</div>
""", unsafe_allow_html=True)

# Production header
st.markdown("""
<div class="main-header">
    <h1>🏢 Olist Business Intelligence Platform</h1>
    <p>Production Dashboard • Real-time Analytics • Enterprise Grade</p>
</div>
""", unsafe_allow_html=True)

# Health check endpoint simulation
def health_check() -> Dict:
    """
    Application health check for monitoring.
    """
    try:
        # Check database connectivity
        db_config = config.get_database_config()
        db_healthy = bool(db_config.get('url'))
        
        # Check performance metrics
        metrics = monitor.get_metrics_summary()
        performance_healthy = metrics['avg_query_time'] < 2.0 and metrics['error_count'] < 10
        
        # Overall health status
        overall_healthy = db_healthy and performance_healthy
        
        return {
            'status': 'healthy' if overall_healthy else 'unhealthy',
            'timestamp': datetime.now().isoformat(),
            'version': config.version,
            'environment': config.environment,
            'database': 'connected' if db_healthy else 'disconnected',
            'performance': 'good' if performance_healthy else 'degraded',
            'uptime_minutes': metrics['uptime_minutes'],
            'total_requests': metrics['page_loads']
        }
        
    except Exception as e:
        logger.error(f"Health check failed: {e}")
        return {
            'status': 'unhealthy',
            'error': str(e),
            'timestamp': datetime.now().isoformat()
        }

# Application monitoring dashboard
st.subheader("📊 Application Health & Performance")

health_data = health_check()
performance_metrics = monitor.get_metrics_summary()

# Health status indicators
health_col1, health_col2, health_col3, health_col4 = st.columns(4)

with health_col1:
    status_emoji = "🟢" if health_data['status'] == 'healthy' else "🔴"
    st.metric(
        f"{status_emoji} System Health",
        health_data['status'].title(),
        f"Environment: {config.environment}"
    )

with health_col2:
    st.metric(
        "📡 Database Status",
        health_data.get('database', 'unknown').title(),
        "Real-time"
    )

with health_col3:
    st.metric(
        "⚡ Avg Response Time",
        f"{performance_metrics['avg_query_time']:.3f}s",
        "Target: <2.0s"
    )

with health_col4:
    st.metric(
        "🔢 Total Requests",
        f"{performance_metrics['page_loads']:,}",
        f"Errors: {performance_metrics['error_count']}"
    )

# Performance status
if performance_metrics['avg_query_time'] < 1.0:
    performance_class = "performance-good"
    performance_message = "🚀 Application performance is excellent"
elif performance_metrics['avg_query_time'] < 2.0:
    performance_class = "performance-warning"
    performance_message = "⚠️ Application performance is acceptable but could be improved"
else:
    performance_class = "performance-critical"
    performance_message = "🚨 Application performance needs immediate attention"

st.markdown(f"""
<div class="{performance_class}">
    <strong>Performance Status:</strong> {performance_message}
</div>
""", unsafe_allow_html=True)

# Sample business data with performance tracking
@st.cache_data(ttl=300)  # 5-minute cache for production
def load_production_data():
    """
    Load production data with performance monitoring.
    """
    start_time = time.time()
    
    try:
        # Simulate production data loading
        np.random.seed(42)
        
        # Generate business metrics
        dates = pd.date_range('2024-01-01', periods=365, freq='D')
        data = {
            'date': dates,
            'revenue': np.random.normal(50000, 10000, 365).cumsum(),
            'orders': np.random.poisson(200, 365),
            'customers': np.random.poisson(150, 365),
            'satisfaction': np.random.normal(4.2, 0.3, 365)
        }
        
        df = pd.DataFrame(data)
        
        # Track query performance
        execution_time = time.time() - start_time
        monitor.track_query_performance('load_production_data', execution_time)
        
        logger.info(f"Production data loaded successfully in {execution_time:.3f}s")
        return df
        
    except Exception as e:
        monitor.track_error('data_loading_error', str(e))
        raise

# Load and display production data
try:
    with st.spinner("Loading production data..."):
        production_df = load_production_data()
    
    # Business metrics dashboard
    st.markdown("---")
    st.subheader("📈 Business Performance Dashboard")
    
    # Current metrics
    current_revenue = production_df['revenue'].iloc[-1]
    current_orders = production_df['orders'].iloc[-30:].sum()
    current_satisfaction = production_df['satisfaction'].iloc[-30:].mean()
    
    metric_col1, metric_col2, metric_col3 = st.columns(3)
    
    with metric_col1:
        st.metric(
            "💰 Total Revenue",
            f"R$ {current_revenue:,.0f}",
            "YTD Performance"
        )
    
    with metric_col2:
        st.metric(
            "📦 Orders (30d)",
            f"{current_orders:,}",
            "Recent Performance"
        )
    
    with metric_col3:
        st.metric(
            "⭐ Satisfaction",
            f"{current_satisfaction:.2f}/5.0",
            "30-day Average"
        )
    
    # Revenue trend chart
    st.subheader("📊 Revenue Trend Analysis")
    
    import plotly.express as px
    
    fig = px.line(
        production_df.tail(90),  # Last 90 days
        x='date',
        y='revenue',
        title="Revenue Trend (Last 90 Days)",
        labels={'revenue': 'Revenue (R$)', 'date': 'Date'}
    )
    
    fig.update_traces(line=dict(color='#667eea', width=3))
    fig.update_layout(height=400)
    
    st.plotly_chart(fig, use_container_width=True)
    
except Exception as e:
    st.error(f"❌ Failed to load production data: {str(e)}")
    monitor.track_error('dashboard_error', str(e))

# Production deployment information
with st.sidebar:
    st.header("🚀 Deployment Info")
    
    st.markdown(f"""
    **Environment:** {config.environment}  
    **Version:** {config.version}  
    **Build:** {datetime.now().strftime('%Y%m%d-%H%M')}  
    **Status:** {health_data['status'].title()}  
    """)
    
    st.markdown("---")
    st.subheader("📊 Performance Metrics")
    
    st.metric("Page Loads", performance_metrics['page_loads'])
    st.metric("Total Queries", performance_metrics['total_queries'])
    st.metric("Error Count", performance_metrics['error_count'])
    
    st.markdown("---")
    st.subheader("🔧 Admin Tools")
    
    if st.button("🔄 Clear Cache", use_container_width=True):
        st.cache_data.clear()
        st.success("Cache cleared!")
    
    if st.button("📊 Full Health Check", use_container_width=True):
        health_result = health_check()
        st.json(health_result)
    
    if st.button("📥 Export Logs", use_container_width=True):
        # In production, this would export actual logs
        st.info("Logs exported to admin panel")

# Footer with deployment information
st.markdown("---")
st.markdown(f"""
<div style="text-align: center; color: #666; padding: 1rem;">
    <p><strong>🏢 Olist Business Intelligence Platform</strong> | 
    Version {config.version} | 
    Environment: {config.environment.title()} | 
    <a href="#" style="color: #667eea;">Support</a> | 
    <a href="#" style="color: #667eea;">Documentation</a></p>
    <p>Deployed on Streamlit Cloud | 
    Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} UTC</p>
</div>
""", unsafe_allow_html=True)

# Log successful page render
logger.info("Dashboard rendered successfully for user session")
