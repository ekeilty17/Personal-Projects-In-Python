import numpy as np
import matplotlib.pyplot as plt
import math

# n = 2 --> Euler's Method
# n = 4 --> RK4
def Taylor(A, t0, tn, X0, dt, n):
    # Initialize variables
    N = int((tn - t0)/dt)
    M = len(X0)
    T = np.zeros(N+1)
    X = np.zeros((M, N+1))

    # Initial Value
    T[0] = t0
    X[:,0] = X0
    
    # M = (I + dt*A + ... + dt^k/k! * A^k)
    A_k = np.identity(A.shape[0])
    M = np.zeros(A.shape)
    for k in range(n):
        M += (dt**k / math.factorial(k)) * A_k
        A_k = np.matmul(A, A_k)

    for i in range(N):
        # t_n+1 = t_n + dt
        T[i+1] = T[i] + dt
        # X_n+1 = (I + dt*A + ... + dt^k/k! * A^k) * X_n
        X[:,i+1] = X[:,i].dot(M)
        
    return [T, X]


A = np.matrix([[-4, 5, -3], [-17/3, 4/3, 7/3], [23/3, -25/3, -4/3]])
X0 = np.array([10, -30, 20])

[T, X] = Taylor(A, 0, 4, X0, 0.01, 4)

# Plotting
for i in range(X.shape[0]):
    plt.plot(T, X[i,:], label='x' + str(i+1) + '(t)')
plt.legend()
plt.xlabel('t')
plt.ylabel('X(t)')
plt.show()
