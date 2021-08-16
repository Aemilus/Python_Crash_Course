"""
16-2. Sitka–Death Valley Comparison: The temperature scales on the Sitka and
Death Valley graphs reflect the different data ranges. To accurately compare
the temperature range in Sitka to that of Death Valley, you need identical
scales on the y-axis. Change the settings for the y-axis on one or both of the
charts in Figures 16-5 and 16-6. Then make a direct comparison between
temperature
"""

import csv
import matplotlib.pyplot as plt
from datetime import datetime


def get_columns_from_csv(filepath: str, *cols):
    """
    Get all values at specified columns from a csv file.
    Note: values will be handled as strings.
    :param filepath: location of csv file
    :param cols: columns to be extracted from csv file
    :return: a list with selected columns.
    """
    if not cols:
        cols = [0]

    with open(filepath) as file:
        reader = csv.reader(file)
        header = next(reader)

        values = []
        for col in cols:
            values.append([])

        for row in reader:
            for index, col in enumerate(cols):
                cell = row[col]
                values[index].append(cell)

    return values


def post_processing_columns(dates, highs, lows):
    """
    FIlter rows that have invalid data.
    For example if there is an empty string for high or low temperature then there is no need to
    keep the date for that measurement.
    :param dates: list with dates when measurement was taken
    :param highs: list with high temperatures recorded
    :param lows: list with low temperatures recorded
    :return: new lists from which invalid measurement data is removed
    """
    pp_dates, pp_highs, pp_lows = [], [], []
    for index in range(len(dates)):
        try:
            date = datetime.strptime(dates[index], '%Y-%m-%d')
            high = int(highs[index])
            low = int(lows[index])
        except ValueError:
            print("Skipping index %d:" % index, dates[index], highs[index], lows[index])
        else:
            pp_dates.append(date)
            pp_highs.append(high)
            pp_lows.append(low)

    return pp_dates, pp_highs, pp_lows


# sitka
filename = 'data/sitka_weather_2018_simple.csv'
dates, highs, lows = get_columns_from_csv(filename, 2, 5, 6)
sitka_dates, sitka_highs, sitka_lows = post_processing_columns(dates, highs, lows)

# death valley
filename = 'data/death_valley_2018_simple.csv'
dates, highs, lows = get_columns_from_csv(filename, 2, 4, 5)
dvalley_dates, dvalley_highs, dvalley_lows = post_processing_columns(dates, highs, lows)

# plot together for direct comparison
plt.style.use('seaborn')
fig, ax = plt.subplots()
plt.title("Sitka vs. Death Valley - High and Low Temperatures (2018)")
fig.autofmt_xdate()
plt.ylabel("Temperature (F)")
plt.ylim(bottom=0, top=150)
plt.tick_params(axis='both', which='major')

plt.plot(sitka_dates, sitka_highs, c='blue', label='Sitka - High')
plt.plot(sitka_dates, sitka_lows, c='orange', label='Sitka - Low')
plt.fill_between(sitka_dates, sitka_highs, sitka_lows, facecolor='blue', alpha=0.1)

plt.plot(dvalley_dates, dvalley_highs, c='purple', label='Death Valley - High')
plt.plot(dvalley_dates, dvalley_lows, c='yellow', label='Death Valley - Low')
plt.fill_between(dvalley_dates, dvalley_highs, dvalley_lows, facecolor='red', alpha=0.1)

plt.legend()
plt.savefig('sitka_vs_death_valley_2018_temperatures.png')
plt.show()
