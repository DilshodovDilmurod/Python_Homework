import pandas as pd 
import sqlite3
# customers
sql_query = "select * from customers"
with sqlite3.connect('chinook.db') as conn:
    Customers = pd.read_sql_query(sql_query, conn)
Customers.head(5)
# invoices 
sql_query = "select * from invoices"
with sqlite3.connect('chinook.db') as conn:
    invoices = pd.read_sql_query(sql_query, conn)
invoices.head(3)
Find the total amount spent by each customer on purchases (considering invoices).
sql_query="select * from invoice_items"
with sqlite3.connect("chinook.db") as conn:
    invoice_items = pd.read_sql_query(sql_query, conn)
invoice_items.head(3)
##  Customer Purchases Analysis:
(invoices
 .groupby('CustomerId')
 .agg(total_amount = ('Total', 'sum')))
Identify the top 5 customers with the highest total purchase amounts.
(invoices
 .groupby('CustomerId')
 .agg(total_amount = ('Total', 'sum'))
 .sort_values('total_amount', ascending=False)).head()
Display the customer ID, name, and the total amount spent for the top 5 customers.
df2 = (invoices
 .groupby('CustomerId')
 .agg(total_amount = ('Total', 'sum'))
 .sort_values('total_amount', ascending=False)).head()
df3 = df2.merge(Customers, how='inner', left_index=True, right_on='CustomerId')
df3[['CustomerId', 'FirstName', 'LastName', 'total_amount']]
# Album vs. Individual Track Purchases
invoices.head(3)
Determine the percentage of customers who prefer to buy individual tracks instead of full albums.
df = invoice_items.merge(invoices, how='inner', on = 'InvoiceId')
customer_of_buy_track = (df.groupby('CustomerId')
                         .agg(total_track_num = ('TrackId', 'count')))

num_one_track = customer_of_buy_track[customer_of_buy_track['total_track_num'] == 1].shape[0]

total_customers = invoices['CustomerId'].nunique()

persantage = num_one_track/total_customers * 100
persantage
A customer is considered to prefer individual tracks if they have purchased only a subset of tracks from an album.
df = invoice_items.merge(invoices, how='inner', on = 'InvoiceId')
customer_of_buy_track = (df.groupby('CustomerId')
                         .agg(total_track_num = ('TrackId', 'count'))
                         .reset_index())

df1 = df.merge(customer_of_buy_track, how='inner', on='CustomerId')
df1['cus_status']=df1['total_track_num'].apply(lambda x: 'individual tracks' if x == 1 else 'full albums')
df1.head()

Provide a summary of the percentage of customers who fall into each category (individual tracks vs. full albums).
df = invoice_items.merge(invoices, how='inner', on = 'InvoiceId')
customer_of_buy_track = (df.groupby('CustomerId')
                         .agg(total_track_num = ('TrackId', 'count'))
                         .reset_index())

df1 = df.merge(customer_of_buy_track, how='inner', on='CustomerId')
df1['cus_status']=df1['total_track_num'].apply(lambda x: 'individual tracks' if x == 1 else 'full albums')
df1.groupby('cus_status').agg(total_cus = ('CustomerId', 'count')) # data boyicha hamma full albumga kiradi 
