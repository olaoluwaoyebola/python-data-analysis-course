# Exercise Datasets

This folder contains small datasets used for in-class exercises and practice assignments. These datasets are simpler than the full Olist database and are designed for focused learning of specific concepts.

## Datasets Included

### retail_sales.csv
A small retail sales dataset with the following columns:
- transaction_id
- date
- customer_id
- product_id
- quantity
- unit_price
- total_amount
- payment_method

### product_catalog.csv
A product catalog with the following columns:
- product_id
- product_name
- category
- subcategory
- base_price
- cost
- supplier_id

### customer_data.csv
Customer information with the following columns:
- customer_id
- join_date
- name
- email
- city
- state
- age_group
- gender

### website_traffic.csv
Website traffic data with the following columns:
- date
- page_url
- visits
- unique_visitors
- bounce_rate
- avg_time_on_page
- source

## Using the Datasets

These datasets can be loaded directly from the GitHub repository using:

```python
import pandas as pd

# Example of loading the retail sales dataset
url = 'https://raw.githubusercontent.com/autom8or-com/python-data-analysis-course/main/Exercise_Datasets/retail_sales.csv'
df_sales = pd.read_csv(url)
```

Or they can be uploaded to Google Colab using:

```python
from google.colab import files
uploaded = files.upload()  # Upload the retail_sales.csv file

import pandas as pd
import io
df_sales = pd.read_csv(io.BytesIO(uploaded['retail_sales.csv']))
```