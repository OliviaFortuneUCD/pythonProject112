import pandas as pd

df = pd.read_csv('Dirtydata.csv')
#drop rows > 120
for x in df.index:
  if df.loc[x, "Duration"] > 120:
    df.drop(x, inplace = True)
print(df)