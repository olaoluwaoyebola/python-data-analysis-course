# SQL to Pandas Translation Guide

This guide provides side-by-side comparisons of common SQL operations and their equivalent Pandas code. Since you already have intermediate SQL knowledge, this guide will help you quickly translate your existing skills to Python.

## Table of Contents
1. [Basic Queries](#basic-queries)
2. [Filtering Data](#filtering-data)
3. [Sorting Data](#sorting-data)
4. [Aggregations](#aggregations)
5. [Joins](#joins)
6. [Grouping](#grouping)
7. [Window Functions](#window-functions)
8. [Subqueries](#subqueries)
9. [Date Operations](#date-operations)

## Basic Queries

### Selecting All Columns

**SQL:**
```sql
SELECT * FROM customers;
```

**Pandas:**
```python
# Assuming df_customers is your DataFrame
df_customers

# Or for explicit selection of all columns
df_customers.loc[:, :]
```

### Selecting Specific Columns

**SQL:**
```sql
SELECT customer_id, name, email FROM customers;
```

**Pandas:**
```python
df_customers[['customer_id', 'name', 'email']]
```

### Limiting Results

**SQL:**
```sql
SELECT * FROM customers LIMIT 5;
```

**Pandas:**
```python
df_customers.head(5)
```

## Filtering Data

### Simple WHERE Clause

**SQL:**
```sql
SELECT * FROM customers WHERE city = 'New York';
```

**Pandas:**
```python
df_customers[df_customers['city'] == 'New York']
```

### Multiple Conditions

**SQL:**
```sql
SELECT * FROM customers 
WHERE city = 'New York' AND age > 30;
```

**Pandas:**
```python
df_customers[(df_customers['city'] == 'New York') & (df_customers['age'] > 30)]
```

### IN Clause

**SQL:**
```sql
SELECT * FROM customers 
WHERE city IN ('New York', 'Los Angeles', 'Chicago');
```

**Pandas:**
```python
df_customers[df_customers['city'].isin(['New York', 'Los Angeles', 'Chicago'])]
```

### LIKE Clause

**SQL:**
```sql
SELECT * FROM customers 
WHERE email LIKE '%gmail.com';
```

**Pandas:**
```python
df_customers[df_customers['email'].str.endswith('gmail.com')]

# Or using contains for a more general LIKE %text%
df_customers[df_customers['email'].str.contains('gmail')]
```

## Sorting Data

### ORDER BY

**SQL:**
```sql
SELECT * FROM customers ORDER BY name ASC;
```

**Pandas:**
```python
df_customers.sort_values('name', ascending=True)
```

### Multiple Sort Columns

**SQL:**
```sql
SELECT * FROM customers 
ORDER BY city ASC, age DESC;
```

**Pandas:**
```python
df_customers.sort_values(['city', 'age'], ascending=[True, False])
```

## Aggregations

### Count

**SQL:**
```sql
SELECT COUNT(*) FROM customers;
```

**Pandas:**
```python
len(df_customers)
# or
df_customers.shape[0]
```

### Basic Aggregations

**SQL:**
```sql
SELECT 
    AVG(age) as avg_age,
    MAX(age) as max_age,
    MIN(age) as min_age,
    SUM(purchases) as total_purchases
FROM customers;
```

**Pandas:**
```python
pd.Series({
    'avg_age': df_customers['age'].mean(),
    'max_age': df_customers['age'].max(),
    'min_age': df_customers['age'].min(),
    'total_purchases': df_customers['purchases'].sum()
})

# Or using agg
df_customers.agg({
    'age': ['mean', 'max', 'min'],
    'purchases': 'sum'
})
```

## Joins

### INNER JOIN

**SQL:**
```sql
SELECT c.customer_id, c.name, o.order_id, o.amount
FROM customers c
INNER JOIN orders o ON c.customer_id = o.customer_id;
```

**Pandas:**
```python
pd.merge(
    df_customers, 
    df_orders, 
    on='customer_id', 
    how='inner'
)[['customer_id', 'name', 'order_id', 'amount']]
```

### LEFT JOIN

**SQL:**
```sql
SELECT c.customer_id, c.name, o.order_id, o.amount
FROM customers c
LEFT JOIN orders o ON c.customer_id = o.customer_id;
```

**Pandas:**
```python
pd.merge(
    df_customers, 
    df_orders, 
    on='customer_id', 
    how='left'
)[['customer_id', 'name', 'order_id', 'amount']]
```

### Different Column Names

**SQL:**
```sql
SELECT c.customer_id, c.name, o.order_id
FROM customers c
INNER JOIN orders o ON c.customer_id = o.cust_id;
```

**Pandas:**
```python
pd.merge(
    df_customers, 
    df_orders, 
    left_on='customer_id', 
    right_on='cust_id', 
    how='inner'
)[['customer_id', 'name', 'order_id']]
```

## Grouping

### GROUP BY

**SQL:**
```sql
SELECT city, COUNT(*) as customer_count
FROM customers
GROUP BY city;
```

**Pandas:**
```python
df_customers.groupby('city').size().reset_index(name='customer_count')

# Alternative
df_customers.groupby('city')['customer_id'].count().reset_index(name='customer_count')
```

### GROUP BY with Multiple Aggregations

**SQL:**
```sql
SELECT 
    city, 
    COUNT(*) as customer_count,
    AVG(age) as avg_age,
    SUM(purchases) as total_purchases
FROM customers
GROUP BY city;
```

**Pandas:**
```python
df_customers.groupby('city').agg(
    customer_count=('customer_id', 'count'),
    avg_age=('age', 'mean'),
    total_purchases=('purchases', 'sum')
).reset_index()
```

### GROUP BY with HAVING

**SQL:**
```sql
SELECT 
    city, 
    COUNT(*) as customer_count
FROM customers
GROUP BY city
HAVING COUNT(*) > 5;
```

**Pandas:**
```python
city_counts = df_customers.groupby('city').size().reset_index(name='customer_count')
city_counts[city_counts['customer_count'] > 5]
```

## Window Functions

### ROW_NUMBER()

**SQL:**
```sql
SELECT 
    customer_id, 
    name,
    purchases,
    ROW_NUMBER() OVER (ORDER BY purchases DESC) as purchase_rank
FROM customers;
```

**Pandas:**
```python
df_result = df_customers.copy()
df_result['purchase_rank'] = df_result['purchases'].rank(method='first', ascending=False)
df_result
```

### PARTITION BY

**SQL:**
```sql
SELECT 
    customer_id, 
    name,
    city,
    purchases,
    ROW_NUMBER() OVER (PARTITION BY city ORDER BY purchases DESC) as city_purchase_rank
FROM customers;
```

**Pandas:**
```python
df_result = df_customers.copy()
df_result['city_purchase_rank'] = df_result.groupby('city')['purchases'].rank(method='first', ascending=False)
df_result
```

## Subqueries

### Subquery in WHERE

**SQL:**
```sql
SELECT customer_id, name
FROM customers
WHERE customer_id IN (
    SELECT customer_id 
    FROM orders 
    WHERE amount > 1000
);
```

**Pandas:**
```python
# Get customer IDs with orders > 1000
high_value_customers = df_orders[df_orders['amount'] > 1000]['customer_id'].unique()

# Filter customers
df_customers[df_customers['customer_id'].isin(high_value_customers)][['customer_id', 'name']]
```

### Subquery in SELECT

**SQL:**
```sql
SELECT 
    c.customer_id, 
    c.name,
    (SELECT COUNT(*) FROM orders o WHERE o.customer_id = c.customer_id) as order_count
FROM customers c;
```

**Pandas:**
```python
# Get order counts per customer
order_counts = df_orders.groupby('customer_id').size().reset_index(name='order_count')

# Merge with customers
pd.merge(df_customers[['customer_id', 'name']], order_counts, on='customer_id', how='left').fillna(0)
```

## Date Operations

### Filtering by Date

**SQL:**
```sql
SELECT * 
FROM orders
WHERE order_date >= '2023-01-01';
```

**Pandas:**
```python
# Ensure date column is datetime type
df_orders['order_date'] = pd.to_datetime(df_orders['order_date'])

# Filter
df_orders[df_orders['order_date'] >= '2023-01-01']
```

### Extracting Date Components

**SQL:**
```sql
SELECT 
    order_id,
    order_date,
    EXTRACT(YEAR FROM order_date) as year,
    EXTRACT(MONTH FROM order_date) as month,
    EXTRACT(DAY FROM order_date) as day
FROM orders;
```

**Pandas:**
```python
df_result = df_orders.copy()
df_result['year'] = df_result['order_date'].dt.year
df_result['month'] = df_result['order_date'].dt.month
df_result['day'] = df_result['order_date'].dt.day
df_result
```

### Grouping by Date Components

**SQL:**
```sql
SELECT 
    EXTRACT(YEAR FROM order_date) as year,
    EXTRACT(MONTH FROM order_date) as month,
    COUNT(*) as order_count,
    SUM(amount) as total_amount
FROM orders
GROUP BY 
    EXTRACT(YEAR FROM order_date),
    EXTRACT(MONTH FROM order_date)
ORDER BY year, month;
```

**Pandas:**
```python
df_orders['year'] = df_orders['order_date'].dt.year
df_orders['month'] = df_orders['order_date'].dt.month

monthly_stats = df_orders.groupby(['year', 'month']).agg({
    'order_id': 'count',
    'amount': 'sum'
}).rename(columns={'order_id': 'order_count', 'amount': 'total_amount'}).reset_index()

monthly_stats.sort_values(['year', 'month'])
```