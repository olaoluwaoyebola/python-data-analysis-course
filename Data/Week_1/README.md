# Week 1 Dataset

This directory contains the datasets used for Week 1 assignments in the Python for Data Analysis course.

## Files

- **sales_data.csv**: Contains information about 10 products including their IDs, names, categories, prices, and inventory quantities.
- **customers.csv**: Contains information about 10 customers including their IDs, names, email addresses, signup dates, and purchase history.
- **orders.csv**: Contains information about 20 orders including their IDs, customer references, dates, amounts, and current status.
- **order_items.csv**: Contains detailed information about 34 items included in the orders, such as quantities and prices.
- **product_reviews.csv**: Contains 20 product reviews with ratings and comments from customers.

## Usage

These files are designed to be used with the Week 1 assignments, particularly for:
1. Learning basic Python data manipulation
2. Practicing pandas operations
3. Translating SQL queries to Python code

## Data Schema

### sales_data.csv
- `product_id`: Unique identifier for each product
- `product_name`: Name of the product
- `category`: Product category (Electronics, Accessories, Audio, Storage)
- `price`: Product price in USD
- `stock_quantity`: Current inventory quantity

### customers.csv
- `customer_id`: Unique identifier for each customer
- `first_name`: Customer's first name
- `last_name`: Customer's last name
- `email`: Customer's email address
- `signup_date`: Date when the customer signed up
- `total_purchases`: Total number of purchases made by the customer

### orders.csv
- `order_id`: Unique identifier for each order
- `customer_id`: Reference to the customer who placed the order
- `order_date`: Date when the order was placed
- `total_amount`: Total order amount in USD
- `status`: Current status of the order (Delivered, Shipped, Processing)

### order_items.csv
- `order_id`: Reference to the order containing this item
- `product_id`: Reference to the product
- `quantity`: Number of units ordered
- `unit_price`: Price per unit in USD
- `subtotal`: Total price for this line item (quantity × unit_price)

### product_reviews.csv
- `review_id`: Unique identifier for each review
- `product_id`: Reference to the product being reviewed
- `customer_id`: Reference to the customer who wrote the review
- `rating`: Rating given to the product (1-5 scale)
- `review_date`: Date when the review was submitted
- `review_text`: Text content of the review