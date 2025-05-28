# Minor Assignment: Data Reshaping - Merge, Pivot, and Time Series Basics

**Due Date:** Thursday, May 1, 2025 (before class)  
**Submission Format:** Google Colab notebook (.ipynb)  
**Total Points:** 100  

## Learning Objectives
By completing this assignment, you will:
1. Master data combination techniques using merge, join, and concatenate operations
2. Transform data between wide and long formats using melt and pivot operations
3. Apply basic time series manipulation techniques for temporal data analysis
4. Translate complex SQL queries to equivalent Pandas operations
5. Analyze real e-commerce data using data reshaping techniques

## Instructions
Complete all tasks in a single Google Colab notebook. Include descriptive markdown text between code cells to explain your approach and findings.

## Dataset
Use the provided e-commerce datasets in the `Data` folder:
- `orders.csv` - Order transaction data
- `customers.csv` - Customer information
- `products.csv` - Product catalog
- `order_items.csv` - Order line items
- `customer_activity.csv` - Daily customer activity metrics
- `monthly_sales.csv` - Monthly sales data in wide format
- `daily_orders.csv` - Daily order data for time series analysis

Load these datasets at the beginning of your notebook using pandas.

## Tasks

### Part 1: Data Combination with Merge and Join Operations (25 points)

1. **Basic Merging (8 points)**
   - Load the `orders.csv` and `customers.csv` datasets
   - Perform an inner join to combine orders with customer information
   - Perform a left join to keep all orders even if customer information is missing
   - Compare the results and explain the difference in row counts

2. **Multi-table Joins (10 points)**
   - Create a comprehensive dataset by joining `orders`, `customers`, `order_items`, and `products`
   - Calculate the total revenue for each customer
   - Find the top 5 customers by total spending
   - Identify which product category generates the most revenue

3. **Handling Join Issues (7 points)**
   - Identify any orders that don't have corresponding customer records
   - Find products that have never been ordered
   - Handle duplicate column names appropriately using suffixes
   - Create a summary report showing data quality issues found

### Part 2: Data Reshaping with Melt and Pivot Operations (25 points)

1. **Wide to Long Format (10 points)**
   - Load the `monthly_sales.csv` dataset (wide format with months as columns)
   - Use `pd.melt()` to convert it to long format
   - Clean the month column to proper datetime format
   - Calculate month-over-month growth rates

2. **Long to Wide Format (10 points)**
   - Using the `customer_activity.csv` dataset, create a pivot table showing:
     - Rows: Date
     - Columns: Activity type (page_views, orders, new_customers)
     - Values: Count/amount
   - Fill missing values with 0
   - Calculate weekly averages for each activity type

3. **Advanced Pivot Tables (5 points)**
   - Create a pivot table showing average order value by:
     - Rows: Customer city
     - Columns: Product category
     - Values: Average order amount
   - Use multiple aggregation functions (mean, count, sum)
   - Identify which city-category combinations perform best

### Part 3: Time Series Manipulation (25 points)

1. **DateTime Parsing and Indexing (8 points)**
   - Load the `daily_orders.csv` dataset
   - Convert the date column to proper datetime format
   - Set the date as the DataFrame index
   - Extract date components (year, month, day, weekday)
   - Identify weekends vs weekdays in the data

2. **Time-based Filtering and Analysis (10 points)**
   - Filter data for the last 30 days
   - Calculate 7-day moving averages for order counts and revenue
   - Identify the best and worst performing days
   - Compare weekend vs weekday performance

3. **Resampling and Aggregation (7 points)**
   - Resample daily data to weekly totals
   - Resample to monthly averages
   - Create business day summaries (Monday-Friday only)
   - Calculate quarter-over-quarter growth if multiple quarters exist

### Part 4: SQL to Pandas Translation (25 points)

Translate the following SQL queries to Pandas code and execute them on your datasets:

1. **Complex Join with Aggregation (8 points)**
   ```sql
   SELECT 
       c.city,
       p.category,
       COUNT(DISTINCT o.order_id) as order_count,
       SUM(oi.quantity * oi.unit_price) as total_revenue,
       AVG(oi.quantity * oi.unit_price) as avg_order_value
   FROM customers c
   JOIN orders o ON c.customer_id = o.customer_id
   JOIN order_items oi ON o.order_id = oi.order_id
   JOIN products p ON oi.product_id = p.product_id
   GROUP BY c.city, p.category
   HAVING COUNT(DISTINCT o.order_id) > 5
   ORDER BY total_revenue DESC;
   ```

