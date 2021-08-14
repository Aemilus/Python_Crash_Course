"""
15-8. Multiplication: When you roll two dice, you usually add the two numbers
together to get the result. Create a visualization that shows what happens if
you multiply these numbers instead.
"""

from collections import OrderedDict
from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

# make two D6 dice
die_1 = Die(6)
die_2 = Die(6)

# roll the dice and save the results
rolls_count = 1000
results = []
for roll_number in range(rolls_count):
    result_1 = die_1.roll()
    result_2 = die_2.roll()
    # multiply instead
    result = result_1 * result_2
    results.append(result)

# analyze frequencies of results
min_result = 1  # because we multiply the result
max_result = die_1.sides_count * die_2.sides_count  # because we multiply the result
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
        title="Results of rolling two D8 dice for %d times (multiply)" % rolls_count,
        xaxis=x_axis_config,
        yaxis=y_axis_config
    )

offline.plot({'data': data, 'layout': layout}, filename='multiply_d8_d8.html')
