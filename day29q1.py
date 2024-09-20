import pandas as pd

df = pd.read_csv("salesdata.csv",sep=",")
print("DataFrame:\n",df)
#pivot=pd.pivot_table(df,index='Region',values=['Manager','SalesMan'],aggfunc=['sum'],margins=True,margins_name='total')
pivot_table = pd.pivot_table(df,
                             values='Sale_amt', 
                             index=['Region', 'Manager', 'SalesMan'],  
                             aggfunc='sum')
print (pivot_table)