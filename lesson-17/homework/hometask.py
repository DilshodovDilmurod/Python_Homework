### Homework1
import pandas as pd
data = {'First Name': ['Alice', 'Bob', 'Charlie', 'David'], 'Age': [25, 30, 35, 40], 'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']} 
df = pd.DataFrame(data)
df
`1.Rename column names using function. "First Name" --> "first_name", "Age" --> "age

df.rename(columns = {
    'First Name': 'first_name',
    'Age':'age'
}, inplace=True)
df
2 Print the first 3 rows of the DataFrame
df.head(3)
3 Find the mean age of the individuals

df['mean_age'] = df.age.mean()
df
4 Select and print only the 'Name' and 'City' columns
 
df[['first_name', 'City']]
5 Add a new column 'Salary' with random salary values

import numpy as np 
val = np.random.rand(4)
df['Salary'] = val
6 Display summary statistics of the DataFrame

df.describe()
## homework 2
1 Create a DataFrame named sales_and_expenses with columns 'Month', 'Sales', and 'Expenses', representing monthly sales and expenses data. Use below table.
data = {'Month':['Jan', 'Feb', 'Mar', 'Apr'], 'Sales':[5000, 6000, 7500, 8000], 'Expenses':[3000, 3500, 4000, 4500]}
sales_and_expenses = pd.DataFrame(data)
sales_and_expenses
2 Calculate and display the maximum sales and expenses.

max_salary = sales_and_expenses.Sales.max()
max_expenses = sales_and_expenses.Expenses.max()
print("max salary:",max_salary)
print("max expenses:", max_expenses)
3 Calculate and display the minimum sales and expenses.

min_salary = sales_and_expenses.Sales.min()
min_expenses = sales_and_expenses.Expenses.min()
print("min salary:",min_salary)
print("min expenses:", min_expenses)
4 Calculate and display the average sales and expenses.

mean_salary = sales_and_expenses.Sales.mean()
mean_expenses = sales_and_expenses.Expenses.mean()
print("mean salary:",mean_salary)
print("mean expenses:", mean_expenses)
## Homework 3
1 Create a DataFrame named expenses with columns 'Category', 'January', 'February', 'March', and 'April', representing monthly expenses for different categories. Use below table.
data = {
    'Category': ['Rent', 'Utilities', 'Groceries', 'Entertainment'],
    'January': [1200, 200, 300, 150],
    'February': [1300, 220, 320, 160],
    'March': [1400, 240, 330, 170],
    'April': [1500, 250, 350, 180]
}
expenses = pd.DataFrame(data)
expenses.set_index('Category', inplace=True)
expenses
2 Calculate and display the maximum expense for each category.

expenses.max(axis=1)
3 Calculate and display the minimum expense for each category.

expenses.min(axis=1)
4 Calculate and display the average expense for each category.

expenses.mean(axis=1)
