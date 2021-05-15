from matrix import *

weights = [2, 1, 3]

estimated = Matrix([    [80, 150, 200],
                        [1.2, 0.6, 1],
                        [3.2, 2.1, 1.4]])

utility =   Matrix([    [0.85, 0.50, 0.3],
                        [0.50, 0.95, 0.7],
                        [0.92, 0.70, 0.3]])

def UtilityFunctions(w, est, util):
    
    weighted_sum = []
    for i in range(len(est[0])):
        row = util.getRow(i+1)
        for i in range(w):
            weighted_sum += [w[i] * util[i]]
    
    return 

print estimated
print
print utility
