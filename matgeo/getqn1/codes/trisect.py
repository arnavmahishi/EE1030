import matplotlib.pyplot as plt

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

# Read coordinates from the text file (assuming 4 points)
with open("coordinates.txt", 'r') as f:
    lines = f.readlines()
    ax, ay = map(float, lines[0].split()[1:])
    bx, by = map(float, lines[1].split()[1:])
    px, py = map(float, lines[2].split()[1:])
    rx, ry = map(float, lines[3].split()[1:])

# Create a figure and axis
fig, ax = plt.subplots()

# Plot points with labels and colors
ax.scatter(ax, ay, color='blue', label=f"a: ({ax}, {ay})")
ax.scatter(bx, by, color='blue', label=f"b: ({bx}, {by})")
ax.scatter(px, py, color='red', label=f"p: ({px}, {py})")
ax.scatter(rx, ry, color='blue', label=f"r: ({rx}, {ry})")

# Draw line from a to b
ax.plot([ax, bx], [ay, by], color='black')

# Show the plot
plt.legend()
plt.show()
