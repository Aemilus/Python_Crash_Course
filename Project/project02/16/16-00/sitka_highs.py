import csv
import matplotlib.pyplot as plt
from datetime import  datetime

# a csv file with weather info
filename = "data/sitka_weather_2018_simple.csv"
with open(filename) as f:
    # read the csv file
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row)

    # print columns header and their index
    for index, column_header in enumerate(header_row):
        print(index, column_header)

    # get dates and high temperatures from this file
    dates, highs = [], []
    for row in reader:
        high = int(row[5])  # what happens if you forget int()?
        highs.append(high)
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        dates.append(current_date)
    else:
        print(highs)
        print(dates)

# plot high temperatures
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red')

# format plot
plt.title("Daily high temperatures - 2018", fontsize=24)
plt.xlabel("", fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
