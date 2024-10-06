"""
MAIN
"""

if __name__ == "__main__":
    # load required packages
    import pandas as pd
    import matplotlib.pyplot as plt

    DATA_CSV = "https://github.com/fivethirtyeight/data/blob/e6bbbb2d35310b5c63c2995a0d03d582d0c7b2e6/covid-geography/mmsa-icu-beds.csv"

    # create a local variable and import our data
    data = pd.read_csv(
        "https://raw.githubusercontent.com/fivethirtyeight/data/refs/heads/master/covid-geography/mmsa-icu-beds.csv"
    )

    # preview a random sample of the data to test for a successful upload
    data.sample(n=10)

    # display summary statistics
    data.describe()

    # slicing columns & dropping NaN values
    plot_slice = data.iloc[:, 2].dropna()
    plot_slice2 = data.iloc[:, 3].dropna()

    # creating subplots
    fig, axes = plt.subplots(1, 2, figsize=(12, 6))

    # box plot for the ICU
    axes[0].boxplot(
        plot_slice.values,
        patch_artist=True,
        boxprops=dict(facecolor="lightblue"),
        whiskerprops=dict(color="blue"),
        capprops=dict(color="blue"),
        medianprops=dict(color="darkblue"),
    )
    axes[0].set_xticklabels(["High Risk per ICU Bed"])

    # box plot for the Hospital
    axes[1].boxplot(
        plot_slice2.values,
        patch_artist=True,
        boxprops=dict(facecolor="lightgreen"),
        whiskerprops=dict(color="green"),
        capprops=dict(color="green"),
        medianprops=dict(color="darkgreen"),
    )
    axes[1].set_xticklabels(["High Risk per Hospital"])

    # custom grid
    for ax in axes:
        ax.grid(axis="y", color="gray", linestyle="--", linewidth=0.7, alpha=0.7)
        ax.set_facecolor("whitesmoke")  # Set the background color

    # adjust layout
    plt.tight_layout()

    # display plots
    plt.show()
