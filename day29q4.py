import pandas as pd

df = pd.read_csv("salesdata.csv",sep=",")
print("DataFrame:\n",df)
pivot_table = pd.pivot_table(df, values='Sale_amt', index='Manager',aggfunc={'Sale_amt': ['count', 'mean']})

print(pivot_table)