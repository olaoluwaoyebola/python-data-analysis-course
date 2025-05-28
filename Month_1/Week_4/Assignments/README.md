# Week 4 Assignments - Data Transformation

This folder contains assignments for Week 4 of the Python for Data Analysis course, focusing on data reshaping techniques.

## Assignment Structure

### Minor Assignment (Wednesday)
**File:** `Minor_Assignment_Data_Reshaping_[WED].md`  
**Due:** Thursday, May 1, 2025 (before class)  
**Focus:** Individual practice with merge, join, melt, pivot, and time series operations  
**Points:** 100 total

## Datasets

The following datasets are provided in the `../Data/` folder for use in assignments:

### Core E-commerce Tables
- **`customers.csv`** - Customer demographic and contact information (20 customers)
- **`orders.csv`** - Order transaction data with dates, amounts, and status (52 orders)
- **`products.csv`** - Product catalog with categories, prices, and inventory (25 products)
- **`order_items.csv`** - Line items linking orders to products with quantities and prices

### Analysis-Specific Datasets
- **`customer_activity.csv`** - Daily customer activity metrics in long format (page views, orders, new customers, returning customers)
- **`monthly_sales.csv`** - Monthly product sales data in wide format (perfect for melt operations)
- **`daily_orders.csv`** - Daily aggregated order metrics for time series analysis

## Data Relationships

The datasets are interconnected through foreign keys:
- `customers.customer_id` ↔ `orders.customer_id`
- `orders.order_id` ↔ `order_items.order_id`
- `products.product_id` ↔ `order_items.product_id`

## Data Quality Notes

The datasets include realistic data quality issues for students to discover and handle:
- Missing customer records (orders with `CUST999` and `CUST888`)
- Product with zero sales (`PROD021` - Gaming Chair RGB)
- Varying date formats and missing values
- Duplicate scenarios requiring aggregation

## Assignment Topics Covered

### Part 1: Data Combination (25 points)
- Inner, left, right, and outer joins
- Multi-table joins with 4+ tables
- Handling missing relationships and duplicate column names

### Part 2: Data Reshaping (25 points)
- Wide to long format conversion with `pd.melt()`
- Long to wide format conversion with `pd.pivot()` and `pd.pivot_table()`
- Advanced pivot tables with multiple aggregations

### Part 3: Time Series Manipulation (25 points)
- DateTime parsing and indexing
- Time-based filtering and analysis
- Resampling and moving averages

### Part 4: SQL Translation (25 points)
- Complex joins with aggregation
- Time-based analysis with LAG functions
- Customer segmentation with CASE statements

## Learning Outcomes

After completing this assignment, students will be able to:
1. Combine multiple datasets using various join strategies
2. Transform data between wide and long formats as needed for analysis
3. Handle datetime data and perform basic time series operations
4. Translate complex SQL queries to equivalent Pandas operations
5. Apply data transformation techniques to solve real business problems

## Getting Started

1. **Load the datasets** at the beginning of your notebook:
   ```python
   import pandas as pd
   
   # Load all datasets
   customers = pd.read_csv('Data/customers.csv')
   orders = pd.read_csv('Data/orders.csv')
   products = pd.read_csv('Data/products.csv')
   order_items = pd.read_csv('Data/order_items.csv')
   customer_activity = pd.read_csv('Data/customer_activity.csv')
   monthly_sales = pd.read_csv('Data/monthly_sales.csv')
   daily_orders = pd.read_csv('Data/daily_orders.csv')
   ```

2. **Parse dates** where appropriate:
   ```python
   orders['order_date'] = pd.to_datetime(orders['order_date'])
   daily_orders['date'] = pd.to_datetime(daily_orders['date'])
   customer_activity['date'] = pd.to_datetime(customer_activity['date'])
   ```

3. **Follow the assignment structure** and complete all parts systematically

## Tips for Success

- **Always check DataFrame shapes** before and after joins to understand the impact
- **Handle missing values** appropriately for your analysis context
- **Verify your results** by cross-checking totals and counts
- **Use descriptive variable names** and comment your complex operations
- **Test your SQL translations** by comparing results between methods

## Submission Guidelines

- Name your notebook: `Week4_Minor_Assignment_DataReshaping_YourName.ipynb`
- Ensure all cells run without errors
- Include markdown explanations for each section
- Submit via the course portal before the deadline

## Major Group Assignment (Thursday)

The major group assignment will build on these individual skills by applying data transformation techniques to the complete Olist Brazilian E-commerce dataset, preparing students for real-world multi-table analysis scenarios.