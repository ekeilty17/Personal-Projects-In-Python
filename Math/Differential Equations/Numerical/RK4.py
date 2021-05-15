import numpy as np
import matplotlib.pyplot as plt
import math

def RK4(f, t0, tn, y0, dt):

    # Initialize variables
    N = int((tn - t0)/dt)
    T = np.zeros(N+1)
    Y = np.zeros(N+1)

    # Initial Value
    T[0] = t0
    Y[0] = y0
    for i in range(N):
        # t_n+1 = t_n + dt
        T[i+1] = T[i] + dt
        
        # K_n1 = f(t_n, y_n)
        K1 = f(T[i], Y[i])
        # K_n2 = f(t_n + dt/2, y_n + dt/2 * K_n1)
        K2 = f(T[i] + 0.5*dt, Y[i] + 0.5*dt*K1)
        # K_n3 = f(t_n + dt/2, y_n + dt/2 * K_n2)
        K3 = f(T[i] + 0.5*dt, Y[i] + 0.5*dt*K2)
        # K_n4 = f(t_n + dt, y_n + dt * K_n3)
        K4 = f(T[i] + dt, Y[i] + dt*K3)

        # y_n+1 = y_n + dt/6 * ( K_n1 + 2*K_n2 + 2*K_n3 + K_n4)
        Y[i+1] = Y[i] + (dt/6)*(K1 + 2*K2 + 2*K3 + K4)

    return [T, Y]

def y_prime(t, y):
    return (5*t**2 - y)/(math.exp(t+y))
    #return 2*t*( 1 - y**2 )**0.5

[T, Y] = RK4(y_prime, 0, 1, 1, 0.01)

plt.plot(T, Y)
plt.xlabel('t')
plt.ylabel('y(t)')
plt.show()
