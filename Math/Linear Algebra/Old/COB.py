from CoordinateSystem import *
from vector import *
from matrix import *
from sympy import *
import sys

#If you have another basis, this creates a COB matrix that takes a vector in the standard basis
#to the basis E provided
#e is a list of basis vectors
def COB_matrx_standard(e):
    #Error Checks
    #   To check that e is a basis we need to check the following
    #   since I can't know the span since I don't know the vector space 
    #       I need to take advantage of the dimesnion and linear independents
    #   If we were to make a matrix out of the basis e or f, then it needs to be a square matrix
    #   e needs to be LI
    #
    #   So by a theorem, the dim of e and the stard basis are equal and vectors in e are LI, 
    #       therefore e is a basis
    for i in range(len(e)):
        if not isinstance(e[i], Vector):
            raise TypeError("Bases are not comprised of vectors.")
            return None
        elif len(e) != len(e[i].store):
            raise TypeError("The number of elements in the coordinate vector needs to be equal to the dimensino of the vector space.")
            return None
    """
    if not (LI(e) and LI(f)):
        raise TypeError("Bases must be Linearly Independent.")
        return None
    """
    
    return vector_list_to_matrix(e).Inverse()


#e is a list of the coordinates vectors of basis E written in the standard basis
#f is a list of the coordinates vectors of basis F written in the standard basis
#   e & f are a list of vectors objects
#   It's weird bc v.store look like row vectors, but they are actually col vectors
def COB_matrix(e,f):
    
    if len(e) != len(f):
        raise TypeError("Bases must have same length.")
        return None
   
    S_e = COB_matrix_standard(e)
    S_f = COB_matrix_standard(f)
    
    #we are getting COB matrix from the BASIS f to the BASIS e
    #    Note: if it was from a vector in f to a vector in e, then it would be the above inverse
    return multiply(S_f, S_e.Inverse())
    #return multiply(S_f, vector_list_to_matrix(e))

def COB_LT(T, e1, e2, f1, f2):
    #T is some transformation that takes a vector in e1 and produces a vector in e2
    #we want to write it so it takes a vector in f1 and produces an vector in f2
    return multiply_list( [ COB_matrix(e2,f2), T, COB_matrix(f1, e1) ] ) 

e1 = Vector([1, 0, 0])
e2 = Vector([1, 1, 0])
e3 = Vector([1, 1, 1])

f1 = Vector([1, 1, 1])
f2 = Vector([1, 1, 0])
f3 = Vector([1, 0, 0])

v = Vector([-2, 6, -1])     #written in basis e

P = COB([e1, e2, e3], [f1, f2, f3])
print P.get()
print
print v.get()
print
print matrix_vector_multiply(P, v).get()
