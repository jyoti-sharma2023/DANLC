import pandas as pd
import matplotlib.pyplot as plt


orders_data = pd.DataFrame({
    'ord_no': [70001, 70009, 70002, 70004, 70007, 70005, 70008, 70010, 70003, 70012, 70011, 70013],
    'purch_amt': [150.5, 270.65, 65.26, 110.5, 948.5, 2400.6, 5760, 1983.43, 2480.4, 250.45, 75.29, 3045.6],
    'ord_date': ['2012-10-05', '2012-09-10', '2012-10-05', '2012-08-17', '2012-09-10', 
                 '2012-07-27', '2012-09-10', '2012-10-10', '2012-10-10', '2012-06-27', 
                 '2012-08-17', '2012-04-25'],
    'customer_id': [3005, 3001, 3002, 3009, 3005, 3007, 3002, 3004, 3009, 3008, 3003, 3002],
    'salesman_id': [5002, 5005, 5001, 5003, 5002, 5001, 5001, 5006, 5003, 5002, 5007, 5001]
})


purchase_stats = orders_data.groupby('customer_id')['purch_amt'].agg(['mean', 'min', 'max'])


print(purchase_stats)


purchase_stats.plot(kind='line', marker='o', figsize=(10, 6))
plt.title('Purchase Amount Statistics by Customer ID')
plt.xlabel('Customer ID')
plt.ylabel('Purchase Amount')
plt.xticks(rotation=45)
plt.grid()

plt.show()