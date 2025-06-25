# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is a 5-month Python data analysis course repository designed for Google Colab. The course bridges SQL knowledge to Python for data analysis, using real e-commerce data from Olist Brazilian marketplace.

## Architecture

### Course Structure
- **Month 1**: Python foundations, NumPy, Pandas, data transformation
- **Month 2**: Visualization (Matplotlib/Seaborn), advanced Pandas operations  
- **Month 3**: Statistical analysis, machine learning preparation
- **Months 4-5**: Capstone projects

### File Organization
Each week follows this structure:
```
Month_X/Week_Y/
├── Lecture/          # Multi-part instructor notebooks
├── Practice/         # In-class guided exercises
├── Assignments/      # Student work (Minor: Wed, Major: Thu)
└── Data/            # Week-specific datasets
```

## Key Utilities

### `Utilities/colab_helper.py`
- `load_github_data(path)`: Load CSV files directly from repository
- `setup_colab()`: Standard imports and display settings
- Core function for Google Colab integration

### `Utilities/olist_helper.py`
- Dataset-specific helpers for Olist e-commerce data
- `load_olist_data(table_name)`: Load specific data tables
- `join_order_data()`: Pre-built business logic joins

### `Utilities/visualization_helper.py`
- `set_plotting_style()`: Consistent chart styling
- Standard plotting functions for distributions and time series

## Development Patterns

### Notebook Structure
- **Lecture notebooks**: Split into parts (part1, part2, etc.)
- **Assignment notebooks**: Empty code cells with markdown instructions
- Heavy use of markdown for business context and explanations
- SQL-to-Python translation emphasis throughout

### Standard Imports
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

## Platform Notes

- **Designed for Google Colab only** - no local setup required
- No package management files (requirements.txt, etc.)
- All dependencies provided by Colab environment
- Repository integrates directly with Colab via GitHub

## Project Types

Capstone projects fall into 5 categories:
- Customer Satisfaction Analysis
- Seller Performance Optimization
- Supply Chain and Logistics Analysis  
- Marketing Channel Effectiveness
- Product Category Performance

Each requires real business insights from Olist e-commerce dataset.

## Content and Curriculum Development Guidelines

### Python for Data Analysis Course

#### Repository
- GitHub Repository: "autom8or-com/python-data-analysis-course"
- Access via GitHub MCP Server when asked

#### Development Workflow
- Always create a branch (`month_week_day`) unless otherwise stated
- Do not edit on the main branch
- Teaching Platform: Google Colab

#### Content Creation Process
1. For new weeks, infer structure from previous week
2. Reference "Python for Data Analysis - 5-Month Curriculum.md"
3. Break down content by sub-topics (e.g., 3 sub-topics per day)

#### Weekly Folder Structure
```
Week_X/
├── Lecture/    # Lecture content
├── Assignment/ # Week's assignments
└── Data/      # Datasets for lecture and assignment
```

#### Lecture File Naming
- Wednesday: `01_<topic>_part<Number>_<subTopic>.ext`
- Thursday: `02_<topic>_part<Number>_<subTopic>.ext`

#### Data Resources
- Brazilian E-Commerce Dataset: https://github.com/autom8or-com/python-data-analysis-course/blob/main/Resources/data/sales.zip
- Marketing Funnel Dataset: https://github.com/autom8or-com/python-data-analysis-course/blob/main/Resources/data/marketing_funnel.zip

#### Additional Notes
- Students have intermediate SQL knowledge
- When unsure, check `ReadMe.md` in working or parent directory

## Database Configuration

### Supabase Database Access
- Use the Supabase MCP server to access project databases
- Key schemas:
  - "olist_sales_data_set": Primary sales dataset
  - "olist_marketing_data_set": Marketing-related data

## Security Best Practices

- NEVER INCLUDE DATABASE CREDENTIALS IN AN TUTORIAL FILE. SAVE IN .ENV FILES. AND CALL IN OTHER FILES WHERE NEEDED.