import numpy as np
import matplotlib.pyplot as plt

def Euler_AdaptiveStep(f, t0, tn, y0, dt, tol):
    
    # Initialize variables
    T = np.zeros(2)
    Y = np.zeros(2)
    
    # Since we have a variable step size, dt is not constant
    # Since it's bad practice to modify input variabels, using h
    h = dt

    # Initial Value
    T[0] = t0
    Y[0] = y0

    # Can't use a simple for loop becuase there's not way of calculating apriori
    # how many steps the approximation will take
    i = 0
    while T[i] <= tn:
        
        # Regular Euler's Method step
        T[i+1] = T[i] + h
        Y[i+1] = Y[i] + h * f(T[i], Y[i])

        # Two successive Euler's Method half steps
        z = Y[i] + (h/2) * f(T[i], Y[i])
        z = z + (h/2) * f(T[i] + dt/2, z)
        
        # Error estimate
        D = abs(Y[i+1] - z)
        if D < tol:
            T = np.append(T, [0])
            Y = np.append(Y, [0])
            i += 1
        
        # resetting the step size
        h = 0.9 * h * min( max( tol/D, 0.3 ), 2 );

    # Last elements will be zeros, so we need to remove those
    return [T[:-1], Y[:-1]]



def y_prime(t, y):
    return 2*t*( 1 - y**2 )**0.5

[T, Y] = Euler_AdaptiveStep(y_prime, 0, 0.75, 0, 0.025, 10**-4)

plt.plot(T, Y)
plt.xlabel('t')
plt.ylabel('y(t)')
plt.show()
