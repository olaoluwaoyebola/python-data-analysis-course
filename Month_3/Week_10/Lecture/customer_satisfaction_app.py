import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import sys
sys.path.append('/home/odunayo12/python-data-analysis-course')
from Utilities.olist_helper import load_olist_data

# App configuration
st.set_page_config(
    page_title="Customer Satisfaction Analysis",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 1. DATA LOADING (Converted from notebook)
@st.cache_data
def load_and_prepare_data():
    """Load and prepare data for analysis - converted from notebook cells"""
    
    with st.spinner("Loading Olist data..."):
        # Load core datasets
        orders = load_olist_data('olist_orders_dataset')
        reviews = load_olist_data('olist_order_reviews_dataset')
        customers = load_olist_data('olist_customers_dataset')
        
        # Merge datasets (cleaned up from notebook)
        merged_data = orders.merge(reviews, on='order_id', how='inner')
        merged_data = merged_data.merge(customers, on='customer_id', how='left')
        
        # Data preparation (extracted from notebook)
        merged_data['order_purchase_timestamp'] = pd.to_datetime(merged_data['order_purchase_timestamp'])
        merged_data['order_delivered_customer_date'] = pd.to_datetime(merged_data['order_delivered_customer_date'])
        merged_data['order_estimated_delivery_date'] = pd.to_datetime(merged_data['order_estimated_delivery_date'])
        
        # Business logic (from notebook)
        merged_data['actual_delivery_days'] = (merged_data['order_delivered_customer_date'] - 
                                              merged_data['order_purchase_timestamp']).dt.days
        merged_data['estimated_delivery_days'] = (merged_data['order_estimated_delivery_date'] - 
                                                 merged_data['order_purchase_timestamp']).dt.days
        merged_data['delivery_delay'] = merged_data['actual_delivery_days'] - merged_data['estimated_delivery_days']
        merged_data['is_late'] = merged_data['delivery_delay'] > 0
        
        # Clean data (improved from notebook)
        clean_data = merged_data.dropna(subset=['review_score', 'actual_delivery_days'])
        clean_data = clean_data[clean_data['actual_delivery_days'] >= 0]  # Remove invalid dates
        clean_data = clean_data[clean_data['actual_delivery_days'] <= 100]  # Remove outliers
        
    return clean_data

# 2. USER CONTROLS (New - not in notebook)
def create_user_controls(data):
    """Create interactive controls for user filtering"""
    
    st.sidebar.header("Analysis Filters")
    
    # Date range filter
    min_date = data['order_purchase_timestamp'].min().date()
    max_date = data['order_purchase_timestamp'].max().date()
    
    date_range = st.sidebar.date_input(
        "Order Date Range",
        value=(min_date, max_date),
        min_value=min_date,
        max_value=max_date
    )
    
    # State filter
    states = sorted(data['customer_state'].dropna().unique())
    selected_states = st.sidebar.multiselect(
        "Customer States",
        options=states,
        default=states[:5]  # Default to first 5 states
    )
    
    # Review score filter
    min_score, max_score = st.sidebar.slider(
        "Review Score Range",
        min_value=1,
        max_value=5,
        value=(1, 5)
    )
    
    return {
        'date_range': date_range,
        'states': selected_states,
        'score_range': (min_score, max_score)
    }

# 3. BUSINESS LOGIC (Extracted from notebook)
def perform_analysis(data, filters):
    """Perform analysis with user filters applied"""
    
    # Apply filters
    filtered_data = data.copy()
    
    # Date filter
    if len(filters['date_range']) == 2:
        start_date, end_date = filters['date_range']
        filtered_data = filtered_data[
            (filtered_data['order_purchase_timestamp'].dt.date >= start_date) &
            (filtered_data['order_purchase_timestamp'].dt.date <= end_date)
        ]
    
    # State filter
    if filters['states']:
        filtered_data = filtered_data[filtered_data['customer_state'].isin(filters['states'])]
    
    # Score filter
    min_score, max_score = filters['score_range']
    filtered_data = filtered_data[
        (filtered_data['review_score'] >= min_score) &
        (filtered_data['review_score'] <= max_score)
    ]
    
    # Calculate key metrics (from notebook)
    total_orders = len(filtered_data)
    avg_satisfaction = filtered_data['review_score'].mean()
    late_delivery_rate = filtered_data['is_late'].mean()
    avg_delivery_time = filtered_data['actual_delivery_days'].mean()
    
    # Satisfaction by delivery performance (from notebook)
    satisfaction_by_performance = filtered_data.groupby('is_late')['review_score'].agg([
        'mean', 'count', 'std'
    ]).round(3)
    
    # Correlation analysis (from notebook)
    delivery_satisfaction_corr = filtered_data['actual_delivery_days'].corr(filtered_data['review_score'])
    
    return {
        'data': filtered_data,
        'metrics': {
            'total_orders': total_orders,
            'avg_satisfaction': avg_satisfaction,
            'late_delivery_rate': late_delivery_rate,
            'avg_delivery_time': avg_delivery_time,
            'correlation': delivery_satisfaction_corr
        },
        'satisfaction_by_performance': satisfaction_by_performance
    }

# 4. PRESENTATION (Converted from notebook visualizations)
def display_results(results):
    """Display analysis results with interactive visualizations"""
    
    data = results['data']
    metrics = results['metrics']
    
    # Header
    st.title("Customer Satisfaction Analysis")
    st.markdown("### Understanding the relationship between delivery performance and customer satisfaction")
    
    # Key metrics (improved from notebook print statements)
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Total Orders", f"{metrics['total_orders']:,}")
    with col2:
        st.metric("Average Satisfaction", f"{metrics['avg_satisfaction']:.2f}/5")
    with col3:
        st.metric("Late Delivery Rate", f"{metrics['late_delivery_rate']:.1%}")
    with col4:
        st.metric("Average Delivery Time", f"{metrics['avg_delivery_time']:.1f} days")
    
    # Visualizations (converted from matplotlib to plotly)
    col1, col2 = st.columns(2)
    
    with col1:
        # Review score distribution (converted from histogram)
        fig_hist = px.histogram(
            data, 
            x='review_score', 
            title='Review Score Distribution',
            nbins=5
        )
        st.plotly_chart(fig_hist, use_container_width=True)
    
    with col2:
        # Satisfaction by delivery performance (converted from bar chart)
        perf_data = results['satisfaction_by_performance'].reset_index()
        perf_data['delivery_status'] = perf_data['is_late'].map({False: 'On Time', True: 'Late'})
        
        fig_bar = px.bar(
            perf_data,
            x='delivery_status',
            y='mean',
            title='Average Review Score by Delivery Performance',
            labels={'mean': 'Average Review Score'}
        )
        st.plotly_chart(fig_bar, use_container_width=True)
    
    # Delivery time analysis
    col1, col2 = st.columns(2)
    
    with col1:
        # Delivery time distribution (converted from histogram)
        fig_delivery = px.histogram(
            data,
            x='actual_delivery_days',
            title='Delivery Time Distribution',
            nbins=30
        )
        st.plotly_chart(fig_delivery, use_container_width=True)
    
    with col2:
        # Correlation scatter (converted from matplotlib scatter)
        fig_scatter = px.scatter(
            data.sample(min(5000, len(data))),  # Sample for performance
            x='actual_delivery_days',
            y='review_score',
            title='Delivery Time vs Review Score',
            opacity=0.6
        )
        st.plotly_chart(fig_scatter, use_container_width=True)
    
    # Key insights (new - not in notebook)
    st.markdown("### Key Insights")
    
    correlation = metrics['correlation']
    if abs(correlation) > 0.3:
        strength = "strong" if abs(correlation) > 0.5 else "moderate"
        direction = "negative" if correlation < 0 else "positive"
        st.info(f"There is a {strength} {direction} correlation ({correlation:.3f}) between delivery time and customer satisfaction.")
    else:
        st.info(f"There is a weak correlation ({correlation:.3f}) between delivery time and customer satisfaction.")
    
    if metrics['late_delivery_rate'] > 0.3:
        st.warning(f"High late delivery rate ({metrics['late_delivery_rate']:.1%}) may be impacting customer satisfaction.")
    
    # Raw data (optional)
    if st.checkbox("Show Raw Data"):
        st.subheader("Filtered Dataset")
        st.dataframe(data)

# 5. MAIN APPLICATION
def main():
    """Main application entry point"""
    
    # Load data
    data = load_and_prepare_data()
    
    # # Create user controls
    # filters = create_user_controls(data)
    
    # # Perform analysis
    # results = perform_analysis(data, filters)
    
    # # Display results
    # display_results(results)

if __name__ == "__main__":
    main()
