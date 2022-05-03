#replace the blank data with the median
import pandas as pd

df = pd.read_csv('Dirtydata.csv')

x = df["Calories"].median()
#print(x)
#nan_values = df[df['Calories'].isna()]

#print(nan_values)

df["Calories"].fillna(x, inplace = True)

nan_values = df[df['Calories'].isna()]

print(nan_values)
print(df)

#print(df.to_string())
