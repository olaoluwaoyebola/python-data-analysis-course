# Olist Dataset Helper Functions
# This file contains helper functions for working with the Olist dataset

def load_olist_data(table_name):
    """
    Load a specific Olist dataset table
    
    Parameters:
    -----------
    table_name : str
        Name of the table to load (e.g., 'customers', 'orders')
    
    Returns:
    --------
    pandas.DataFrame
        Loaded data table
    """
    import pandas as pd
    from google.colab import files
    import io
    
    # Map of table names to file names
    table_map = {
        'customers': 'olist_customers_dataset.csv',
        'orders': 'olist_orders_dataset.csv',
        'order_items': 'olist_order_items_dataset.csv',
        'products': 'olist_products_dataset.csv',
        'sellers': 'olist_sellers_dataset.csv',
        'order_payments': 'olist_order_payments_dataset.csv',
        'order_reviews': 'olist_order_reviews_dataset.csv',
        'categories': 'product_category_name_translation.csv'
    }
    
    # Check if table name is valid
    if table_name not in table_map:
        raise ValueError(f"Invalid table name. Valid options are: {list(table_map.keys())}")
    
    filename = table_map[table_name]
    
    try:
        # First try to load from the Data folder
        return pd.read_csv(f'Data/{filename}')
    except FileNotFoundError:
        # If not available, prompt the user to upload the file
        print(f"Please upload the {filename} file")
        uploaded = files.upload()
        
        # Read the uploaded file
        return pd.read_csv(io.BytesIO(uploaded[filename]))

def join_order_data():
    """
    Join the main order-related tables (orders, customers, order_items)
    and return a comprehensive order dataset
    
    Returns:
    --------
    pandas.DataFrame
        Joined order data
    """
    # Load required tables
    orders = load_olist_data('orders')
    customers = load_olist_data('customers')
    order_items = load_olist_data('order_items')
    
    # Join the tables
    orders_with_customers = orders.merge(customers, on='customer_id', how='left')
    complete_orders = orders_with_customers.merge(order_items, on='order_id', how='left')
    
    return complete_orders

def calculate_delivery_time(orders_df):
    """
    Calculate delivery time metrics for orders
    
    Parameters:
    -----------
    orders_df : pandas.DataFrame
        DataFrame containing the orders data
    
    Returns:
    --------
    pandas.DataFrame
        Orders DataFrame with added delivery time columns
    """
    import pandas as pd
    
    # Create a copy to avoid modifying the original
    df = orders_df.copy()
    
    # Convert date columns to datetime
    date_columns = [
        'order_purchase_timestamp',
        'order_approved_at',
        'order_delivered_carrier_date',
        'order_delivered_customer_date',
        'order_estimated_delivery_date'
    ]
    
    for col in date_columns:
        if col in df.columns:
            df[col] = pd.to_datetime(df[col])
    
    # Calculate delivery times
    if 'order_purchase_timestamp' in df.columns and 'order_delivered_customer_date' in df.columns:
        df['delivery_time_days'] = (df['order_delivered_customer_date'] - 
                                  df['order_purchase_timestamp']).dt.total_seconds() / (60*60*24)
    
    if 'order_delivered_customer_date' in df.columns and 'order_estimated_delivery_date' in df.columns:
        df['delivery_vs_estimate_days'] = (df['order_delivered_customer_date'] - 
                                        df['order_estimated_delivery_date']).dt.total_seconds() / (60*60*24)
        
        # Add a flag for late deliveries
        df['is_late_delivery'] = df['delivery_vs_estimate_days'] > 0
    
    return df