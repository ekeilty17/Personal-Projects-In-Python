import numpy as np
import matplotlib.pyplot as plt
import math

def Improved_Euler(f, t0, tn, y0, dt):

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

        # Normal Euler's Method Step
        y_euler = Y[i] + dt * f(T[i], Y[i])
        
        # y_n+1 = y_n + 1/2 * dt * [ y'(t_n+1, y_n+1) + y'(t_n, y_n) ]
        Y[i+1] = Y[i] + 0.5*dt*( f(T[i+1], y_euler) + f(T[i], Y[i]) )

    return [T, Y]

def y_prime(t, y):
    #return 2*t*( 1 - y**2 )**0.5
    r = 30
    k = 100
    A = 400
    return r*y*(1 - y/float(k)) - A*(1 - math.cos(2*math.pi*t))    

[T, Y] = Improved_Euler(y_prime, 0, 10, 50, 0.05)

plt.plot(T, Y)
plt.xlabel('t')
plt.ylabel('y(t)')
plt.show()
