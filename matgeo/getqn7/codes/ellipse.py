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

# Read intersection points from the text file
with open('intersection_points.txt', 'r') as file:
    lines = file.readlines()
    
    # Extract first intersection point
    parts1 = lines[1].split(',')
    x_intersection1 = float(parts1[0].split('=')[1])
    y_intersection1 = float(parts1[1].split('=')[1])
    
    # Extract second intersection point (if it exists)
    if len(lines) > 2:  # Check if a second point is provided
        parts2 = lines[2].split(',')
        x_intersection2 = float(parts2[0].split('=')[1])
        y_intersection2 = float(parts2[1].split('=')[1])

# Define the ellipse
theta = np.linspace(0, 2 * np.pi, 1000)
x_ellipse = 3 * np.cos(theta)
y_ellipse = 2 * np.sin(theta)

# Define the line equation: y = 2 - (2/3)x, extend it fully beyond the ellipse
x_line = np.linspace(-5, 5, 1000)  # Extend line range beyond the ellipse
y_line = 2 - (2/3) * x_line

# Plot the ellipse and the fully extended line
plt.plot(x_ellipse, y_ellipse, label="Ellipse: x²/9 + y²/4 = 1")
plt.plot(x_line, y_line, label="Line: x/3 + y/2 = 1", color='orange')

# Shade the area between the line and the ellipse if there are two intersection points
if 'x_intersection2' in locals():  # Check if both intersection points are available
    # x range to shade between intersections
    x_shade = np.linspace(x_intersection1, x_intersection2, 1000)
    y_shade_line = 2 - (2/3) * x_shade               # corresponding y values of the line
    y_shade_ellipse_upper = 2 * np.sqrt(1 - (x_shade**2) / 9)  # upper half of the ellipse

    # Shade the region inside the ellipse and below the line
    plt.fill_between(x_shade, y_shade_line, y_shade_ellipse_upper, where=(y_shade_line < y_shade_ellipse_upper),
                     color='blue', alpha=0.3)

    # Mark and label the intersection points
    plt.plot(x_intersection1, y_intersection1, 'ro', label=f'P1({x_intersection1:.2f}, {y_intersection1:.2f})')
    plt.text(x_intersection1, y_intersection1 - 0.3, f'P1({x_intersection1:.2f}, {y_intersection1:.2f})', 
             horizontalalignment='center', fontsize=10, color='red')

    plt.plot(x_intersection2, y_intersection2, 'ro', label=f'P2({x_intersection2:.2f}, {y_intersection2:.2f})')
    plt.text(x_intersection2, y_intersection2 - 0.3, f'P2({x_intersection2:.2f}, {y_intersection2:.2f})', 
             horizontalalignment='center', fontsize=10, color='red')

# Labels and title
plt.title("Intersection of Ellipse and Line with Shaded Area")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.legend()

# Show the plot
plt.show()

