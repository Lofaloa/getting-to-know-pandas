import numpy as np
import pandas as pd

def count(ratings):
    return len(ratings)

def count_unique_values(ratings):
    # nunique ne compte pas les NaN
    return len(ratings["rating"].nunique())

def count_ratings_equal_to(ratings, value):
    return len(ratings[ratings["rating"] == value])

def find_movies_rated_to(ratings, value):
    return ratings[ratings["rating"] == value]

def find_first_most_popular_movie(ratings):
    # Just needed to count the number of times a movie appears with a rating of 4
    return ratings[["movieId", "rating"]].groupby("movieId").mean().idxmax()

def __get_timestamp(day, month, year):
    return pd.Timestamp(day = day, month = month, year = year).timestamp()

def count_ratings_for_year(ratings, year):
    # It is possible to add a new column using the following code:
    # ratings["date"] = pd.to_datetime(ratings["timestamp"], unit = "s")
    start = __get_timestamp(31, 12, year - 1)
    end = __get_timestamp(1, 1, year + 1)
    return len(ratings[(ratings["timestamp"] > start) & (ratings["timestamp"] < end)])

def main():
    ratings_df = pd.read_csv("./resources/ratings.csv")
    print(count_ratings_for_year(ratings_df, 2015))

if __name__ == "__main__":
    main()