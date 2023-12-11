import pandas as pd

titanic=pd.read_csv("titanic.csv")
# print(titanic)
# print(titanic.head(10))
# print(titanic.dtypes)


titanic_excel = titanic.to_excel("titanic.xlsx", sheet_name="passengers", index=False)
titanic=pd.read_excel("titanic.xlsx", sheet_name="passengers")
# print(titanic.head())

ages=titanic[['Age',"Ticket"]]
above_35 = titanic[titanic["Age"] > 35]
# print(above_35.head())

data = titanic['Age'] > 35
# print(data)


p_class = titanic[titanic["Pclass"].isin([2,3])]
# print(p_class.head)

age_no_na = titanic[titanic["Age"].notna()]
# print(age_no_na.head())

adult_names = titanic.loc[titanic["Age"] > 35, ["Name", "Survived", "Ticket"]]
# print(adult_names.head())

# print(titanic.iloc[9:25, 2:5])

# print(titanic['Age'].mean())

# print(titanic['Age'].median())

# print(titanic['Age'].mode())

# print(titanic['Age'].describe())
# print(titanic['Name'].str.lower())

new_data = titanic['Name'].str.split(",")
# print(new_data)


titanic['Surname'] = titanic['Name'].str.split(",").str.get(0)
# print(titanic['Surname'])

print("With surname:\n",titanic)