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
import numpy as np
import matplotlib.pyplot as plt

def read_points_from_file(filename):
    """Reads points from a text file and returns a NumPy array."""
    with open(filename, 'r') as file:
        points = np.loadtxt(file, delimiter=',', skiprows=1)  # Assuming header row
    return points

def plot_rhombus(points):
    """Plots a rhombus based on given points."""
    # Calculate diagonal points
    diagonal_points = (points[0::2] + points[1::2]) / 2

    # Create lines
    lines = np.array([
        [points[0], diagonal_points[0]],
        [points[1], diagonal_points[1]],
        [points[2], diagonal_points[0]],
        [points[3], diagonal_points[1]]
    ])

    # Plot the rhombus
    fig, ax = plt.subplots()
    ax.plot(lines[:, :, 0].T, lines[:, :, 1].T, color='black')

    # Fill the rhombus with light blue
    ax.fill(points[:, 0], points[:, 1], color='lightblue')

    # Label the points using NumPy's vectorized operations
    labels = np.array([f'A{i+1}({point[0]}, {point[1]})' for i, point in enumerate(points)])
    ax.annotate(labels, points, xytext=(0, -5), textcoords='offset points', ha='center', va='top')

    # Show the plot
    plt.show()

# Read points from the file
points = read_points_from_file("rhombus_points.txt")  # Replace with your file name

# Plot the rhombus
plot_rhombus(points)
