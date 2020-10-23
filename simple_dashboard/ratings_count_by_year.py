import pandas as pd
import matplotlib.pyplot as plt

def create_year_column(ratings):
    ratings["publication_year"] = ratings.apply(lambda row: pd.Timestamp.fromtimestamp(row["timestamp"]).year, axis = 1)

def get_ratings_count_by_year():
    ratings_df = pd.read_csv("./resources/ratings.csv")
    create_year_column(ratings_df)
    return (ratings_df
        .groupby(by = ["publication_year"], as_index = False)
        .count()
    )

def show_ratings_count_by_year():
    ratings_by_year = get_ratings_count_by_year()[["rating", "publication_year"]]
    publication_year = ratings_by_year["publication_year"]
    ratings_count = ratings_by_year["rating"]
    plt.plot(publication_year, ratings_count, "b-o")
    plt.xlabel("Rating Publication Year")
    plt.ylabel("Number of publied ratings")
    plt.show()

def main():
    show_ratings_count_by_year()

if __name__ == "__main__":
    main()