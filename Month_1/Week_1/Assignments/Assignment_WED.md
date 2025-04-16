# Minor Assignment: Introduction to Python and Google Colab

**Due Date:** Wednesday, April 16, 2025 (before class)  
**Submission Format:** Google Colab notebook (.ipynb)  
**Total Points:** 100  

## Learning Objectives
By completing this assignment, you will:
1. Demonstrate basic Python syntax and data types
2. Practice using Python data structures (lists, dictionaries)
3. Create and use functions for data manipulation
4. Translate SQL queries to equivalent Python code
5. Apply basic control flow techniques

## Instructions
Complete all tasks in a single Google Colab notebook. Include descriptive markdown text between code cells to explain your approach.

## Dataset
Use the provided sales data files (`sales_data.csv`, `customers.csv`, `orders.csv`, `order_items.csv`, `product_reviews.csv`). Load these datasets at the beginning of your notebook.

## Tasks

### Part 1: Basic Python Variables and Operations (20 points)
1. Create variables for:
   - A product name (string)
   - A product price (float)
   - Whether the product is in stock (boolean)
   - The stock quantity (integer)

2. Write expressions that:
   - Calculate the total value of the inventory (price × quantity)
   - Apply a 15% discount to the price
   - Check if the product is in stock AND the price is less than $100
   - Create a formatted string showing product details

### Part 2: Working with Data Structures (25 points)
1. Create a list of at least 5 products with their prices
2. Create a dictionary representing a single product with the following keys:
   - `id`, `name`, `price`, `category`, `in_stock`, `features` (list of features)

3. Using the list of products:
   - Find the most expensive product
   - Calculate the average price
   - Create a new list containing only products under $50

4. Using the product dictionary:
   - Add a new key for `discount_price` that's 10% off the original price
   - Add a new feature to the features list
   - Create a formatted string that describes the product

### Part 3: Functions and Control Flow (25 points)
1. Write a function called `calculate_total_price(price, quantity, tax_rate=0.08)` that:
   - Calculates the subtotal (price × quantity)
   - Adds tax based on the provided rate
   - Returns the final total
   - Test your function with at least 3 different scenarios

2. Write a function called `analyze_sales(products_data)` that:
   - Takes a list of product dictionaries
   - Groups products by category
   - Calculates the average price per category
   - Returns a dictionary with categories as keys and average prices as values
   - Test your function with a sample list of at least 6 products across 3 categories

3. Write a function called `check_inventory(product, threshold=10)` that:
   - Returns "Low stock" if quantity is below the threshold
   - Returns "In stock" if quantity is at or above the threshold
   - Returns "Out of stock" if quantity is 0
   - Test with different product scenarios

### Part 4: SQL to Python Translation (30 points)
Using the provided CSV datasets, translate the following SQL queries to Python code using pandas:

1. Basic Selection and Filtering
   ```sql
   SELECT * FROM products WHERE category = 'Electronics' AND price > 100;
   ```

2. Aggregation and Grouping
   ```sql
   SELECT category, COUNT(*) as product_count, AVG(price) as avg_price 
   FROM products 
   GROUP BY category;
   ```

3. Joining Tables
   ```sql
   SELECT o.order_id, c.first_name, c.last_name, o.order_date, o.total_amount
   FROM orders o
   JOIN customers c ON o.customer_id = c.customer_id
   WHERE o.total_amount > 200
   ORDER BY o.order_date DESC;
   ```

4. Complex Query with Multiple Joins
   ```sql
   SELECT 
       p.product_name,
       COUNT(DISTINCT o.order_id) as order_count,
       SUM(oi.quantity) as total_quantity,
       AVG(oi.unit_price) as avg_price
   FROM products p
   JOIN order_items oi ON p.product_id = oi.product_id
   JOIN orders o ON oi.order_id = o.order_id
   WHERE o.status = 'Delivered'
   GROUP BY p.product_id, p.product_name
   HAVING COUNT(DISTINCT o.order_id) > 1
   ORDER BY total_quantity DESC;
   ```

## Submission Guidelines
1. Make sure your notebook runs without errors
2. Include descriptive markdown cells explaining your approach for each part
3. Comment your code appropriately
4. Name your notebook as: `Week1_Minor_Assignment_<YourGroupName>.ipynb`
5. Submit your notebook via the course portal

## Grading Criteria
- **Correctness (60%)**: Code produces the expected results
- **Code Quality (20%)**: Well-organized, readable, and properly commented
- **Documentation (10%)**: Clear explanations in markdown cells
- **Efficiency (10%)**: Efficient and elegant solutions

## Academic Integrity
Your submitted work must be your own. You may refer to course materials and documentation but do not copy solutions from external sources or other students.

Good luck!