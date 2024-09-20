import pandas as pd

df = pd.read_csv("salesdata.csv",sep=",")
print("DataFrame:\n",df)
pivot_table_product = pd.pivot_table(df, values='Sale_amt', index='Item', aggfunc='sum')
pivot_table_salesperson = pd.pivot_table(df, values='Sale_amt', index='SalesMan', aggfunc='sum')

# Identify the top-selling product and salesperson
top_product = pivot_table_product.idxmax()[0]
top_salesperson = pivot_table_salesperson.idxmax()[0]

print("Total Sales by Product:")
print(pivot_table_product)
print("\nTotal Sales by Salesperson:")
print(pivot_table_salesperson)
print("\nTop-Selling Product:", top_product)
print("Top-Selling Salesperson:", top_salesperson)


# Total sales amount for top product and top salesperson
top_product_sales = pivot_table_product.max()
top_salesperson_sales = pivot_table_salesperson.max()