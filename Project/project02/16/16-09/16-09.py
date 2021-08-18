"""
16-9. World Fires: In the resources for this chapter, you’ll find a file called
world_fires_1_day.csv. This file contains information about fires burning in different
locations around the globe, including the latitude and longitude, and the
brightness of each fire. Using the data processing work from the first part of
this chapter and the mapping work from this section, make a map that shows
which parts of the world are affected by fires.
You can download more recent versions of this data at
https://earthdata.nasa.gov/earth-observation-data/near-real-time/firms/active-fire-data/.
You can find links to the data in CSV format in the TXT section.
"""

import csv
from plotly import offline
from plotly.graph_objs import Layout

filepath = "world_fires_1_day.csv"

with open(filepath, encoding='utf-8') as file:
    reader = csv.reader(file)
    header = next(reader)

    lats, lons, brights = [], [], []
    for row in reader:
        lats.append(float(row[0]))
        lons.append(float(row[1]))
        brights.append(float(row[2]))

data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'marker': {
        'size': [bright / 50 for bright in brights],
        'color': brights,
        'colorscale': 'Hot',
        'reversescale': True,
        'colorbar': {'title': "Fire Brightness"}
    },
}]

layout = Layout(title="World Fires 1 Day")
fig = {
    'data': data,
    'layout': layout
}

offline.plot(fig, filename="world_fires_1day.html")
