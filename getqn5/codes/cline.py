import matplotlib.pyplot as plt

# Read data from the text file
with open('line_data.txt', 'r') as file:
    data = file.readline()

# Extract x and y values
x_values = []
y_values = []
x, y = map(int, data.split(','))
x_values.append(x)
y_values.append(y)

# Plot the data with a thicker blue line
plt.plot(x_values, y_values, color='blue', linewidth=3)

# Annotate the points

plt.annotate(f'P{i}\n({x_values[i]}, {y_values[i]})', (x_values[0], y_values[0]), xytext=(0, -10), textcoords='offset points', ha='center', va='top')

# Add labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Plot of Data from Text File')

# Display the plot
plt.grid(True)
plt.show()
