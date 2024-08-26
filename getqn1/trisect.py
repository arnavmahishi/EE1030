import matplotlib.pyplot as plt

def plot_coordinates(filename):
    """Plots coordinates from a text file.

    Args:
        filename: The name of the text file containing coordinates.
    """
    coordinates = {}
    with open(filename, 'r') as f:
        for line in f:
            point_name, coords_str = line.strip().split(': ')
            coords = tuple(map(int, coords_str.strip('()').split(',')))
            coordinates[point_name] = coords

    # Extract x and y values
    x_values = [coord[0] for coord in coordinates.values()]
    y_values = [coord[1] for coord in coordinates.values()]

    # Plot the points
    plt.scatter(x_values, y_values)

    # Draw a line through the points
    plt.plot(x_values, y_values, linestyle='-', color='red')

    # Add labels and title
    plt.xlabel("X-coordinate")
    plt.ylabel("Y-coordinate")
    plt.title("Coordinates Plot")

    # Annotate points with labels and coordinates
    for point_name, (x, y) in coordinates.items():
        plt.annotate(f"{point_name} ({x}, {y})", (x, y), textcoords="offset points", xytext=(0, 10), ha="center")

    plt.show()

# Replace 'coordinates.txt' with your actual file name
plot_coordinates('coordinates.txt')
