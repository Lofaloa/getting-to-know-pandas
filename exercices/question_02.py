import numpy as np
import pandas as pd
import re

# Question 2: extract year from title into a new column of movie dataset

def extract_release_year(row):
    return pd.to_numeric(row["title"].rstrip()[-5:-1], errors="coerce")
 
def create_release_year_column(movies):
    movies["release_year"] = movies.apply(extract_release_year, axis = 1)

def show_movies_without_release_year(movies):
    return movies[movies["release_year"].isnull()]

def main():
    movies_df = pd.read_csv("./resources/movies.csv")
    create_release_year_column(movies_df)
    print(show_movies_without_release_year(movies_df))

if __name__ == "__main__":
    main()