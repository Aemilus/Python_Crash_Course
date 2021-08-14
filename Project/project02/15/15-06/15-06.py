"""
15-6. Two D8s: Create a simulation showing what happens when you roll two
eight-sided dice 1000 times. Try to picture what you think the visualization will
look like before you run the simulation; then see if your intuition was correct.
Gradually increase the number of rolls until you start to see the limits of your
system’s capabilities.
"""

from collections import OrderedDict
from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

# make two D8 dice
die_1 = Die(8)
die_2 = Die(8)

# roll the dice and save the results
rolls_count = 1000
results = []
for roll_number in range(rolls_count):
    result_1 = die_1.roll()
    result_2 = die_2.roll()
    result = result_1 + result_2
    results.append(result)

# analyze frequencies of results
min_result = 2
max_result = die_1.sides_count + die_2.sides_count
frequencies = OrderedDict()
for result in range(min_result, max_result + 1):
    frequency = results.count(result)
    frequencies[result] = frequency

# visualize data as histogram
x_values = list(frequencies.keys())
y_values = list(frequencies.values())
data = [Bar(x=x_values, y=y_values)]

x_axis_config = {'title': "Result", 'dtick': 1}
y_axis_config = {'title': "Frequency of Result"}

layout = Layout(
        title="Results of rolling two D8 dice for %d times" % rolls_count,
        xaxis=x_axis_config,
        yaxis=y_axis_config
    )

offline.plot({'data': data, 'layout': layout}, filename='d8_d8.html')
