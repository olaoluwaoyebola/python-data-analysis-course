# Week 2: Practice Exercises

## NumPy Fundamentals (Wednesday)

### Exercise 1: Array Creation and Manipulation
Create the following arrays using NumPy:
1. A 1D array of 10 zeros
2. A 1D array of 10 ones
3. A 1D array of 10 random integers between 1 and 100
4. A 2D array of shape (3, 4) filled with random floats between 0 and 1

Then, perform the following operations:
1. Add 5 to all elements in the random integers array
2. Multiply all elements in the random floats array by 10
3. Find the mean, minimum, and maximum values of both random arrays
4. Reshape the random integers array to shape (2, 5)

### Exercise 2: Array Indexing and Slicing
Create a 2D array of shape (5, 5) with values ranging from 1 to 25. Then:
1. Extract the element at row 2, column 3
2. Extract the first row
3. Extract the last column
4. Extract the subarray consisting of rows 1 through 3 and columns 2 through 4
5. Extract all even-indexed columns (0, 2, 4)
6. Set all elements in the second row to 0

### Exercise 3: Broadcasting and Vectorization
1. Create a 3x4 array of random integers between 1 and 10
2. Create a 1D array of length 4 containing the values [10, 20, 30, 40]
3. Add the 1D array to each row of the 3x4 array using broadcasting
4. Create a 1D array of length 3 containing the values [1, 2, 3]
5. Multiply each column of the 3x4 array by this 1D array using broadcasting
6. Compare the performance of a vectorized operation versus a loop for calculating the square root of each element in a large array (size 1,000,000)

### Exercise 4: Practical Application
Using NumPy, perform the following tasks:
1. Generate 1000 random data points from a normal distribution with mean 50 and standard deviation 10
2. Calculate the mean, median, and standard deviation of this data
3. Normalize the data to have a mean of 0 and standard deviation of 1
4. Create a 2D array representing 20 data points with 5 features each (random values)
5. Calculate the correlation between each pair of features
6. Find the feature with the highest average value

## Pandas Fundamentals (Thursday)

### Exercise 1: DataFrame Creation and Basic Operations
1. Create a DataFrame from the provided `numeric_data.csv` file
2. Display the first 5 rows of the DataFrame
3. Get information about the DataFrame's structure (data types, non-null values)
4. Compute basic statistics for the numeric columns
5. Create a new DataFrame from a dictionary containing:
   - Student names
   - Test scores
   - Grades
   - Subjects

### Exercise 2: Column Selection and Manipulation
Using the DataFrame created from `numeric_data.csv`:
1. Select a single column using bracket notation
2. Select a single column using dot notation
3. Select multiple columns using a list of column names
4. Create a new column that is the sum of two existing numeric columns
5. Create a new column that categorizes values in another column as 'High', 'Medium', or 'Low'
6. Rename at least two columns
7. Drop a column from the DataFrame

### Exercise 3: Row Filtering
Using the DataFrame created from `numeric_data.csv`:
1. Filter rows where a numeric column is greater than its mean
2. Filter rows where a categorical column matches a specific value
3. Filter rows that satisfy multiple conditions (using & and |)
4. Filter rows where values are in a specific list (using `isin()`)
5. Filter rows using string methods (if applicable)
6. Sort the DataFrame by a specific column (ascending and descending)
7. Get the top 3 rows based on a numeric column

### Exercise 4: SQL to Pandas Translation
Translate the following SQL queries to Pandas code:

```sql
-- Query 1
SELECT *
FROM data
WHERE value1 > 6
ORDER BY value1 DESC;

-- Query 2
SELECT id, value1, value2
FROM data
WHERE category IN ('A', 'B')
AND value3 > 15;

-- Query 3
SELECT *
FROM data
WHERE (value1 > 5 OR value2 > 12)
AND NOT category = 'B';

-- Query 4
SELECT id, category, value1 + value2 AS sum_values
FROM data
WHERE value3 BETWEEN 15 AND 20
ORDER BY sum_values;
```

## Submission Guidelines
- Complete all exercises in a Google Colab notebook
- Include comments explaining your solutions
- Submit your notebook via the course portal by next Wednesday (April 23, 2025)
- Be prepared to discuss your solutions in the next class