import pandas as pd

df = pd.read_csv('Dirtydata.csv')

df['Date'] = pd.to_datetime(df['Date'])

#print(df.to_string())
#drop if null
df.dropna(subset=['Date'], inplace = True)
print(df.to_string())