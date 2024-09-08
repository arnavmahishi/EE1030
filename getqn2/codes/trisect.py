import matplotlib.pyplot as plt
import numpy as np

def read_points(filename):
    """Reads points from a text file and returns them as a list of tuples.

    Args:
        filename: The name of the text file.

    Returns:
        A list of tuples, where each tuple represents a point (x, y).
    """

    with open(filename, 'r') as f:
        points = [(float(x), float(y)) for line in f for x, y in [line.split()]]
    return points

def plot_points(points, labels):
    """Plots the points with labels and lines connecting A and B to P.

    Args:
        points: A list of tuples representing points (x, y).
        labels: A list of labels for each point.
    """

    x, y = zip(*points)  # Unpack coordinates into separate arrays

    plt.figure(figsize=(8, 6))
    plt.scatter(x, y, color='blue', marker='o')

    # Label the points using a list comprehension
    for i, (px, py) in enumerate(points):
        plt.text(px, py, f"P{i+1} ({px:.2f}, {py:.2f})", ha='center', va='bottom')

    # Connect points A and B to P
    plt.plot([points[0][0], points[1][0], points[2][0]],
             [points[0][1], points[1][1], points[2][1]],
             color='red', linestyle='-', linewidth=2)

    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Plot of Points')

    plt.show()

if __name__ == '__main__':
    filename = 'points.txt'
    points = read_points(filename)
    labels = [f"P{i+1}" for i in range(len(points))]
    plot_points(points, labels)
