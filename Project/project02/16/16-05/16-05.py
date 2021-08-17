"""
16-5. Explore: Generate a few more visualizations that examine any other
weather aspect you’re interested in for any locations you’re curious about.
"""
import csv
import matplotlib.pyplot as plt
from datetime import datetime

# AWND = Average daily wind speed (tenths of meters per second)
# PRCP = Precipitation (tenths of mm)
# TMAX = Maximum temperature (tenths of degrees C)
# TMIN = Minimum temperature (tenths of degrees C)
# TAVG = Average temperature (tenths of degrees C)

# parse csv file
filepath = 'data/new_york_2015.csv'
with open(filepath) as file:
    reader = csv.reader(file)
    header = next(reader)

    # desired measurements
    dates = []
    wind_avgs = []
    precipitations = []
    temp_avgs, temp_highs, temp_lows = [], [], []

    # gather measurements from csv file
    for row in reader:
        try:
            date = datetime.strptime(row[2], '%Y-%m-%d')
            awnd = float(row[3])
            prcp = float(row[5])
            tavg = float(row[8])
            tmax = float(row[9])
            tmin = float(row[10])
        except ValueError:
            print(f"Skipping row {row}: date={date}, awnd={awnd}, prcp={prcp}, tavg={tavg}, tmax={tmax}, tmin={tmin}")
        else:
            dates.append(date)
            wind_avgs.append(awnd)
            precipitations.append(prcp)
            temp_avgs.append(tavg)
            temp_highs.append(tmax)
            temp_lows.append(tmin)

# plot gathered measurements
plt.style.use('seaborn')
fig, axs = plt.subplots(3)
fig.suptitle("JFK INTERNATIONAL AIRPORT, NY US (2015)")

axs[0].plot(dates, temp_avgs, c='green', label='Average', linewidth=0.5)
axs[0].plot(dates, temp_highs, c='red', label='Maximum', linewidth=0.5)
axs[0].plot(dates, temp_lows, c='blue', label='Minimum', linewidth=0.5)
degree_symbol = u'\N{DEGREE SIGN}'
axs[0].set(ylabel=f"Temperature ({degree_symbol}C)")
axs[0].legend(loc='upper left')

axs[1].plot(dates, wind_avgs, c='purple', linewidth=0.5)
axs[1].set(ylabel="Average wind speed (m/s)")

axs[2].plot(dates, precipitations, c='orange', linewidth=0.5)
axs[2].set(ylabel="Precipitation (mm)")

plt.savefig("new_york_2015.png")
plt.show()
