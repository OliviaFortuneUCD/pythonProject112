#Bad data could be:

#Empty cells
#Data in wrong format
#Wrong data
#Duplicates
import pandas as pd

df = pd.read_csv('dirtydata.csv')
#print(df)
#df.info()
#print(df.describe())
# get the number of missing data points per column
#missing_values_count = df.isnull().sum()
#print(missing_values_count)
 



#One way to deal with empty cells is to remove rows that contain empty cells.

#new_df = df.dropna()

#print(new_df.to_string())