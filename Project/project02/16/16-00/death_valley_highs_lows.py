import csv
import matplotlib.pyplot as plt
from datetime import  datetime

# a csv file with weather info
filename = "data/death_valley_2018_simple.csv"
with open(filename) as f:
    # read the csv file
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row)

    # print columns header and their index
    for index, column_header in enumerate(header_row):
        print(index, column_header)

    # get dates, and high and low temperatures from this file
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        try:
            high = int(row[4])  # what happens if you forget int()?
            low = int(row[5])
        except ValueError:
            print("Missing data for %s." % current_date)
        else:
            highs.append(high)
            lows.append(low)
            dates.append(current_date)
    else:
        print("highs:", highs)
        print("lows:", lows)
        print("dates:", dates)

# plot high and low temperatures
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.5)
ax.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# format plot
plt.title("Daily high and low temperatures - 2018\nDeath Valley, CA", fontsize=20)
plt.xlabel("", fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
