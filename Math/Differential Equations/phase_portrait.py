import numpy as np
import matplotlib.pyplot as plt

A = [[1, 2], [2, 1]]
G = [0, 0]
def f(Y, t):
    return [ A[0][0]*Y[0] + A[0][1]*Y[1] + G[0],
             A[1][0]*Y[0] + A[1][1]*Y[1] + G[0]
            ]

# x-axis
a_x = -5
b_x = 5
# y-axis
a_y = -5
b_y = 5

partitions = 20

# Setting up Grid
Y1, Y2 = np.meshgrid(np.linspace(a_x, b_x, partitions), np.linspace(a_y, b_y, partitions))


# Initializing slope variables
U, V = np.zeros(Y1.shape), np.zeros(Y2.shape)

t = 0
NI, NJ = Y1.shape
for i in range(NI):
    for j in range(NJ):
        U[i,j], V[i,j] = f([Y1[i, j], Y2[i, j]], t)
        #U[i,j] = Yprime[0]
        #V[i,j] = Yprime[1]
        

# Normalize the arrows
U /= np.sqrt(U**2 + V**2);
V /= np.sqrt(U**2 + V**2);

# plotting eigenvectors
L, v = np.linalg.eig(A)
x = np.linspace(a_x, b_x, 10)
print(v)
print((v[0][1]/v[0][0]))
print(v[1][1]/v[1][0])
plt.plot(x, (v[0][1]/v[0][0])*(x - G[0]) + G[1], color='0.75')
plt.plot(x, (v[1][1]/v[1][0])*(x - G[0]) + G[1], color='0.75')

# plitting direction field
Q = plt.quiver(Y1, Y2, U, V, color='k')

# plotting streamlines
plt.streamplot(Y1, Y2, U, V, density=0.5, color='b')


plt.xlabel('$y_1$')
plt.ylabel('$y_2$')
plt.xlim([a_x, b_x])
plt.ylim([a_y, b_y])
plt.show()
