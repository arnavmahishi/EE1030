import numpy as np
import matplotlib.pyplot as plt

def plot_coordinates(filename):
    """Plots coordinates from a text file, highlighting point "P" in red.

    Args:
        filename: The name of the text file containing coordinates.
    """

    with open(filename, 'r') as f:
        coordinates = {
            line.strip().split(': ')[0]: tuple(map(int, line.strip().split(': ')[1].strip('()').split(',')))
            for line in f
        }

    # Extract x and y values
    x_values, y_values = zip(*coordinates.values())

    # Create NumPy arrays (if needed for other calculations)
    # x_array = np.array(x_values)
    # y_array = np.array(y_values)

    # Plot the points
    plt.scatter(x_values, y_values, color='blue')

    # Plot point "P" in red (if it exists)
    if "P" in coordinates:
        x_p, y_p = coordinates["P"]
        plt.scatter(x_p, y_p, color='red', marker='x', s=100)

    # Draw a line through the points
    plt.plot(x_values, y_values, linestyle='-', color='red')

    # Add grid lines
    plt.grid(True)

    # Add labels and title
    plt.xlabel("X-coordinate")
    plt.ylabel("Y-coordinate")
    plt.title("Coordinates Plot")

    # Annotate points using list comprehension with zip
    annotations = [plt.annotate(f"{name} ({x}, {y})", (x, y), textcoords="offset points", xytext=(0, 10), ha="center")
                   for name, (x, y) in coordinates.items()]

    plt.show()

# Replace 'coordinates.txt' with your actual file name
plot_coordinates('coordinates.txt')
