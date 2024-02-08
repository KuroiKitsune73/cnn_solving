import numpy as np
import matplotlib.pyplot as plt
def gradient_descent_step(x, y, learning_rate):
# Partial derivative functions
    df_dx = 2*x+y
    df_dy = x+2*y
    # Update x and y
    x_new = x-learning_rate*df_dx
    y_new = y-learning_rate*df_dy
    return x_new, y_new
# Input
x = 1.3
y = 5.4
learning_rate = 0.01
# Function
xi = np.arange(0, 2, 0.1)
yi = np.arange(0, 2, 0.1)
f=xi**2 + xi*yi + yi**2
# 1step SGD
x_new, y_new = gradient_descent_step(x, y, learning_rate)
# Output
plt.figure(figsize=(10, 10))
plt.plot(f)
plt.scatter(x_new, y_new)
plt.grid()
plt.title('Local minimum')
plt.xlabel("X")
plt.ylabel("Y")
plt.text(0,10,f"1st step SGD:\nx={x_new}\ny={y_new}", fontsize=8)
plt.show()