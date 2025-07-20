
import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Configure page
st.set_page_config(
    page_title="Advanced Widget Patterns",
    page_icon="⚡",
    layout="wide"
)

st.title("⚡ Advanced Widget Patterns for Business Apps")
st.markdown("**Professional patterns for complex business requirements**")

# Pattern 1: Conditional Widget Display
st.header("🔀 Pattern 1: Conditional Widget Display")
st.markdown("Show/hide widgets based on user selections - common in role-based dashboards.")

with st.container():
    col1, col2 = st.columns([1, 2])
    
    with col1:
        user_role = st.selectbox(
            "Select Your Role:",
            ['Sales Manager', 'Marketing Analyst', 'Operations Director', 'Finance Controller']
        )
    
    with col2:
        # Show different widgets based on role
        if user_role == 'Sales Manager':
            st.info("🎯 Sales-focused controls active")
            territory = st.selectbox("Sales Territory:", ['North', 'South', 'East', 'West', 'Central'])
            quota_period = st.selectbox("Quota Period:", ['Monthly', 'Quarterly', 'Annual'])
            
        elif user_role == 'Marketing Analyst':
            st.info("📢 Marketing analytics controls active")
            campaign_type = st.multiselect(
                "Campaign Types:", 
                ['Email', 'Social Media', 'Search Ads', 'Display', 'Influencer']
            )
            attribution_window = st.slider("Attribution Window (days):", 1, 30, 7)
            
        elif user_role == 'Operations Director':
            st.info("⚙️ Operations monitoring controls active")
            warehouse = st.selectbox("Warehouse:", ['São Paulo', 'Rio', 'Belo Horizonte', 'Salvador'])
            sla_metric = st.radio("SLA Metric:", ['Delivery Time', 'Order Accuracy', 'Return Rate'])
            
        elif user_role == 'Finance Controller':
            st.info("💰 Financial controls active")
            currency = st.selectbox("Currency:", ['BRL', 'USD', 'EUR'])
            fiscal_period = st.date_input("Fiscal Period Start:", datetime.now().replace(month=1, day=1))

# Pattern 2: Dynamic Widget Updates
st.header("🔄 Pattern 2: Dynamic Widget Updates")
st.markdown("Widget options change based on other selections - cascading dropdowns.")

with st.container():
    col1, col2, col3 = st.columns(3)
    
    # Sample hierarchical data
    location_data = {
        'Brazil': {
            'Southeast': ['São Paulo', 'Rio de Janeiro', 'Minas Gerais', 'Espírito Santo'],
            'South': ['Rio Grande do Sul', 'Santa Catarina', 'Paraná'],
            'Northeast': ['Bahia', 'Pernambuco', 'Ceará', 'Paraíba']
        }
    }
    
    with col1:
        country = st.selectbox("Country:", list(location_data.keys()))
    
    with col2:
        if country:
            regions = list(location_data[country].keys())
            region = st.selectbox("Region:", regions)
        else:
            region = None
    
    with col3:
        if region:
            states = location_data[country][region]
            state = st.selectbox("State:", states)
        else:
            state = None
    
    if state:
        st.success(f"✅ Selected: {state}, {region}, {country}")

# Pattern 3: Form-based Input with Validation
st.header("📝 Pattern 3: Form-based Input with Validation")
st.markdown("Professional form handling with validation - essential for data entry applications.")

with st.form("business_form"):
    st.subheader("Customer Order Form")
    
    form_col1, form_col2 = st.columns(2)
    
    with form_col1:
        customer_name = st.text_input(
            "Customer Name *",
            placeholder="Enter full name",
            help="Required field"
        )
        
        customer_email = st.text_input(
            "Email Address *",
            placeholder="customer@email.com",
            help="Valid email required"
        )
        
        order_value = st.number_input(
            "Order Value (R$) *",
            min_value=0.01,
            max_value=10000.00,
            value=100.00,
            step=0.01,
            help="Minimum R$ 0.01"
        )
    
    with form_col2:
        product_category = st.selectbox(
            "Product Category *",
            ['', 'Electronics', 'Fashion', 'Home & Garden', 'Books', 'Sports']
        )
        
        shipping_method = st.radio(
            "Shipping Method:",
            ['Standard (5-7 days)', 'Express (2-3 days)', 'Premium (1-2 days)']
        )
        
        special_instructions = st.text_area(
            "Special Instructions:",
            placeholder="Any special delivery instructions...",
            height=100
        )
    
    # Form submission with validation
    submitted = st.form_submit_button("📦 Submit Order", type="primary")
    
    if submitted:
        # Validation logic
        errors = []
        
        if not customer_name.strip():
            errors.append("Customer name is required")
        
        if not customer_email.strip() or '@' not in customer_email:
            errors.append("Valid email address is required")
        
        if not product_category:
            errors.append("Product category must be selected")
        
        if order_value <= 0:
            errors.append("Order value must be greater than zero")
        
        # Display results
        if errors:
            st.error("❌ Please fix the following errors:")
            for error in errors:
                st.error(f"• {error}")
        else:
            st.success("✅ Order submitted successfully!")
            st.info(f"Order ID: ORD-{datetime.now().strftime('%Y%m%d%H%M%S')}")
            
            # Display order summary
            with st.expander("📋 Order Summary", expanded=True):
                st.write(f"**Customer:** {customer_name}")
                st.write(f"**Email:** {customer_email}")
                st.write(f"**Category:** {product_category}")
                st.write(f"**Value:** R$ {order_value:.2f}")
                st.write(f"**Shipping:** {shipping_method}")
                if special_instructions:
                    st.write(f"**Instructions:** {special_instructions}")

# Pattern 4: Session State Management
st.header("💾 Pattern 4: Session State Management")
st.markdown("Maintain state across widget interactions - essential for multi-step processes.")

# Initialize session state
if 'counter' not in st.session_state:
    st.session_state.counter = 0
if 'user_data' not in st.session_state:
    st.session_state.user_data = []

with st.container():
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("➕ Increment Counter"):
            st.session_state.counter += 1
    
    with col2:
        if st.button("➖ Decrement Counter"):
            st.session_state.counter -= 1
    
    with col3:
        if st.button("🔄 Reset Counter"):
            st.session_state.counter = 0
    
    st.metric("Current Counter Value", st.session_state.counter)
    
    # Data collection example
    st.markdown("**Add Data Points:**")
    new_value = st.number_input("Enter a value:", value=0.0)
    
    if st.button("📊 Add to Dataset"):
        st.session_state.user_data.append({
            'timestamp': datetime.now(),
            'value': new_value,
            'counter_state': st.session_state.counter
        })
        st.success(f"Added value {new_value} to dataset")
    
    if st.session_state.user_data:
        st.markdown("**Current Dataset:**")
        df_session = pd.DataFrame(st.session_state.user_data)
        st.dataframe(df_session, use_container_width=True)
        
        if st.button("🗑️ Clear Dataset"):
            st.session_state.user_data = []
            st.rerun()

# Footer
st.markdown("---")
st.markdown(
    "**⚡ Advanced Patterns** | "
    "Professional widget patterns for business applications | "
    "**📚 Next:** Data visualization integration"
)
