import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    plt.figure(figsize=(10, 5))
    plt.scatter(df["Year"], df["CSIRO Adjusted Sea Level"], label="Original Data")

    # Create first line of best fit for all data
    res_all = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
    x_pred_all = pd.Series(range(1880, 2051))
    y_pred_all = res_all.intercept + res_all.slope * x_pred_all
    plt.plot(x_pred_all, y_pred_all, 'r', label='Fit: All Data')

    # Create second line of best fit for year >= 2000
    df_recent = df[df["Year"] >= 2000]
    res_recent = linregress(df_recent["Year"], df_recent["CSIRO Adjusted Sea Level"])
    x_pred_recent = pd.Series(range(2000, 2051))
    y_pred_recent = res_recent.intercept + res_recent.slope * x_pred_recent
    plt.plot(x_pred_recent, y_pred_recent, 'g', label='Fit: Since 2000')

    # Add labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")
    plt.legend()

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
