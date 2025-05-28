# Week 4 - Day 1 (Wednesday): Data Reshaping Lecture Content

## Session Overview
**Date:** April 30th, 2025  
**Duration:** 2 hours (120 minutes)  
**Topic:** Data Transformation - Merge, Join, Concatenate, Melt, Pivot, and Time Series Basics

## Learning Objectives
By the end of this session, students will be able to:
- Combine DataFrames using various merge and join operations
- Transform data between wide and long formats using melt and pivot
- Handle datetime data and perform basic time series operations
- Apply these techniques to real e-commerce scenarios
- Prepare data for analysis and visualization

## Session Structure (120 minutes)

### Part 1: Merge, Join, and Concatenate (40 minutes)
**File:** `01_Data_Reshaping_part1_Merge_Join_Concatenate.ipynb`

**Content Coverage:**
- Introduction to data combination (5 min)
- Concatenation with `pd.concat()` (10 min)
- Merging with `pd.merge()` - all join types (15 min)
- Advanced merging scenarios (10 min)

**Key Skills:**
- Understanding SQL JOIN equivalents in Pandas
- Handling one-to-many and many-to-many relationships
- Troubleshooting common merge issues
- Performance considerations

### Part 2: Melt and Pivot Operations (40 minutes)
**File:** `01_Data_Reshaping_part2_Melt_Pivot.ipynb`

**Content Coverage:**
- Wide vs Long format concepts (5 min)
- Melting data with `pd.melt()` (15 min)
- Pivoting data with `pd.pivot()` and `pd.pivot_table()` (15 min)
- Advanced reshaping techniques (5 min)

**Key Skills:**
- Converting between data formats for analysis
- Creating business dashboards and reports
- Handling aggregation with pivot tables
- Stack/unstack operations

### Part 3: Time Series Manipulation Basics (40 minutes)
**File:** `01_Data_Reshaping_part3_Time_Series_Basics.ipynb`

**Content Coverage:**
- Datetime data types and parsing (10 min)
- Time-based indexing and filtering (10 min)
- Resampling and time series operations (15 min)
- Time zones and real-world challenges (5 min)

**Key Skills:**
- Working with datetime indices
- Time-based data filtering and selection
- Resampling for different time frequencies
- Moving averages and trend analysis

## E-commerce Focus
All parts use realistic e-commerce scenarios:
- **Orders and Customers**: Multi-table relationships
- **Sales Analytics**: Time-based performance metrics
- **Customer Behavior**: Temporal patterns and trends
- **Global Operations**: Multi-timezone considerations

## Practice Exercises
Each part includes 4 progressive exercises:
- **Basic**: Fundamental operations
- **Intermediate**: Business scenarios
- **Advanced**: Complex multi-step problems
- **Challenge**: Real-world data cleaning

## Prerequisites
- Completed Week 1-3 content
- Understanding of Pandas DataFrame basics
- SQL knowledge for JOIN operations
- Basic datetime concepts

## Teaching Notes

### Timing Recommendations
- **Part 1:** 40 minutes (25 min teaching + 15 min exercises)
- **Part 2:** 40 minutes (25 min teaching + 15 min exercises)
- **Part 3:** 40 minutes (25 min teaching + 15 min exercises)

### Key Teaching Points
1. **Always verify results** after reshaping operations
2. **Plan transformations** step by step
3. **Connect to SQL knowledge** throughout
4. **Use realistic business examples**
5. **Demonstrate common pitfalls** and solutions

### Interactive Elements
- Live coding demonstrations
- Student exercises with immediate feedback
- Group problem-solving for complex scenarios
- SQL-to-Pandas translation practice

## Assessment Integration
This session directly supports:
- **Minor Assignment:** Data reshaping exercises (due next class)
- **Major Group Assignment:** Olist dataset exploration (Thursday)
- **Future Projects:** All require data transformation skills

## Connection to Olist Dataset
These skills are essential for Thursday's session where students will:
- Merge multiple Olist data tables
- Create customer and seller performance reports
- Analyze temporal sales patterns
- Build comprehensive business dashboards

## Common Student Challenges
1. **Merge multiplication**: Unexpected row increases due to relationships
2. **Memory usage**: Large dataset performance issues
3. **Date parsing**: Inconsistent formats in real data
4. **Index confusion**: When to use datetime indices
5. **Missing data**: Handling NaN values in time series

## Additional Resources
- SQL to Pandas cheat sheet (referenced in notebooks)
- Datetime format reference guide
- Performance optimization tips
- Real-world data cleaning examples

## Files in This Directory
- `01_Data_Reshaping_part1_Merge_Join_Concatenate.ipynb` - Part 1 content
- `01_Data_Reshaping_part2_Melt_Pivot.ipynb` - Part 2 content
- `01_Data_Reshaping_part3_Time_Series_Basics.ipynb` - Part 3 content
- `README.md` - This documentation file

## Next Session Preview
**Thursday (May 1st):** Introduction to the Olist Dataset
- Database schema exploration
- Multi-table data loading
- Initial data quality assessment
- Application of today's reshaping techniques