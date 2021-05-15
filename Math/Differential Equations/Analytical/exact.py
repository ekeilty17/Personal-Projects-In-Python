from sympy import *

#N + My' = 0
def exact(N, M, x, y):
    
    if diff(N, y) != diff(M, x):
        return "Can't be done"
    
    
    
