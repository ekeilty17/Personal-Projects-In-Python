import numpy as np
import matplotlib.pyplot as plt

def Euler(F, t0, tn, X0, dt):
    # Initialize variables
    N = int((tn - t0)/dt)
    M = len(X0)
    T = np.zeros(N+1)
    X = np.zeros((M, N+1))

    # Initial Value
    T[0] = t0
    X[:,0] = X0

    for i in range(N):
        # t_n+1 = t_n + dt
        T[i+1] = T[i] + dt
        # X_n+1 = X_n + dt * A*X_n
        X[:,i+1] = X[:,i] + dt * F(T[i], X[:,i])
    return [T, X]

def Improved_Euler(F, t0, tn, X0, dt):
    # Initialize variables
    N = int((tn - t0)/dt)
    M = len(X0)
    T = np.zeros(N+1)
    X = np.zeros((M, N+1))

    # Initial Value
    T[0] = t0
    X[:,0] = X0
    for i in range(N):
        # t_n+1 = t_n + dt
        T[i+1] = T[i] + dt

        # Normal Euler's Method Step
        X_euler = X[:,i] + dt * F(T[i], X[:,i])

        # X_n+1 = X_n + 1/2 * dt * [ f(t_n+1, X_n+1) + f(t_n, X_n) ]
        X[:,i+1] = X[:,i] + 0.5*dt*( F(T[i+1], X_euler) + F(T[i], X[:,i]) )

    return [T, X]

def RK4(F, t0, tn, X0, dt):
    # Initialize variables
    N = int((tn - t0)/dt)
    M = len(X0)
    T = np.zeros(N+1)
    X = np.zeros((M, N+1))

    # Initial Value
    T[0] = t0
    X[:,0] = X0

    for i in range(N):
        # t_n+1 = t_n + dt
        T[i+1] = T[i] + dt

        # K_n1 = f(t_n, y_n)
        K1 = F(T[i], X[:,i])
        # K_n2 = f(t_n + dt/2, y_n + dt/2 * K_n1)
        K2 = F(T[i] + 0.5*dt, X[:,i] + 0.5*dt*K1)
        # K_n3 = f(t_n + dt/2, y_n + dt/2 * K_n2)
        K3 = F(T[i] + 0.5*dt, X[:,i] + 0.5*dt*K2)
        # K_n4 = f(t_n + dt, y_n + dt * K_n3)
        K4 = F(T[i] + dt, X[:,i] + dt*K3)

        # X_n+1 = X_n + dt/6 * ( K_n1 + 2*K_n2 + 2*K_n3 + K_n4)
        X[:,i+1] = X[:,i] + (dt/6)*(K1 + 2*K2 + 2*K3 + K4)


    return [T, X]

def F(t, X):
    A = np.matrix([[-4, 5, -3], [-17/3, 4/3, 7/3], [23/3, -25/3, -4/3]])
    return X.dot(A)

X0 = np.array([10, -30, 20])

#[T, X] = Euler(f, 0, 4, X0, 0.01)
[T, X] = Improved_Euler(F, 0, 4, X0, 0.01)
#[T, X] = RK4(f, 0, 4, X0, 0.01)

# Plotting
for i in range(X.shape[0]):
    plt.plot(T, X[i,:], label='x' + str(i+1) + '(t)')
plt.legend()
plt.xlabel('t')
plt.ylabel('X(t)')
plt.show()
