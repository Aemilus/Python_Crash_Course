"""
16-6. Refactoring: The loop that pulls data from all_eq_dicts uses variables for
the magnitude, longitude, latitude, and title of each earthquake before appending
these values to their appropriate lists. This approach was chosen for clarity
in how to pull data from a JSON file, but it’s not necessary in your code.
Instead of using these temporary variables, pull each value from eq_dict and
append it to the appropriate list in one line. Doing so should shorten the body
of this loop to just four lines.
"""

import json

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

# explore the structure of the data
filename = "data/eq_data_30_day_m1.json"

with open(filename) as f:
    all_eq_data = json.load(f)

all_eq_dicts = all_eq_data['features']
print(len(all_eq_dicts))

# extract magnitude, longitude, latitude for each earthquake
mags, lons, lats, hover_texts = [], [], [], []
for eq_dict in all_eq_dicts:
    mags.append(eq_dict['properties']['mag'])
    lons.append(eq_dict['geometry']['coordinates'][0])
    lats.append(eq_dict['geometry']['coordinates'][1])
    hover_texts.append(eq_dict['properties']['title'])

# map the earthquakes
data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'text': hover_texts,
    'marker': {
        'size': [5*mag for mag in mags],
        'color': mags,
        'colorscale': 'Earth',
        'reversescale': True,
        'colorbar': {'title': "Magnitude"},
    },
}]
my_layout = Layout(title="Global Earthquakes 30 Days")

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename="plots/global_earthquakes_30days.html")
