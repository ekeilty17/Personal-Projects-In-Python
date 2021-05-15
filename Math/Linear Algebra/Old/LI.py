from vector_lib import *
from matrix_lib import *
from vector_matrix_lib import *
from matrix_prop import *
from GE import *

def LI(L):
    
    if type(L) != list:
        raise TypeError("Input is not a list.")
        return False
    first = len(L[0].store)
    for v in L:
        if not isinstance(v, Vector):
            raise TypeError("Input is not a list of vectors.")
            return False
        if len(v.store) != first:
            raise TypeError("Vectors are not the same length.")
            return False

    #if there are more vectors than dimensions in the vector space
    #Then they cannot be LI
    if len(L) > len(L[0].store):
        return False
    
    #get matrix into RREF
    M = ge( vector_list_to_matrix(L), vector_to_matrix(Vector([0]*len(L[0].store))) )

    #remove the augmented part
    M.deleteCol(M.dim()[1])
    
    #removing zero rows
    for i in range(M.dim()[0]):
        if M.getRow(i+1) == [0]*M.dim()[1]:
            M.deleteRow(i+1)
    
    if M.store == I(M.dim()[0]).store:
        return True
    return False

v1 = Vector([1,1,1])
v2 = Vector([0,1,0])
v3 = Vector([0,0,1])

print LI([v1,v2,v3])
