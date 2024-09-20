import sys
sys.path.insert(0, '/home/arnav/matgeo/codes/CoordGeo')
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

def plot_plane_and_normal(plane_normal):
    # Extract coefficients from the plane equation
    a, b, c, d = plane_normal

    # Generate points for the plane
    x = np.linspace(-10, 10, 100)
    y = np.linspace(-10, 10, 100)
    X, Y = np.meshgrid(x, y)
    Z = (-d - a * X - b * Y) / c

    # Plot the plane
    plt.plot_surface(X, Y, Z, alpha=0.5)

    # Plot the normal vector
    origin = np.array([0, 0, 0])
    end_point = np.array([a, b, c])
    plt.quiver(origin[0], origin[1], origin[2], end_point[0], end_point[1], end_point[2], color='red')

    # Calculate direction cosines
    direction_cosines = plane_normal / np.linalg.norm(plane_normal)

    # Label direction cosines below the arrow
    x_label = f"x: {direction_cosines[0]:.3f}"
    y_label = f"y: {direction_cosines[1]:.3f}"
    z_label = f"z: {direction_cosines[2]:.3f}"
    plt.text(end_point[0] + 0.5, end_point[1] - 0.5, end_point[2] + 0.5,
             f"{x_label}\n{y_label}\n{z_label}",
             ha='center', va='center')

    plt.xlabel('x')
    plt.ylabel('y')
    plt.zlabel('z')
    plt.show()

# Load input parameters from the text file
with open("plane_data.txt", "r") as file:
    line = file.readline()
    plane_normal = np.array(list(map(float, line.split())))

# Calculate direction cosines using matrix method
direction_cosines = plane_normal / np.linalg.norm(plane_normal)

print("Direction cosines of the normal vector:", direction_cosines)

# Plot the plane and normal vector
plot_plane_and_normal(plane_normal)
