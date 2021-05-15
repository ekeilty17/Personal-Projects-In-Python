from matrix_lib import *
from vector_lib import *

def vector_list_to_matrix(L):
    if type(L) != list:
        raise TypeError("Arguement is not list.")

    first = len(L[0].store)
    for v in L:
        if not isinstance(v, Vector):
            raise TypeError("List is not comprised of vectors.")
            return None
        if len(v.store) != first:
            raise TypeError("Vectors are not all the same length.")
            return None

    out = []
    for c in range(len(L[0].store)):
        temp = []
        for r in range(len(L)):
            temp += [L[r].store[c]]
        out += [temp]
    return Matrix(out)

def matrix_to_list_vectors(A):
    if not isinstance(A, Matrix):
        raise TypeError("Argument is not a matrix.")
        return None

    out = []
    for c in range(len(A.store[0])):
        temp = []
        for r in range(len(A.store)):
            temp += [A.store[r][c]]
        out += [Vector(temp)]
    return out

def vector_to_matrix(v):
    if not isinstance(v, Vector):
        raise TypeError("Arguement is not a vector.")
        return None
    out = []
    for x in v.store:
        out += [[x]]
    return Matrix(out)

def matrix_to_vector(A):
    if not isinstance(A, Matrix):
        raise TypeError("Arguement is not a matrix.")
        return None
    if len(A.store[0]) != 1:
        raise TypeError("Cannot convert a matrix with >1 cols into a col vector.")
        return None
    out = []
    for r in range(len(A.store)):
        out += [A.store[r][0]]
    return Vector(out)

def matrix_vector_multiply(A, v):
    if not isinstance(A, Matrix):
        raise TypeError("First argument is not a Matrix.")
        return None
    if not isinstance(v, Vector):
        raise TypeError("Second arguement is not a Vector.")
        return None
    return matrix_to_vector(multiply(A, vector_to_matrix(v)))
