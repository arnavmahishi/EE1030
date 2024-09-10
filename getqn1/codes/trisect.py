import matplotlib.pyplot as plt

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
