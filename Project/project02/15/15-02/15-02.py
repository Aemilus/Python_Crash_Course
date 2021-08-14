"""
15-2. Colored Cubes: Apply a colormap to your cubes plot.
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
plt.scatter(input_values[:5], cubes[:5], c=cubes[:5], cmap=plt.cm.Reds, edgecolors='none',  s=10)
# set range for each axis
plt.axis([0, 6, 0, 100])
# display the plot
plt.show()

# plot first 5000 cubic numbers
plt.scatter(input_values, cubes, c=cubes, cmap=plt.cm.Reds, edgecolors='none', s=10)
# display the plot
plt.show()
