import numpy as np
import pandas as pd

def extract_year(title):
    index = title.find('(')
    yearStr = title[index + 1:-1]
    return int(yearStr)

def main():
    movies_df = pd.read_csv("./resources/movies.csv")
    movies_df["release_year"] = movies_df.apply(lambda m: m["title"][-5:-1], axis = 1)
    # movies_df["release_year"] = movies_df["title"].str[-5:-1]
    print(movies_df)

if __name__ == "__main__":
    main()