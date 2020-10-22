import numpy as np
import pandas as pd

# DataFrame.index is of type Index. The documentation of the class:
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Index.html

movies_df_df = pd.read_csv("./resources/movies_df.csv")

# Demos the access of rows using loc and iloc

# The difference between the two data frame attributes is explained here:
# https://stackoverflow.com/questions/31593201/how-are-iloc-and-loc-different

# Note: in the movies_df_df data set, it doesn't make a difference as the index is
# a number 

print(list(movies_df.columns))
print(movies_df.columns[0:2])
print(movies_df.columns.dtype)

print(movies_df[["title", "genres"]].head())

print(movies_df.loc[10:20]) # Prints movies_df from index 10 to 20
print(movies_df.loc[0, "title"]) # Prints the title of the movie named 0 (index)