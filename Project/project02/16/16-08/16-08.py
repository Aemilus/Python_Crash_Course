"""
16-8. Recent Earthquakes: You can find data files containing information about
the most recent earthquakes over 1-hour, 1-day, 7-day, and 30-day periods
online. Go to https://earthquake.usgs.gov/earthquakes/feed/v1.0/geojson.php
and you’ll see a list of links to data sets for various time periods, focusing on
earthquakes of different magnitudes. Download one of these data sets, and
create
a visualization of the most recent earthquake activity.
"""

import json
from plotly import offline
from plotly.graph_objs import Layout

filepath = "2.5_month.geojson"
with open(filepath, encoding='utf-8') as file:
    eqs_data = json.load(file)
    eqs_data_title = eqs_data['metadata']['title']
    eq_mags, eq_lons, eq_lats, eq_titles = [], [], [], []
    for eq_data in eqs_data['features']:
        eq_mags.append(eq_data['properties']['mag'])
        eq_lons.append(eq_data['geometry']['coordinates'][0])
        eq_lats.append(eq_data['geometry']['coordinates'][1])
        eq_titles.append(eq_data['properties']['title'])

data =[{
    'type': 'scattergeo',
    'lon': eq_lons,
    'lat': eq_lats,
    'text': eq_titles,
    'marker': {
        'size': [2*eq_mag for eq_mag in eq_mags],
        'color': eq_mags,
        'colorscale': 'Earth',
        'reversescale': False,
        'colorbar': {'title': "Magnitude"}
    },
}]

layout = Layout(title=eqs_data_title)
fig = {
    'data': data,
    'layout': layout
}

offline.plot(fig, filename='global_earthquakes.html')
