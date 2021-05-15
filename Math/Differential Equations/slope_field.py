import numpy as np
import matplotlib.pyplot as plt

# ODE you want to graph the slope field of
def y_prime(x, y):
    return np.sin(y)*np.cos(y)

# x-axis
a_x = 0
b_x = 20
# y-axis
a_y = -5
b_y = 5

partitions = 20

# Setting up Grid
X, Y = np.meshgrid(np.linspace(a_x, b_x, partitions), np.linspace(a_y, b_y, partitions))

# Initializing slope variables
U, V = np.zeros(X.shape), np.zeros(Y.shape)

NI, NJ = X.shape
for i in range(NI):
    for j in range(NJ):
        U[i,j] = 1
        V[i,j] = y_prime(X[i, j], Y[i, j])


# Normalize the arrows
U /= np.sqrt(U**2 + V**2);
V /= np.sqrt(U**2 + V**2);

Q = plt.quiver(X, Y, U, V, color='b')

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.xlim([a_x, b_x])
plt.ylim([a_y, b_y])
plt.show()
