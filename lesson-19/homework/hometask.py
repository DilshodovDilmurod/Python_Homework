import pandas as pd 
# Homework Assignment 1: Analyzing Sales Data
sales_data = pd.read_csv('sales_data.csv', parse_dates=['Date'])
sales_data.head()
1 Group the data by the Category column and calculate the following aggregate statistics for each category:
Total quantity sold.
Average price per unit.
Maximum quantity sold in a single transaction.
(sales_data
 .groupby('Category')
 .agg(total_quantity = ('Quantity', 'sum'),
        mean_price = ('Price', 'mean'),
        max_quantity = ('Quantity', 'max')))
2 Identify the top-selling product in each category based on the total quantity sold.
def top_product(group):
    return group.nlargest(1, 'Quantity')

(sales_data
 .groupby('Category')
 .apply(top_product))['Product']
3 Find the date on which the highest total sales (quantity * price) occurred.
sales_data.nlargest(1, 'total_sales')['Date']
# Homework Assignment 2: Examining Customer Orders
customer_orders = pd.read_csv('customer_orders.csv')
customer_orders.head()
1 Group the data by CustomerID and filter out customers who have made less than 20 orders.
df =(customer_orders
    .groupby('CustomerID')
    .agg(total_quantity = ('OrderID', 'count')))
df[df['total_quantity']>=20]
2 Identify customers who have ordered products with an average price per unit greater than $120.
df1 = (customer_orders
        .groupby('CustomerID')
        .agg(mean_price = ('Price', 'mean')))
df1[df1['mean_price']> 120]
3 Find the total quantity and total price for each product ordered, and filter out products that have a total quantity less than 5 units.
df2 = (customer_orders
        .groupby('Product')
        .agg(total_quantity = ('Quantity', 'sum'),
            total_price = ('Price', 'sum')))
df2[df2['total_quantity']>5]
# Homework Assignment 3: Population Salary Analysis
import sqlite3
sql_query = """select * from population"""
with sqlite3.connect('population.db') as conn:
    population = pd.read_sql_query(sql_query, conn)

population.head()
def Salary_status(Salary):
    if Salary< 1000000:
        return "low"
    elif Salary < 1500000:
        return "middile"
    else: 
        return "high"
# salary ni category ga ajratish
population['salary_status']= population['salary'].apply(Salary_status)
population['full_name'] = population['first_name'] + "_" + population['last_name']
Percentage of population for each salary category;
(population
 .groupby('salary_status')
 .agg(total_population = ('full_name', 'count')))/ population['full_name'].count() *100
Average salary in each salary category;
Median salary in each salary category;
Number of population in each salary category;
(population
 .groupby('salary_status')
 .agg(mean_salary = ('salary', 'mean'),
      median_salary = ('salary', 'median'),
      num_of_pop = ('full_name', 'count')))
Calculate the same measures in each State
(population
 .groupby('state')
 .agg(count_population = ('full_name', 'count'),
      mean_salary = ('salary', 'mean'),
      max_salary = ('salary', 'max'))).astype('int')
