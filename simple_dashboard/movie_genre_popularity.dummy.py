import pandas as pd
import matplotlib.pyplot as plt

def get_df():
    ratings_df = pd.read_csv("./resources/ratings.csv")
    movies_df = pd.read_csv("./resources/movies.csv")
    movies_rating = movies_df.merge(right = ratings_df, how = "inner", on = "movieId")
    return movies_rating.join(movies_rating["genres"].str.get_dummies(sep = "|"))

def show_bar_chart(series):
    plt.bar(series.index, series.values) 
    plt.title("Movie Genre Popularity") 
    plt.xlabel("Genre")
    plt.ylabel("Number of ratings")
    plt.xticks(rotation=90)
    plt.show()

def main():
    df = get_df().drop(["movieId", "title", "genres", "userId", "rating", "timestamp"], axis = 1)
    show_bar_chart(df.sum().sort_values())

if __name__ == "__main__":
    main()