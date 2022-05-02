import pandas as pd

df = pd.read_csv('dirtydata.csv')
#print(df)

#replace the null values with 130



df.fillna(130, inplace = True)
print(df)