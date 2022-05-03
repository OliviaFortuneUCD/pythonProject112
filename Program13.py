import pandas as pd

df = pd.read_csv('Dirtydata.csv')

print(df.duplicated())

df.drop_duplicates(inplace = True)
