import matplotlib.pyplot as plt
import pandas as pd
import os

def plot_histogram(df, column):
    plt.figure()
    df[column].hist()
    plt.title(f"Histogram of {column}")
    plt.savefig(f"plots/hist_{column}.png")
