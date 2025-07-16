# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is a 4-month Python data analysis course repository designed for Google Colab. The course bridges SQL knowledge to Python for data analysis, using real e-commerce data from Olist Brazilian marketplace. The course culminates in a 6-week capstone project delivered as a deployed Streamlit web application.

## Course Architecture

### Current Structure (Updated)
- **Month 1**: Python foundations, NumPy, Pandas, data transformation (Weeks 1-4)
- **Month 2**: Visualization (Matplotlib/Seaborn), SQL integration, EDA, statistical analysis (Weeks 5-8)
- **Month 3**: Streamlit development and project preparation (Weeks 9-10)
- **Month 4**: Capstone project execution (6 weeks)

### Key Changes Made
The course has been restructured from a 5-month to 4-month format:
- Removed advanced ML topics (originally Weeks 11-12)
- Replaced with Streamlit development (Weeks 9-10)
- Shortened capstone from 8 weeks to 6 weeks
- Focus shifted from predictive modeling to descriptive analysis and dashboard creation

### File Organization
Each week follows this structure:
```
Month_X/Week_Y/
├── Lecture/          # Multi-part instructor notebooks
├── Practice/         # In-class guided exercises (may be empty)
├── Assignments/      # Student work (Minor: Wed, Major: Thu)
└── Data/            # Week-specific datasets
```

## Key Utilities

### `Utilities/colab_helper.py`
- `load_github_data(path)`: Load CSV files directly from GitHub repository
- `setup_colab()`: Standard imports and display settings for Colab
- `save_work()`: Remind students to save work to Google Drive

### `Utilities/olist_helper.py`
- `load_olist_data(table_name)`: Load specific Olist data tables with error handling
- `join_order_data()`: Pre-built business logic joins for common analysis patterns
- `calculate_delivery_time(orders_df)`: Calculate delivery metrics and late delivery flags

### `Utilities/visualization_helper.py`
- `set_plotting_style()`: Consistent chart styling across all course materials
- `plot_numeric_distribution()`: Standard distribution plots with summary statistics
- `plot_categorical_distribution()`: Bar plots with customizable sorting and filtering
- `plot_time_series()`: Time series visualization with resampling options

## Development Patterns

### Notebook Structure
- **Lecture notebooks**: Multi-part structure (part1, part2, part3) for complex topics
- **Assignment notebooks**: Empty code cells with detailed markdown instructions
- **Business Context**: Heavy use of markdown for business context and real-world applications
- **SQL Translation**: Consistent emphasis on SQL-to-Python translation throughout

### Standard Imports Pattern
```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
```

### Data Loading Pattern
```python
from Utilities.colab_helper import load_github_data
df = load_github_data('path/to/data.csv')
```

### Visualization Pattern
```python
from Utilities.visualization_helper import set_plotting_style, plot_numeric_distribution
plt, sns = set_plotting_style()
plot_numeric_distribution(df, 'column_name')
```

## Platform Requirements

- **Google Colab Only**: No local development setup required
- **No Package Management**: All dependencies provided by Colab environment
- **GitHub Integration**: Repository integrates directly with Colab via GitHub
- **Streamlit Cloud**: For final project deployment

## Project Structure

### Capstone Project Categories (Non-Predictive Focus)
All projects emphasize descriptive analysis and business insights:
1. **Customer Satisfaction Analysis** - Pattern analysis and satisfaction drivers
2. **Seller Performance Optimization** - Performance metrics and benchmarking
3. **Supply Chain and Logistics Analysis** - Delivery performance and bottleneck identification
4. **Marketing Channel Effectiveness** - Channel performance and ROI analysis
5. **Product Category Performance** - Sales trends and seasonal patterns

### Project Deliverables
- Interactive Streamlit web application (primary deliverable)
- Technical documentation embedded in application
- Live demonstration presentation
- Deployed application accessible via URL

## Database Integration

### Supabase Configuration
- Use Supabase MCP server for database access
- Key schemas:
  - `olist_sales_data_set`: Primary sales dataset
  - `olist_marketing_data_set`: Marketing and funnel data
- Real-time data integration with Streamlit applications

## Content Development Guidelines

### Weekly Development Workflow
1. Always create branches using format: `month_X_week_Y_topic`
2. Never edit directly on main branch
3. Reference existing week structures for consistency
4. Break complex topics into 3-4 sub-topics per session

### File Naming Conventions
- **Wednesday lectures**: `01_<topic>_part<number>_<subtopic>.ipynb`
- **Thursday lectures**: `02_<topic>_part<number>_<subtopic>.ipynb`
- **Assignments**: `<day>_<type>_assignment_<topic>.ipynb`

### Content Focus Areas
- **Statistical Analysis**: Hypothesis testing, comparative analysis, regression (Week 8)
- **Streamlit Development**: Interactive dashboards, deployment, user experience (Weeks 9-10)
- **Business Applications**: Real-world e-commerce problems using Olist dataset
- **SQL Translation**: Continuous emphasis on SQL-to-Python equivalencies

## Security and Environment

### Database Security
- NEVER include database credentials in tutorial files
- Use environment variables for sensitive information
- Store credentials in .env files (excluded from repository)

### Student Prerequisites
- Intermediate SQL knowledge required
- Google account for Colab access
- Basic understanding of statistical concepts (by Week 8)

## Assessment Structure

### Weekly Assignments
- **Minor Assignments**: Wednesday individual work (30% of grade)
- **Major Assignments**: Thursday group projects (30% of grade)
- **Capstone Project**: Final Streamlit application (40% of grade)

### Grading Components
- Technical implementation and code quality
- Business insights and recommendations
- Streamlit application functionality and user experience
- Professional presentation and documentation