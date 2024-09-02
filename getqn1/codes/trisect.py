import matplotlib.pyplot as plt

def plot_coordinates(filename):
    """Plots coordinates from a text file.

    Args:
        filename: The name of the text file containing coordinates.
    """
    with open(filename, 'r') as f:
        data = list(map(lambda line: line.strip().split(': '), f))

    # Extract point names and coordinates
    point_names, coords_str = zip(*data)
    coordinates = dict(zip(point_names, map(lambda s: tuple(map(int, s.split(',')[1:-1])), coords_str)))

    # Extract x and y values
    x_values, y_values = zip(*coordinates.values())

    # Plot the points
    plt.scatter(x_values, y_values)

    # Draw a line through the points
    plt.plot(x_values, y_values, linestyle='-', color='red')

    # Add labels and title
    plt.xlabel("X-coordinate")
    plt.ylabel("Y-coordinate")
    plt.title("Coordinates Plot")

    # Annotate points with labels and coordinates
    annotations = [plt.annotate(f"{point_name} ({x}, {y})", (x, y), textcoords="offset points", xytext=(0, 10), ha="center") for point_name, (x, y) in coordinates.items()]

    plt.show()

# Replace 'coordinates.txt' with your actual file name
plot_coordinates('coordinates.txt')
