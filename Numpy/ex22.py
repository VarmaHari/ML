import pandas as pd
x=pd.read_csv('3051715_data.csv', header=0, usecols=['shop_id','shop_name']).values
y=pd.read_csv('3051715_data.csv', header=0).values
print(x)
print(y)