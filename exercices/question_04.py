import numpy as np
import pandas as pd

# Question 4: find the best comedy movies based on their average rating

def get_movies_ratings_df():
    ratings_df = pd.read_csv("./resources/ratings.csv")
    movies_df = pd.read_csv("./resources/movies.csv")
    return (movies_df
        .merge(right = ratings_df, how = "inner", on = "movieId")
        .groupby(by = ["movieId", "title", "genres"], as_index = False)
        .mean()
    )

def find_most_popular_movies(movies, nrows = 5, genre = "Comedy"):
    return (movies[movies["genres"].str.contains(genre)]
        .sort_values("rating", ascending = False)
        .head(nrows)
    )

def main():
    movies_ratings_df = get_movies_ratings_df()[["movieId", "title", "genres", "rating"]]
    print(find_most_popular_movies(movies_ratings_df, nrows = 5, genre = "Thriller"))

if __name__ == "__main__":
    main()