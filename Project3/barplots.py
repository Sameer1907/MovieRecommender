import pandas as pd
from pandas.api.types import CategoricalDtype
import numpy as np
import matplotlib.pyplot as plt


def main():

    dtype_dict = {
        "key": "string",
        "utility": "category",
        "usability": "float",
        "interface": "float",
        "relevance": CategoricalDtype(
            categories=["Low", "Medium", "High"], ordered=True),
        "response_time": CategoricalDtype(
            categories=["Slow", "Neutral", "Fast"], ordered=True),
        "quality": CategoricalDtype(categories=["Bad", "Average", "Good"], ordered=True),
        "use?": CategoricalDtype(categories=["No", "Yes"], ordered=True),
        "recommend?": CategoricalDtype(categories=["No", "Yes"], ordered=True),
        "overall": "float",
        "num_liked": "float"
    }

    df = pd.read_csv("./feedback.csv", dtype=dtype_dict)
    cat_cols = df.select_dtypes(["category"]).columns
    df[cat_cols] = df[cat_cols].apply(lambda x: x.cat.codes)
    print(df)

    for column in df.columns:
        if column in ["key", "utility"]:
            continue
        x = ["MovieRecommender", "PickAMovie", "SuggestMeMovie"]
        means = []
        for site in df["utility"].unique():
            sitedf = df.loc[df["utility"] == site]
            means.append(sitedf[column].mean())
        x_pos = [i for i, _ in enumerate(x)]

        plt.clf()
        plt.bar(x_pos, means)
        plt.xlabel("website")
        plt.ylabel("Mean {}".format(column))
        plt.title("Website vs mean {}".format(column))
        plt.xticks(x_pos, x)

        plt.savefig("./plots/{}.png".format(column))


if __name__ == "__main__":
    main()
