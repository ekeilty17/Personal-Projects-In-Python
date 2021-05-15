import numpy as np
import matplotlib.pyplot as plt
import math

def Euler(f, t0, tn, y0, dt):
    
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
        # y_n+1 = y_n + dt * f(t_n, y_n)
        Y[i+1] = Y[i] + dt * f(T[i], Y[i])
    
    return [T, Y]

def y_prime(t, y):
    #return 2*t*( 1 - y**2 )**0.5
    r = 3
    k = 100
    A = k/float(r)
    return r*y*(1 - y/float(k)) - A*(1 - math.cos(2*math.pi*t))

[T, Y] = Euler(y_prime, 0, 10, 50, 0.01)

plt.plot(T, Y)
plt.xlabel('t')
plt.ylabel('y(t)')
plt.show()
