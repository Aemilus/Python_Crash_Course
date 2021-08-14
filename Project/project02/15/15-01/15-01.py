"""
15-1. Cubes: A number raised to the third power is a cube. Plot the first five
cubic numbers, and then plot the first 5000 cubic numbers.
"""

import matplotlib.pyplot as plt

# make chart input
input_values = list(range(5001))
cubes = [x ** 3 for x in range(5001)]

# set chart title and label axes
plt.title("Cube values")
plt.xlabel("Value", fontsize=14)
plt.ylabel("Cube", fontsize=14)

# set size of tick labels
plt.tick_params(axis='both', which='major', labelsize=10)

# plot first five cubic numbers
plt.scatter(input_values[:5], cubes[:5], edgecolors='none',  s=10, c='red')
# set range for each axis
plt.axis([0, 6, 0, 100])
# display the plot
plt.show()

# plot first 5000 cubic numbers
plt.scatter(input_values, cubes, edgecolors='none', s=10, c='red')
# display the plot
plt.show()
