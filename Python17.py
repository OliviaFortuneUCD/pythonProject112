# importing pandas as pd
import pandas as pd

# Making data frame from the csv file
df = pd.read_csv("nba.csv")

# Printing the first 10 rows of the data frame for visualization
print(df[:10])

df['dates'] = pd.Timestamp('2022-05-06')
# Printing the first 10 rows of the data frame for visualization
print(df[:10])

