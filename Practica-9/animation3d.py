import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# Define vertices of the square
square_vertices = np.array([[0, 0, 0],
                            [1, 0, 0],
                            [1, 1, 0],
                            [0, 1, 0]])

# Define faces of the square
square_faces = [[square_vertices[0], square_vertices[1], square_vertices[2], square_vertices[3]]]

# Define vertices of the cube
cube_vertices = np.array([[0, 0, 0],
                          [1, 0, 0],
                          [1, 1, 0],
                          [0, 1, 0],
                          [0, 0, 1],
                          [1, 0, 1],
                          [1, 1, 1],
                          [0, 1, 1]])

# Define faces of the cube
cube_faces = [[cube_vertices[0], cube_vertices[1], cube_vertices[2], cube_vertices[3]],
              [cube_vertices[4], cube_vertices[5], cube_vertices[6], cube_vertices[7]],
              [cube_vertices[0], cube_vertices[1], cube_vertices[5], cube_vertices[4]],
              [cube_vertices[2], cube_vertices[3], cube_vertices[7], cube_vertices[6]],
              [cube_vertices[1], cube_vertices[2], cube_vertices[6], cube_vertices[5]],
              [cube_vertices[0], cube_vertices[3], cube_vertices[7], cube_vertices[4]]]

# Create the figure and 3D axis
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Add the square to the plot
square_collection = Poly3DCollection(square_faces, alpha=0.5, edgecolor='k')
ax.add_collection3d(square_collection)

# Add the cube to the plot
cube_collection = Poly3DCollection(cube_faces, alpha=0.5, edgecolor='k')
ax.add_collection3d(cube_collection)

# Set axis limits
ax.set_xlim([0, 1])
ax.set_ylim([0, 1])
ax.set_zlim([0, 1])

# Show the plot
plt.show()
