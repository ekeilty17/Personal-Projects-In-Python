from matrix import *
import numpy as np
from numpy import linalg as LA

def MakeReciprocle(RP_List, RI):
    
    N = RP_List[0].dim()[0]
    for RP in RP_List:
        for i in range(N):
            for j in range(i, N):
                RP[j][i] = 1.0/RP[i][j]
    
    P = RI.dim()[0]
    for i in range(P):
        for j in range(P):
            RI[j][i] = 1.0/RI[i][j]


def DecisionValue(RP_List, RI):
    
    # Filling in reciprocle values
    MakeReciprocle(RP_List, RI)
   

    """ Relative Preference Matrices"""
    
    # All RP matrices should be square and the same dimensions
    N = RP_List[0].dim()[0]
   
    # Creating copies so I don't change the values of the original matrices
    RP_List_norm = []
    for RP in RP_List:
        RP_List_norm += [RP.copy()]
    
    # Normalizing Columns for each objective
    for p in range(len(RP_List_norm)):
        RP = RP_List_norm[p]
        for i in range(N):
            for j in range(N):
                RP_List_norm[p][i][j] /= sum(RP.getCol(j+1))

    # Overall Prefernce Rating
    preference_rating = []
    for RP_norm in RP_List_norm:
        temp = []
        for i in range(N):
            temp += [sum(RP_norm.getRow(i+1)) / N]
        preference_rating += [temp]
    
    
    
    """ Relative Importance Matrices""" 
    
    P = RI.dim()[0]
    
    # Creating copies so I don't change the values of the original matrix
    RI_norm = RI.copy()
    
    # Normalizing Columns for each objective
    for i in range(P):
        for j in range(P):
            RI_norm[i][j] /= sum(RI.getCol(j+1))
    
    # Overall Importance Rating
    importance_rating = []
    for i in range(P):
        importance_rating += [sum(RI_norm.getRow(i+1)) / P]
    
    
    # Decision Value
    D = []
    for s_i in range(N):
        d = 0
        for t in range(P):
            d += importance_rating[t] * preference_rating[t][s_i]
        D += [d]

    return D

def ConsistencyMeasure(RP_List, RI):
    
    # Initialize output values
    CR_RP = []
    CR_RI = 1

    # Consistency Index for a random for different sized matrices
    CI_R = { 2 : 0.00,
             3 : 0.52,
             4 : 0.90,
             5 : 1.12,
             6 : 1.24,
             7 : 1.32,
             8 : 1.41}    

    """ Relative Preference Matrices"""

    # All RP matrices should be square and the same dimensions
    N = RP_List[0].dim()[0]

    for RP in RP_List:
        L, v = LA.eig(np.array( RP.L ))
        
        CI = (max(L).real - N) / float(N - 1)
        CR_RP += [CI / CI_R[N]]
    
    """ Relative Importance Matrices"""

    P = RI.dim()[0]

    L, v = LA.eig(np.array( RI.L ))
    CI = (max(L).real - P) / float(P - 1)
    CR_RI = CI / CI_R[P]

    return [CR_RP, CR_RI]

def AHP(RP_List, RI):
    
    D = DecisionValue(RP_List, RI)
    [CR_RP, CR_RI] = ConsistencyMeasure(RP_List, RI)

    # Just so things print nicely
    for RP in RP_List:
        RP.setAccuracy(3)

    RI.setAccuracy(3)

    print
    print "Relative Preference Matrices"
    print
    for p in range(len(RP_List)):
        print "Objective " + str(p+1)
        print "Consistency:", CR_RP[p]
        print RP_List[p]
        print
    print
    print "Relative Importance Matrix"
    print
    print "Consistency:", CR_RI
    print RI
    print
    print "Decision Values"
    for i in range(len(D)):
        print "Solution " + str(i+1) + ": " + str(D[i])
    print

# Cost
Pos1 = Matrix( [[1, 1.0/6, 1.0/2], 
                [0, 1, 7], 
                [0, 0, 1]])

# Size
Pos2 = Matrix( [[1, 1.0/5, 1.0/5],
                [0, 1, 1],
                [0, 0, 1]])

# Weight
Pos3 = Matrix( [[1, 1.0/5, 1],
                [0, 1, 5],
                [0, 0, 1]])

# Time
Pos4 = Matrix( [[1, 1, 1],
                [0, 1, 1],
                [0, 0, 1]])

