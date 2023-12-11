import pandas as pd
import matplotlib.pyplot as plt


a=pd.read_csv("3051715_data.csv")

# print(a.head(12))
# print(a.tail(12))
# print(a.to_string()) 
# print(a.dtypes)
# a_excel=a.to_excel("axls.xlsx", sheet_name="shopify", index=False) # converting the csv file to excel

# b=pd.read_excel("axls.xlsx", sheet_name="shopify")
# print(b.to_string()) 
# print(b.info()) # check the info for the file

# c=a[["shop_id","shop_domain"]].describe
# c=a[["shop_id","shop_domain"]]
# c=a[["shop_id","shop_domain"]].shape
# print(c.to_string()) 
# print(c.head(4)) 

# for ploting the data
d=pd.read_csv("3051715_data.csv", index_col=1, parse_dates=True)
# print(d[['shop_id', 'reason']])
# print(d[['reason']])
print(d[['reason']].head(12))



# d.plot()
# d['shop_id'].plot()
# plt.show()











