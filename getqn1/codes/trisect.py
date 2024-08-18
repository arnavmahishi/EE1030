import matplotlib.pyplot as plt

def trisection_points(a, b):
  """
  Calculates the trisection points of a line segment defined by points a and b.

  Args:
    a: The first point as a tuple (x, y).
    b: The second point as a tuple (x, y).

  Returns:
    A tuple containing the two trisection points (p, r).
  """

  x1, y1 = a
  x2, y2 = b

  # Calculate the coordinates of the trisection points using the section formula
  px = (2*x1 + x2) / 3
  py = (2*y1 + y2) / 3
  rx = (x1 + 2*x2) / 3
  ry = (y1 + 2*y2) / 3

  return (px, py), (rx, ry)

def plot_line_and_points(a, b, p, r):
  """
  Plots the line segment defined by points a and b, and the trisection points p and r with labels.

  Args:
    a: The first point as a tuple (x, y).
    b: The second point as a tuple (x, y).
    p: The first trisection point as a tuple (x, y).
    r: The second trisection point as a tuple (x, y).
  """

  x_values = [a[0], b[0]]
  y_values = [a[1], b[1]]

  plt.plot(x_values, y_values)
  plt.scatter([a[0], b[0], p[0], r[0]], [a[1], b[1], p[1], r[1]])

  # Add labels for each point
  plt.text(a[0], a[1], f'A({a[0]}, {a[1]})')
  plt.text(b[0], b[1], f'B({b[0]}, {b[1]})')
  plt.text(p[0], p[1], f'P({p[0]}, {p[1]})')
  plt.text(r[0], r[1], f'R({r[0]}, {r[1]})')

  plt.xlabel('x')
  plt.ylabel('y')
  plt.grid(True)
  plt.show()

# Example usage
a = (7, -2)
b = (1, -5)
p, r = trisection_points(a, b)
print("Trisection points:", p, r)
plot_line_and_points(a, b, p, r)
