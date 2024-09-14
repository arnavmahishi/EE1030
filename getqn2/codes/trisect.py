

#Code by GVV Sharma
#September 12, 2023
#Revised July 21, 2024
#released under GNU GPL
#Point Vectors


import sys                                          #for path to external scripts
sys.path.insert(0,'/home/arnav/matgeo/codes/CoordGeo')        #path to my scripts
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

with open(points, 'r') as file:
  lines = file.readlines()

# Define the coordinates of points P, A, and B
point_P = tuple(map(float, lines[0].strip().replace('B(', '').replace(')', '').split(', ')))
point_A = tuple(map(float, lines[1].strip().replace('C(', '').replace(')', '').split(', ')))
point_B = tuple(map(float, lines[2].strip().replace('A(', '').replace(')', '').split(', ')))

# Create the plot
plt.figure(figsize=(6, 6))

# Plot the points with labels and coordinates
plt.plot(point_P[0], point_P[1], 'o', markersize=10, label='P')
plt.text(point_P[0], point_P[1] - 0.5, f'P ({point_P[0]}, {point_P[1]})', ha='center')
plt.plot(point_A[0], point_A[1], 'o', markersize=10, label='A')
plt.text(point_A[0], point_A[1] - 0.5, f'A ({point_A[0]}, {point_A[1]})', ha='center')
plt.plot(point_B[0], point_B[1], 'o', markersize=10, label='B')
plt.text(point_B[0], point_B[1] - 0.5, f'B ({point_B[0]}, {point_B[1]})', ha='center')

# Draw the lines from P to A and P to B
plt.plot([point_P[0], point_A[0]], [point_P[1], point_A[1]], '-b', label='P-A')
plt.plot([point_P[0], point_B[0]], [point_P[1], point_B[1]], '-b', label='P-B')

# Add labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Points and Connecting Lines')

# Add legend
plt.legend()

# Show the plot
plt.grid(True)
plt.show()
