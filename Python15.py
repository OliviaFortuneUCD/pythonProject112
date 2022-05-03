# importing pandas as pd
import pandas as pd

# Making data frame from the csv file
df = pd.read_csv("nba.csv")

# Printing the first 10 rows of the data frame for visualization
print(df[:10])


# this will replace "Boston Celtics" with "Omega Warrior"
ndf=df.replace(to_replace ="Boston Celtics",
                 value ="Omega Warrior")

print(ndf[:10])



