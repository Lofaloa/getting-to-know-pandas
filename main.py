import numpy as np
import pandas as pd

def show_columns(movies):
    """ Demo the dataframe index features
    
    DataFrame.index is of type Index. The documentation of the class:
    https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Index.html
    """
    print(list(movies.columns))
    print(movies.columns[0:2])
    print(movies.columns.dtype)

def accessing_columns(movies):
    print(movies[["title", "genres"]].head())

def access_rows(movies):
    """ Demos the access of rows using loc and iloc

    The difference between the two data frame attributes is explained here:
    https://stackoverflow.com/questions/31593201/how-are-iloc-and-loc-different

    Note: in the movies data set, it doesn't make a difference as the index is
    a number 
    """
    print(movies.loc[10:20]) # Prints movies from index 10 to 20
    print(movies.loc[0, "title"]) # Prints the title of the movie named 0 (index)

def main():
    movies_df = pd.read_csv("./resources/movies.csv")
    access_rows(movies_df)

if __name__ == "__main__":
    main()