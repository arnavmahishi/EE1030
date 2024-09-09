import matplotlib.pyplot as plt

# Define the coordinates of points P, A, and B
point_P = (2, 4)
point_A = (5, 3)
point_B = (3, 7)

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