# Ease
Pos5 = Matrix( [[1, 1, 1],
                [0, 1, 1],
                [0, 0, 1]])

# Accuracy and Correctness
Pos6 = Matrix( [[1, 3, 4],
                [0, 1, 2],
                [0, 0, 1]])

# Simplicity
Pos7 = Matrix( [[1, 1.0/3, 1],
                [0, 1, 3],
                [0, 0, 1]])

# Cost
Dep1 = Matrix([     [1,     4,      1,      2,      2,      1.0/3],
                    [0,     1,      1.0/7,  1.0/4,  1.0/4,  1.0/9],
                    [0,     0,      1,      2,      2,      1.0/3],
                    [0,     0,      0,      1,      1,      1.0/4],
                    [0,     0,      0,      0,      1,      1.0/4],
                    [0,     0,      0,      0,      0,      1]])

# Size
Dep2 = Matrix([     [1,     1.0/5,  1.0/5,  1.0/5,  1.0/5,  1.0/7],
                    [0,     1,      1,      1,      1,      1.0/3],
                    [0,     0,      1,      2,      2,      1.0/3],
                    [0,     0,      0,      1,      1,      1.0/2],
                    [0,     0,      0,      0,      1,      1.0/2],
                    [0,     0,      0,      0,      0,      1]])

# Weight
Dep3 = Matrix([     [1,     1.0/3,  1.0/5,  1.0/4,  1.0/4,  1.0/7],
                    [0,     1,      1.0/3,  1.0/2,  1.0/2,  1.0/5],
                    [0,     0,      1,      2,      2,      1.0/2],
                    [0,     0,      0,      1,      1,      1.0/3],
                    [0,     0,      0,      0,      1,      1.0/3],
                    [0,     0,      0,      0,      0,      1]])

# TIme
Dep4 = Matrix([     [1,     4,      1.0/2,  2,      2,      1],
                    [0,     1,      1.0/6,  1.0/5,  1.0/5,  1.0/4],
                    [0,     0,      1,      4,      4,      2],
                    [0,     0,      0,      1,      1,      1.0/2],
                    [0,     0,      0,      0,      1,      1.0/2],
                    [0,     0,      0,      0,      0,      1]])

# Ease
Dep5 = Matrix([     [1,     1.0/4,  1.0/4,  1.0/4,  1.0/4,  1.0/4],
                    [0,     1,      1,      1,      1,      1],
                    [0,     0,      1,      1,      1,      1],
                    [0,     0,      0,      1,      1,      1],
                    [0,     0,      0,      0,      1,      1],
                    [0,     0,      0,      0,      0,      1]])

# Accuracy and Correctness
Dep6 = Matrix([     [1,     1,      5,      3,      3,      1],
                    [0,     1,      5,      3,      3,      1],
                    [0,     0,      1,      1.0/3,  1.0/3,  1.0/5],
                    [0,     0,      0,      1,      1,      1.0/3],
                    [0,     0,      0,      0,      1,      1.0/3],
                    [0,     0,      0,      0,      0,      1]])

# Simplicity
Dep7 = Matrix([     [1,     2,      1.0/4,  1.0/3,  1.0/3,  1.0/6],
                    [0,     1,      1.0/5,  1.0/4,  1.0/4,  1.0/7],
                    [0,     0,      1,      3,      3,      1.0/4],
                    [0,     0,      0,      1,      1,      1.0/5],
                    [0,     0,      0,      0,      1,      1.0/5],
                    [0,     0,      0,      0,      0,      1]])

RI = Matrix( [  [1,     1,      1,      1,      1.0/2,  1.0/5,  1.0/5], 
                [0,     1,      1,      1.0/2,  1.0/2,  1.0/5,  1.0/5], 
                [0,     0,      1,      1.0/2,  1.0/2,  1.0/5,  1.0/5],
                [0,     0,      0,      1,      1,      1.0/3,  1.0/3],
                [0,     0,      0,      0,      1,      1.0/3,  1.0/3],
                [0,     0,      0,      0,      0,      1,      1],
                [0,     0,      0,      0,      0,      0,      1]])

AHP([Pos1, Pos2, Pos3, Pos4, Pos5, Pos6, Pos7], RI)
print
print
print
AHP([Dep1, Dep2, Dep3, Dep4, Dep5, Dep6, Dep7], RI)
