import numpy as np
import pandas as pd

import question_02

def count_movies_with_genre(movies, genre):
    return len(movies[movies["genres"].str.contains(genre)])

def count_movies_with_release_year(movies, release_year):
    return len(movies[movies["release_year"] == release_year])

def count_thriller_with_release_year(movies, genre, year):
    is_genre = movies["genres"].str.contains(genre)
    is_year = movies["release_year"] == year
    return len(movies[(is_genre) & (is_year)])

def main():
    movies_df = pd.read_csv("./resources/movies.csv")
    question_02.create_release_year_column(movies_df)
    print(count_thriller_with_release_year(movies_df, "Thriller", 2016))

if __name__ == "__main__":
    main()