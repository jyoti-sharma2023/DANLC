import pandas as pd

df = pd.read_csv("sales-data.csv",sep=",")
print("DataFrame:\n",df)

#pivot=pd.pivot_table(df,index='Product',values=['Quantity','Sales'],aggfunc=['sum'],margins=True,margins_name='total')
#pivot=pd.pivot_table(df,index=['Rep','Manager',],values=['Quantity','Sales'],aggfunc=['sum'],margins=True,margins_name='total')
pivot=pd.pivot_table(df,index=['Rep','Manager'],columns='Product',values=['Quantity','Sales'],aggfunc=['sum','mean'],margins=True,margins_name='total')

print (pivot)
