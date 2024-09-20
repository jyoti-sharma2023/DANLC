import pandas as pd

df = pd.read_csv("salesdata.csv",sep=",")
print("DataFrame:\n",df)
pivot_table = pd.pivot_table(df, values='Units', index='Region', columns='Item', aggfunc='sum')

print(pivot_table)