# Week 2: Major Group Assignment

## Dataset Exploration with Pandas

### Overview
In this assignment, you will work in groups of 3-4 students to explore and analyze a dataset using NumPy and Pandas. This assignment will allow you to apply the concepts learned in Week 2, particularly focusing on DataFrame creation, column selection, row filtering, and translating SQL queries to Pandas code.

### Objectives
- Load and inspect a dataset using Pandas
- Perform data cleaning and preparation
- Apply selection and filtering operations to analyze the data
- Translate SQL queries to Pandas code
- Visualize key findings
- Document your process and insights

### The Dataset: E-commerce Sales Data
You will be working with a synthetic e-commerce sales dataset containing the following information:
- Customer demographics
- Product details
- Order information (date, quantity, price)
- Payment details
- Shipping information

The dataset is available in the `Data` folder as `ecommerce_sales.csv`.

### Tasks

#### Part 1: Data Loading and Exploration (15%)
1. Load the dataset into a Pandas DataFrame
2. Display the first and last few rows of the DataFrame
3. Get information about the DataFrame structure
4. Generate descriptive statistics for the numeric columns
5. Check for missing values and propose a strategy for handling them

#### Part 2: Data Cleaning and Preparation (20%)
1. Handle missing values according to your proposed strategy
2. Convert data types as needed (e.g., dates to datetime)
3. Create derived columns that may be useful for analysis:
   - Total order value (price × quantity)
   - Customer age group (based on birth year)
   - Order month and year
   - Shipping time (days between order and delivery)
4. Identify and handle any outliers

#### Part 3: Data Analysis with Selection and Filtering (30%)
Perform the following analyses using Pandas selection and filtering operations:

1. Find the top 10 customers by total purchase amount
2. Calculate the average order value by product category
3. Identify the most popular products (by quantity sold)
4. Analyze sales trends by month/year
5. Compare payment methods by frequency and average order value
6. Analyze shipping times by region
7. Calculate the customer retention rate (percentage of customers who made multiple purchases)

#### Part 4: SQL to Pandas Translation (25%)
Translate the following SQL queries to Pandas code and execute them on your dataset:

```sql
-- Query 1: Monthly Sales Analysis
SELECT 
    EXTRACT(YEAR FROM order_date) AS year,
    EXTRACT(MONTH FROM order_date) AS month,
    COUNT(DISTINCT order_id) AS num_orders,
    SUM(price * quantity) AS total_sales,
    AVG(price * quantity) AS avg_order_value
FROM 
    sales
GROUP BY 
    EXTRACT(YEAR FROM order_date),
    EXTRACT(MONTH FROM order_date)
ORDER BY 
    year, month;

-- Query 2: Product Category Performance
SELECT 
    product_category,
    COUNT(DISTINCT order_id) AS num_orders,
    SUM(quantity) AS total_units_sold,
    SUM(price * quantity) AS total_revenue,
    AVG(price) AS avg_unit_price
FROM 
    sales
GROUP BY 
    product_category
ORDER BY 
    total_revenue DESC;

-- Query 3: Customer Segmentation
SELECT 
    CASE 
        WHEN customer_age < 25 THEN 'Under 25'
        WHEN customer_age BETWEEN 25 AND 34 THEN '25-34'
        WHEN customer_age BETWEEN 35 AND 44 THEN '35-44'
        WHEN customer_age BETWEEN 45 AND 54 THEN '45-54'
        ELSE '55 and above'
    END AS age_group,
    customer_gender,
    COUNT(DISTINCT customer_id) AS num_customers,
    COUNT(DISTINCT order_id) AS num_orders,
    SUM(price * quantity) AS total_spent,
    AVG(price * quantity) AS avg_order_value
FROM 
    sales
GROUP BY 
    age_group, customer_gender
ORDER BY 
    age_group, customer_gender;

-- Query 4: Shipping Time Analysis
SELECT 
    CASE 
        WHEN shipping_days <= 2 THEN 'Same/Next Day'
        WHEN shipping_days BETWEEN 3 AND 5 THEN '3-5 Days'
        WHEN shipping_days BETWEEN 6 AND 10 THEN '6-10 Days'
        ELSE 'Over 10 Days'
    END AS shipping_time,
    COUNT(DISTINCT order_id) AS num_orders,
    AVG(price * quantity) AS avg_order_value,
    AVG(shipping_days) AS avg_shipping_days
FROM 
    sales
GROUP BY 
    shipping_time
ORDER BY 
    avg_shipping_days;
```

#### Part 5: Visualization and Reporting (10%)
1. Create at least 3 visualizations to illustrate your key findings
2. Write a brief summary (500-750 words) of your analysis process and insights
3. Include recommendations based on your findings

### Deliverables
1. A Google Colab notebook containing:
   - Well-documented code for all parts of the assignment
   - Output of all analyses
   - Visualizations
   - Narrative explanations
2. A brief presentation slide deck (5-7 slides) summarizing your findings

### Submission Guidelines
- Submit your group's completed Colab notebook and presentation via the course portal
- Due date: Thursday, April 24, 2025, before class
- One submission per group is sufficient, but include all group members' names
- Be prepared to give a 5-minute presentation of your key findings in class

### Evaluation Criteria
- **Technical execution (40%)**: Correct implementation of Pandas operations, code quality
- **Analysis depth (25%)**: Thoroughness of exploration, appropriate techniques
- **Insight quality (20%)**: Meaningful interpretations, business relevance
- **Presentation (15%)**: Clarity, visualization quality, narrative flow

### Note on Collaboration
While this is a group assignment, all group members are expected to contribute actively. Consider dividing responsibilities (e.g., data cleaning, analysis, visualization) but ensure everyone understands all aspects of the submission.