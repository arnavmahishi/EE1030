#Code by GVV Sharma
#September 12, 2023
#Revised July 21, 2024
#released under GNU GPL
#Point Vectors


import sys                                          #for path to external scripts
sys.path.insert(0, '/home/arnav/matgeo/codes/CoordGeo')        #path to my scripts
import numpy as np
import numpy.linalg as LA
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from mpl_toolkits.mplot3d import Axes3D

#local imports
from line.funcs import *
from triangle.funcs import *
from conics.funcs import circ_gen
import ctypes
from ctypes import Structure, c_double
# Read data from the text file
with open("circle_data.txt", "r") as f:
    lines = f.readlines()

# Extract the points, center, and radius
x1, y1 = map(float, lines[0].split(","))
x2, y2 = map(float, lines[1].split(","))
x3, y3 = map(float, lines[2].split(","))
center_x, center_y = map(float, lines[3].split(","))
radius = float(lines[4])

# Generate points for the circle
theta = np.linspace(0, 2 * np.pi, 100)
x_circle = center_x + radius * np.cos(theta)
y_circle = center_y + radius * np.sin(theta)

# Plot the circle and points
plt.plot(x_circle, y_circle, color='blue')
plt.scatter([x1, x2, x3], [y1, y2, y3], color='red', label='Points')
plt.scatter(center_x, center_y, color='green', label='Center')

# Label the points with coordinates
plt.text(x1, y1 - 0.2, f"({x1:.2f}, {y1:.2f})", ha='center')
plt.text(x2, y2 - 0.2, f"({x2:.2f}, {y2:.2f})", ha='center')
plt.text(x3, y3 - 0.2, f"({x3:.2f}, {y3:.2f})", ha='center')
plt.text(center_x, center_y + 0.2, f"({center_x:.2f}, {center_y:.2f})", ha='center')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Circle and Points')
plt.legend()
plt.grid(True)
plt.axis('equal')  # Ensure x and y axes have the same scale
plt.show()
