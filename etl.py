import pandas as pd

data ={'Name':['Alice', 'Bob', 'Charlie'], 'Age' :[25,30,40]}
df=pd.dataFrame(data)
df.to_csv('Output.csv', index=False)

print('ETL job completed. data saved to output.csv')
