import pandas as pd
import matplotlib.pyplot as plt

def get_df():
    ratings_df = pd.read_csv("./resources/ratings.csv")
    movies_df = pd.read_csv("./resources/movies.csv")
    return movies_df.merge(right = ratings_df, how = "inner", on = "movieId")

def find_all_genres():
    return ["Thriller", "Comedy", "Adventure", "Children", "Fantasy", "Romance", "Drama", "Action"]

def count_genres_occurences(df):
    genres = find_all_genres()
    counters = {}
    for genre in genres:
        counters[genre] = len(df[df["genres"].str.contains(genre)])
    return counters

def show_bar_chart(genres):
    plt.bar(genres[0], genres[1]) 
    plt.title("Movie Genre Popularity") 
    plt.xlabel("Genre")
    plt.ylabel("Number of ratings")
    plt.show()

def main():
    df = get_df()
    genres_occurences = count_genres_occurences(df)
    genres_df = pd.DataFrame(list(genres_occurences.items()))
    show_bar_chart(genres_df)

if __name__ == "__main__":
    main()