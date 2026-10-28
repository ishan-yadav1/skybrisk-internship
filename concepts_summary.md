# Month 1 Concepts Learned — Python Basics and Data Manipulation

## Week 1: Introduction to Python
- **Variables:** Names used to store values, such as `temperature = 28.5`.
- **Data types:** Common types include `int`, `float`, `str`, and `bool`.
- **Operators:** Arithmetic (`+`, `-`, `*`, `/`), comparison (`>=`, `==`), and logical (`and`, `or`, `not`) operators.
- **Input/output:** `input()` reads text from the user; `print()` displays output.
- **Conditions:** `if`, `elif`, and `else` run code based on a condition.
- **Loops:** `for` iterates over a sequence; `while` repeats while a condition is true.
- **Functions:** Reusable blocks of code that can accept inputs and return results.

## Week 2: Data Structures and Functions
- **List:** Ordered and mutable collection, e.g. `[10, 20, 30]`.
- **Tuple:** Ordered and immutable collection, e.g. `(10, 20, 30)`.
- **Dictionary:** Stores key-value pairs, e.g. `{"city": "Delhi"}`.
- **Set:** Stores unique values and removes duplicates.
- **List comprehension:** Concise way to build a list, e.g. `[x*x for x in values]`.
- **Lambda:** Small anonymous function, e.g. `lambda x: x * 2`.
- **Recursion:** A function calls itself and needs a base case to stop.
- **Data cleaning:** Fixing missing, duplicate, invalid, or inconsistent values before analysis.

## Week 3: NumPy and Pandas
- **NumPy array:** Efficient structure for numerical data and vectorized calculations.
- **Broadcasting:** Lets compatible arrays participate in operations without manually repeating values.
- **Pandas Series:** One-dimensional labeled data.
- **Pandas DataFrame:** Two-dimensional table with rows and columns.
- **Indexing/filtering:** Select rows and columns using labels, positions, or conditions.
- **Grouping and aggregation:** `groupby()` with operations such as `mean()`, `sum()`, and `count()`.
- **Missing values:** Pandas can detect them with `isna()` and handle them with methods such as `fillna()` or `dropna()`.

## Week 4: Data Visualization
- **Matplotlib:** Library for creating and customizing plots.
- **Seaborn:** Higher-level statistical visualization library built on Matplotlib.
- **Histogram:** Shows the distribution of a numerical variable.
- **Scatter plot:** Shows the relationship between two numerical variables.
- **Heatmap:** Uses color to represent values in a matrix, such as a correlation matrix.
- **Dashboard:** Brings key metrics, tables, and plots together in one report.

## What this project does
The project loads a sample weather CSV, validates columns, removes duplicate records, handles missing values, calculates city-level statistics with Pandas, computes numerical summaries with NumPy, and creates charts using Matplotlib and Seaborn.

## Limitations
The included dataset is a small illustrative dataset for learning. It is not a live or official weather dataset. Median imputation is a simple demonstration approach and may not be suitable for every real-world dataset.
