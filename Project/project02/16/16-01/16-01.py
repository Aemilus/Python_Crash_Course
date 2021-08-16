"""
16-1. Sitka Rainfall: Sitka is in a temperate rainforest, so it gets a fair amount of
rainfall. In the data file sitka_weather_2018_simple.csv is a header called PRCP,
which represents daily rainfall amounts. Make a visualization focusing on the
data in this column. You can repeat the exercise for Death Valley if you’re curious
how little rainfall occurs in a desert.
"""

import csv
from datetime import datetime
import matplotlib.pyplot as plt


def plot_precipitations_from_csv_file(filepath, title="Precipitations"):
    with open(filepath) as file:
        reader = csv.reader(file)

        # skip header
        header_row = next(reader)

        # gather stats
        precipitations, dates = [], []
        for row in reader:
            try:
                current_date = datetime.strptime(row[2], '%Y-%m-%d')
                precipitation = float(row[3])
            except ValueError:
                print("Error on row:", row)
            else:
                dates.append(current_date)
                precipitations.append(precipitation)

    # plot gathered stats
    plt.style.use('seaborn')
    fig, ax = plt.subplots()
    ax.plot(dates, precipitations)

    # format plot
    plt.title(title)
    fig.autofmt_xdate()
    plt.ylabel("Precipitations")
    plt.tick_params(axis='both', which='major')

    plt.show()


plot_precipitations_from_csv_file('data/sitka_weather_2018_simple.csv', "Precipitations 2018, Sitka")
plot_precipitations_from_csv_file('data/death_valley_2018_simple.csv', "Precipitations 2018, Death Valley")
