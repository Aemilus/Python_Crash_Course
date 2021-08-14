"""
15-7. Three Dice: When you roll three D6 dice, the smallest number you can roll
is 3 and the largest number is 18. Create a visualization that shows what happens
when you roll three D6 dice.
"""

from collections import OrderedDict
from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

# make three D6 dice
die_1 = Die(6)
die_2 = Die(6)
die_3 = Die(6)

# roll the dice and save the results
rolls_count = 50_000
results = []
for roll_number in range(rolls_count):
    result_1 = die_1.roll()
    result_2 = die_2.roll()
    result_3 = die_3.roll()
    result = result_1 + result_2 + result_3
    results.append(result)

# analyze frequencies of results
min_result = 3
max_result = die_1.sides_count + die_2.sides_count + die_3.sides_count
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
        title="Results of rolling three D6 dice for %d times" % rolls_count,
        xaxis=x_axis_config,
        yaxis=y_axis_config
    )

offline.plot({'data': data, 'layout': layout}, filename='3xD6.html')
