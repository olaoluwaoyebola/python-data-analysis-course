# Week 2 Datasets

This folder contains datasets for Week 2 exercises and assignments.

## Files

### `numeric_data.csv`
A small dataset for NumPy and Pandas practice exercises with numerical and categorical data.

#### Schema:
- `id`: Unique identifier (integer)
- `value1`: Numeric values (float)
- `value2`: Numeric values (float)
- `value3`: Numeric values (float)
- `category`: Categorical values (string: 'A', 'B', or 'C')

#### Sample Data:
```
id,value1,value2,value3,category
1,5.2,10.5,15.7,A
2,6.8,12.3,18.1,B
3,4.5,9.8,14.3,A
4,7.2,13.5,20.7,C
5,5.9,11.2,17.1,B
```

### `ecommerce_sales.csv`
A synthetic e-commerce dataset for the major group assignment.

#### Schema:
- `order_id`: Unique order identifier
- `customer_id`: Customer identifier
- `order_date`: Date of order placement (YYYY-MM-DD)
- `product_id`: Product identifier
- `product_name`: Name of the product
- `product_category`: Category of the product
- `quantity`: Number of units ordered
- `price`: Unit price
- `payment_method`: Method of payment (Credit Card, PayPal, etc.)
- `shipping_country`: Country of shipping address
- `shipping_region`: Region/state within the country
- `shipping_method`: Shipping method selected
- `shipping_days`: Number of days between order and delivery
- `customer_gender`: Customer's gender
- `customer_age`: Customer's age
- `customer_email_domain`: Domain of customer's email address

#### Sample Data:
```
order_id,customer_id,order_date,product_id,product_name,product_category,quantity,price,payment_method,shipping_country,shipping_region,shipping_method,shipping_days,customer_gender,customer_age,customer_email_domain
ORD-001,CUST-1001,2024-01-15,PROD-101,Premium Laptop,Electronics,1,1299.99,Credit Card,USA,California,Express,2,Male,32,gmail.com
ORD-002,CUST-1002,2024-01-16,PROD-205,Wireless Headphones,Electronics,2,149.99,PayPal,Canada,Ontario,Standard,5,Female,45,yahoo.com
ORD-003,CUST-1003,2024-01-16,PROD-310,Fitness Tracker,Wearables,1,89.95,Credit Card,USA,New York,Express,3,Male,28,outlook.com
```

### `sales_data.csv`
A dataset for Pandas introduction with time series data of product sales.

#### Schema:
- `date`: Date of sale (YYYY-MM-DD)
- `product_id`: Product identifier
- `product_name`: Name of the product
- `category`: Product category
- `subcategory`: Product subcategory
- `quantity`: Number of units sold
- `unit_price`: Price per unit
- `total_sales`: Total sale amount (quantity × unit_price)
- `store_id`: Store identifier
- `store_location`: City of the store

#### Sample Data:
```
date,product_id,product_name,category,subcategory,quantity,unit_price,total_sales,store_id,store_location
2024-01-01,P001,Ergonomic Chair,Furniture,Office,5,159.99,799.95,S01,New York
2024-01-01,P002,Standing Desk,Furniture,Office,2,249.99,499.98,S01,New York
2024-01-01,P003,Wireless Mouse,Electronics,Computer Accessories,10,24.99,249.90,S02,Chicago
```

## Usage

### Loading Data in Python
```python
import pandas as pd

# Load the numeric data
numeric_df = pd.read_csv('numeric_data.csv')

# Load the e-commerce sales data
ecommerce_df = pd.read_csv('ecommerce_sales.csv')

# Load the sales data
sales_df = pd.read_csv('sales_data.csv')

# Convert date columns to datetime
ecommerce_df['order_date'] = pd.to_datetime(ecommerce_df['order_date'])
sales_df['date'] = pd.to_datetime(sales_df['date'])
```

### Data Exploration Examples
```python
# Basic information
print(numeric_df.info())
print(numeric_df.describe())

# Preview data
print(ecommerce_df.head())

# Check for missing values
print(sales_df.isnull().sum())
```

## Notes for Instructors
- The `numeric_data.csv` file contains 10 rows with a mix of numeric values and categories for simple exercises
- The `ecommerce_sales.csv` file contains 1000 rows of synthetic e-commerce data for the group assignment
- The `sales_data.csv` file contains 500 rows of product sales data for Pandas introduction
- All datasets are clean (no missing values) but have intentional patterns and outliers for analysis
- Additional datasets can be provided as needed for specific exercises