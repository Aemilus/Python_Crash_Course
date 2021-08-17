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
mags, lons, lats = [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)

# map the earthquakes
data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'marker': {
        'size': [5*mag for mag in mags],
        'color': mags,
        'colorscale': 'Viridis',
        'reversescale': True,
        'colorbar': {'title': "Magnitude"},
    },
}]
my_layout = Layout(title="Global Earthquakes 30 Days")

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename="plots/global_earthquakes_30days.html")
