import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import math
# Define the function f(x, y) = x² + xy + y²
def f(x, y):
    return x*x + x*y + y*y
# Define the partial derivatives of f with respect to x and y
def df_dx(x, y):
    return 2*x + y
def df_dy(x, y):
    return x + 2*y

# Gradient descent function
def gradient_descent(x, y, learning_rate):
    x_new = x - learning_rate * df_dx(x, y)
    y_new = y - learning_rate * df_dy(x, y)
    return x_new, y_new

# Initial values
x_start, y_start = 1.3, 5.4
learning_rate = 0.01

# Perform the first step of gradient descent
x_new, y_new = gradient_descent(x_start, y_start, learning_rate)

# Print the results
print(f"Initial values: x = {x_start}, y = {y_start}")
print(f"Gradient descent step: x_new = {x_new}, y_new = {y_new}")

# Create a meshgrid for 3D plot
x_vals = np.linspace(-6, 6, 100)
y_vals = np.linspace(-6, 6, 100)
X, Y = np.meshgrid(x_vals, y_vals)
Z = f(X, Y)

# Plot the 3D surface of the source function
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.4, edgecolor='k')

# Plot the point of the initial values
ax.scatter(x_start, y_start, f(x_start, y_start), color='red', label='Initial Point')

# Plot the point after the first step of gradient descent
ax.scatter(x_new, y_new, f(x_new, y_new), color='blue', label='After 1st Step')

# Set labels and legend
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('f(X, Y)')
ax.legend()

# Show the plot
plt.show()