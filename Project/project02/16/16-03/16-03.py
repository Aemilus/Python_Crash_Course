"""
16-3. San Francisco: Are temperatures in San Francisco more like temperatures
in Sitka or temperatures in Death Valley? Download some data for San
Francisco, and generate a high-low temperature plot for San Francisco to
make a comparison.
"""
import csv
from datetime import datetime
import matplotlib.pyplot as plt


def get_columns_from_csv(filepath, *column_names):
    """
    Retrieves the desired columns from a csv file.
    The search will be done based on the name of each column name argument.
    Once the index for a desired column is found
    then the function will work with that index to retrieve the values in that column.
    :param filepath: path to csv file
    :param column_names: names of columns in the csv files
    :return: name of meteo station and a list with values for each desired column
    """
    if not column_names:
        return None

    with open(filepath) as file:
        reader = csv.reader(file)
        header_row = next(reader)

        # find the index for each column name provided
        # and save them into column_indexes list
        column_indexes = []
        for column_name in column_names:
            for column_index, header in enumerate(header_row):
                if header == column_name:
                    column_indexes.append(column_index)

        # make a list that will hold each desired column
        values = [[] for column_name in column_names]

        # fill the values list with values of each desired column
        for row in reader:
            for index, column_index in enumerate(column_indexes):
                cell = row[column_index]
                values[index].append(cell)

        # save name of meteo station
        # - fidn index of NAME header
        name_index, name = None, None
        for index, header in enumerate(header_row):
            if header == 'NAME':
                name_index = index
        # - go to begining of file and skip first row
        file.seek(0)
        next(reader)
        # - name will be the same in entire column so exit loop on first iteration
        for row in reader:
            name = row[name_index]
            break

        return name, *values


def post_process_columns(dates, highs, lows):
    """
    Cast each list of string arguments to a new list with elements of desired type.
    :param dates: list of dates as strings which will be casted to datetime
    :param highs: list of max temperatures which will be cast to integers
    :param lows: list of min temperatures which will be cast to integers
    :return: lists with casted types
    """
    pp_dates, pp_highs, pp_lows = [], [], []
    for index in range(len(dates)):
        try:
            date = datetime.strptime(dates[index], '%Y-%m-%d')
            high = int(highs[index])
            low = int(lows[index])
        except ValueError:
            print("Skipping row %index:", dates[index], highs[index], lows[index])
        else:
            pp_dates.append(date)
            pp_highs.append(high)
            pp_lows.append(low)
    return pp_dates, pp_highs, pp_lows


filepath = 'data/san_francisco_2020.csv'
station, dates, highs, lows = get_columns_from_csv(filepath, "DATE", "TMAX", "TMIN")
dates, highs, lows = post_process_columns(dates, highs, lows)

# plot statistics
plt.style.use('seaborn')
fig, ax = plt.subplots()
fig.autofmt_xdate()
plt.title(station + " (2020)")
plt.ylabel("Temperature (F)")
plt.ylim(bottom=0, top=150)
plt.tick_params(axis='both', which='major')

plt.plot(dates, highs, c='red', label="High", alpha=0.5)
plt.plot(dates, lows, c='blue', label="Low", alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='yellow', alpha=0.15)

plt.legend()

plt.savefig('san_francisco_temperatures_2020.png')
plt.show()
