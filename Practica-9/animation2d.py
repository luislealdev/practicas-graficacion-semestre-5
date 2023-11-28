import matplotlib.pyplot as plt
import numpy as np

# Define square vertices
square_vertices = np.array([[1, 1],
                            [2, 1],
                            [2, 2],
                            [1, 2]])

# Create figure and axis
fig, ax = plt.subplots()

# Create the square and add it to the axis
square = plt.Polygon(square_vertices, closed=True, edgecolor='black', fill=None)
ax.add_patch(square)

# Set axis limits
ax.set_xlim([0, 3])
ax.set_ylim([0, 3])

# Show the plot
plt.show()
