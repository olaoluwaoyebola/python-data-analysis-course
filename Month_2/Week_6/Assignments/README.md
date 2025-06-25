# Week 6 Assignments

This folder contains assignments for Week 6: Advanced Visualization and SQL Integration

## Overview

Week 6 assignments integrate **interactive visualizations** (Wednesday) with **SQL-Python database connections** (Thursday) using real Brazilian e-commerce data from Olist.

## Assignment Structure

### 📊 Minor Assignment (Wednesday): Interactive Visualization Conversion
**File**: `minor_assignment_interactive_visualizations.ipynb`  
**Points**: 20 points  
**Type**: Individual assignment  
**Due**: End of Wednesday class session

**Objectives**:
- Convert static matplotlib/seaborn charts to interactive Plotly visualizations
- Create engaging dashboard-style layouts
- Work with real Supabase database connections
- Generate business insights through interactive exploration

**Topics Covered**:
- Plotly basics and advanced features
- Interactive chart types (bar, scatter, time series, geographic)
- Dashboard creation with subplots
- Real-time data integration

### 🗄️ Major Assignment (Thursday): Advanced SQL-Python Analytics
**File**: `major_group_assignment_sql_analytics.ipynb`  
**Points**: 100 points  
**Type**: Group assignment (3-4 students)  
**Duration**: 2 weeks

**Objectives**:
- Establish PostgreSQL connections to cloud databases (Supabase)
- Execute complex SQL queries from Python for business intelligence
- Combine SQL analytics with interactive Plotly visualizations
- Generate strategic business recommendations

**Topics Covered**:
- SQLAlchemy database connections
- Advanced SQL (CTEs, window functions, complex JOINs)
- Marketing-sales data integration
- Customer segmentation and lifetime value analysis
- Geographic market analysis
- Executive dashboard creation

## 🔧 Technical Setup

### Database Connection
Both assignments use **Supabase PostgreSQL** to access real Brazilian e-commerce data:
- **Sales Dataset**: 100K+ orders, customers, products, reviews, sellers
- **Marketing Dataset**: Lead generation, conversions, closed deals
- **Geographic Data**: Brazilian states and cities

### Environment Setup
1. **Create `.env` file** (copy from `.env.example`):
   ```
   POSTGRES_HOST=your_supabase_host
   POSTGRES_PORT=6543
   POSTGRES_DATABASE=postgres
   POSTGRES_USER=your_username
   POSTGRES_PASSWORD=your_password
   ```

2. **Required Python packages**:
   ```python
   pandas, numpy, sqlalchemy, plotly, matplotlib, seaborn, python-dotenv
   ```

3. **Security Note**: Never commit your `.env` file to version control

## 📁 Files in This Directory

| File | Description |
|------|-------------|
| `minor_assignment_interactive_visualizations.ipynb` | Individual assignment for interactive visualization conversion |
| `major_group_assignment_sql_analytics.ipynb` | Group assignment for SQL-Python analytics |
| `.env.example` | Template for database credentials |
| `README.md` | This file - assignment instructions |

## 🎯 Learning Outcomes

By completing these assignments, students will:
- Master interactive visualization techniques with Plotly
- Connect Python to cloud PostgreSQL databases
- Execute advanced SQL analytics from Python notebooks
- Bridge marketing and sales data for business insights
- Create executive-level dashboards and reports
- Apply security best practices for database connections

## 🚀 Getting Started

### For Minor Assignment:
1. Copy `.env.example` to `.env` and add your Supabase credentials
2. Open `minor_assignment_interactive_visualizations.ipynb`
3. Update student information in the first cell
4. Follow the step-by-step tasks for visualization conversion

### For Major Assignment:
1. Form teams of 3-4 students
2. Assign roles (Data Engineer, Analyst, Visualization Specialist, Business Strategist)
3. Set up shared database access using team credentials
4. Open `major_group_assignment_sql_analytics.ipynb`
5. Complete the comprehensive business analysis

## 📊 Data Sources

### Olist Brazilian E-commerce Dataset
- **Business Context**: Brazil's largest e-commerce marketplace
- **Time Period**: 2016-2018
- **Scale**: 1.5M+ total records across all tables
- **Coverage**: All Brazilian states with geographic coordinates

### Available Schemas:
- `olist_sales_data_set`: Core business operations
- `olist_marketing_data_set`: Lead generation and conversion

## 💡 Tips for Success

1. **Database Connections**: Test your connection early and troubleshoot any issues
2. **Interactive Features**: Focus on business value, not just technical complexity
3. **Team Collaboration**: Leverage each member's strengths for the group assignment
4. **Business Context**: Always connect technical findings to business insights
5. **Documentation**: Comment your code and explain your analytical decisions

## 🔍 Common Issues & Solutions

**Connection Problems**:
- Verify credentials in `.env` file
- Check internet connectivity
- Ensure Supabase project is active

**Query Errors**:
- Use schema-qualified table names: `"schema"."table"`
- Check column names and data types
- Handle NULL values appropriately

**Visualization Issues**:
- Ensure data is properly formatted for Plotly
- Check for missing or infinite values
- Verify color scales and axis ranges

## 📚 Additional Resources

- [Plotly Documentation](https://plotly.com/python/)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)
- [Supabase Documentation](https://supabase.io/docs)
- [Brazilian E-commerce Market Context](https://en.wikipedia.org/wiki/E-commerce_in_Brazil)

---

**📧 Need Help?**
- Attend office hours for technical support
- Use class discussion forums for questions
- Collaborate with classmates for conceptual understanding

**🎉 Ready to bridge SQL and Python for real business intelligence!**