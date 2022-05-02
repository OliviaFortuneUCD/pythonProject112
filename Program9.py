import pandas as pd

df = pd.read_csv('dirtydata.csv')
#print(df)

#replace the calorie that are null null values with 130



df["Calories"].fillna(130, inplace = True)
print(df)