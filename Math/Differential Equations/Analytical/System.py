import numpy as np
from sympy import *

#x' = Ax + b
def System_ConstantCoefficients(A, b):
    
    # Finding equilibrium equation
    x_eq = -1 * np.linalg.inv(A).dot(b)
    
    print(x_eq)
    print()
    L, v = np.linalg.eig(A)
    print(L)
    print(v)
    print()
    y = 0
    for i in range(A.shape[0]):
        print(L[i])
        print(v[:,i])
        print()

A = np.matrix([[2, 1], [1, 2]])
b = np.array([0, 0])
System_ConstantCoefficients(A, b)