2. **Time-based Analysis (8 points)**
   ```sql
   SELECT 
       EXTRACT(YEAR FROM order_date) as year,
       EXTRACT(MONTH FROM order_date) as month,
       COUNT(*) as total_orders,
       COUNT(DISTINCT customer_id) as unique_customers,
       SUM(total_amount) as monthly_revenue,
       AVG(total_amount) as avg_order_value,
       SUM(total_amount) - LAG(SUM(total_amount)) OVER (ORDER BY EXTRACT(YEAR FROM order_date), EXTRACT(MONTH FROM order_date)) as revenue_change
   FROM orders
   GROUP BY EXTRACT(YEAR FROM order_date), EXTRACT(MONTH FROM order_date)
   ORDER BY year, month;
   ```

3. **Customer Segmentation (9 points)**
   ```sql
   WITH customer_metrics AS (
       SELECT 
           customer_id,
           COUNT(DISTINCT order_id) as order_count,
           SUM(total_amount) as total_spent,
           AVG(total_amount) as avg_order_value,
           MAX(order_date) as last_order_date,
           MIN(order_date) as first_order_date
       FROM orders
       GROUP BY customer_id
   )
   SELECT 
       CASE 
           WHEN order_count = 1 THEN 'One-time'
           WHEN order_count BETWEEN 2 AND 5 THEN 'Regular'
           ELSE 'Frequent'
       END as customer_segment,
       CASE
           WHEN total_spent < 100 THEN 'Low Value'
           WHEN total_spent BETWEEN 100 AND 500 THEN 'Medium Value'
           ELSE 'High Value'
       END as value_segment,
       COUNT(*) as customer_count,
       AVG(total_spent) as avg_total_spent,
       AVG(avg_order_value) as avg_order_value
   FROM customer_metrics
   GROUP BY customer_segment, value_segment
   ORDER BY customer_segment, value_segment;
   ```

## Bonus Challenge (5 extra points)
Create a comprehensive customer dashboard that combines all the techniques learned:
1. Merge customer data with their order history
2. Calculate RFM metrics (Recency, Frequency, Monetary value)
3. Create a pivot table showing customer segments
4. Analyze temporal patterns in customer behavior
5. Present your findings with clear visualizations

## Submission Guidelines
1. Ensure your notebook runs without errors from start to finish
2. Include clear markdown explanations for each section
3. Comment your code appropriately, especially for complex operations
4. Name your notebook: `Week4_Minor_Assignment_DataReshaping_YourName.ipynb`
5. Submit via the course portal before the deadline
6. Include a brief summary (200-300 words) of key insights discovered

## Grading Criteria
- **Technical Correctness (50%)**: Code produces accurate results and follows best practices
- **SQL Translation Accuracy (20%)**: Pandas code correctly replicates SQL query logic
- **Code Quality (15%)**: Well-organized, readable, and properly commented code
- **Analysis Quality (10%)**: Meaningful insights and appropriate interpretations
- **Documentation (5%)**: Clear explanations and professional presentation

## Tips for Success
1. **Plan your joins carefully**: Always check the shape of your DataFrames before and after merging
2. **Handle missing data**: Decide on appropriate strategies for NaN values in your analysis
3. **Validate your results**: Cross-check your Pandas output with expected SQL results
4. **Use appropriate data types**: Ensure dates are datetime objects and categorical data is properly typed
5. **Memory management**: For large datasets, consider using chunking or efficient data types

## Academic Integrity
Your submitted work must be your own. You may refer to course materials, documentation, and the lecture notebooks, but do not copy solutions from external sources or other students. Collaboration is not permitted for this individual assignment.

## Getting Help
- Review the lecture materials and practice exercises
- Attend office hours for clarification on concepts
- Post questions in the course forum (without sharing code solutions)
- Email the instructor for urgent technical issues

**Good luck with your data reshaping journey!**