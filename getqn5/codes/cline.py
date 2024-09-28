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




# Read data from the text file
with open('line_data.txt', 'r') as file:
    data = file.readline()

# Extract x and y values
x, y,m = map(int, data.split(','))

c = y - m * x
x_min = x - 20  
x_max = x + 20
x1 = np.linspace(x_min, x_max, 100)

# Calculate y values for line
y1 = m * x1 + c

# Plot line
plt.plot(x1, y1, color='blue', linewidth=1)

# Annotate the points
plt.annotate(f'A\n({x}, {y})', (x, y), xytext=(x, y), textcoords='offset points', ha='center', va='top')

# Add labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Line Passing Through Point with Slope')

# Display the plot
plt.grid(True)
plt.show()
