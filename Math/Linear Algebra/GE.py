from matrix_lib import *

#Elementary Row Ops
# k*r_i -> r_i
def E1(M, k, i):
    if not (0 < i <= len(M.store)):
        raise TypeError("Index out of range.")
        return M
    for c in range(len(M.store[i-1])):
        M.store[i-1][c] *= k
    return M

# r_i + k*r_j -> r_i
def E2(M, k, i, j):
    if not (0 < i <= len(M.store)):
        raise TypeError("Index out of range.")
        return M
    if not (0 < j <= len(M.store)):
        raise TypeError("Index out of range.")
        return M
    if i == j:
        raise TypeError("Indices are equal.")
        return M
    
    for c in range(len(M.store[i-1])):    #using fact that row(i) = row(j)
        M.store[i-1][c] += k*M.store[j-1][c]
    return M

# r_i <-> r_j
def E3(M, i, j):
    if not (0 < i <= len(M.store)):
        raise TypeError("Index out of range.")
        return M
    if not (0 < j <= len(M.store)):
        raise TypeError("Index out of range.")
        return M
    if i == j:
        raise TypeError("Indeces are equal.")
        return M

    M.store[i-1], M.store[j-1] = M.store[j-1], M.store[i-1]
    return M

# For the easy case of an nxn with non-zero determinant, 
# this code works and it's clean and easy to follow
"""
def ge_fwd(M):

    for lead in range(len(M.store)):
        #make the leading entry equal to one
        E1(M, 1/float(M.store[lead][lead]), lead+1)

        #make all the entries in the same col in the rows below it zero
        for j in range(lead+1,len(M.store)):
            E2(M, -M.store[j][lead], j+1, lead+1)
    
    return M

def ge_bwd(M):

    for lead in range(len(M.store)-1, -1, -1):
        #make the leading entry equal to one
        E1(M, 1/float(M.store[lead][lead]), lead+1)

        #make all the entries in the same col in the rows below it zero
        for j in range(lead):
            E2(M, -M.store[j][lead], j+1, lead+1)

    return M
"""

#But the world isn't easy, so we need to messy the code up with handle all the exceptions
def ge_fwd(M):

    lead = 0
    col_cor = 0
    # Think about it this way. The lead index is gonna go down the diagonal
    # Sometime we need to correct it, hence col_cor
    # we never have to correct for the row index bc we can swap rows
    while lead+col_cor < len(M.store):
        # First move all non_zero rows to the bottom
        # This is acutally quite elegant if you think about it
        M.store.sort()
        M.store.reverse()

        # So now we have to deal with the fact that the leading column could be all zeros
        #
        #   This is the general case...all you do is just move to the next col and continue
        #
        #   | 1  *  ...  *  * ...  * |
        #   | 0  ...                 |
        #   | 0     1    *  * ...  * |
        #   | 0     0    0  *      * |
        #   | 0     0    0  *      * |
        while True:
            if M.getCol(lead + col_cor + 1)[lead:] == [0]*( M.dim()[0] - lead):
                col_cor += 1
            else:
                break
        
        if lead + col_cor >= len(M.store):
            break

        # Okay so now what about the case where we have a zero in the leading entry,
        # but nonzeros below
        #   
        #   You just have to switch it with a row below it that has a nonzero entry
        #
        #   | 1  *  ...  *  * ...  * |
        #   | 0  ...                 |
        #   | 0     1    *  * ...  * |
        #   | 0     0    0  *      * |
        #   | 0     0    *  *      * |
        #
        # The reason the sorted line is elegant is that it actually fixes this problem
        
        #make the leading entry equal to one
        E1(M, 1/float(M.store[lead][lead + col_cor]), lead+1)

        #make all the entries in the same col in the rows below it zero
        for j in range(lead+1,len(M.store)):
            E2(M, -M.store[j][lead + col_cor], j+1, lead+1)
        
        lead += 1

    return M

def ge_bwd(M):

    # The strategy for this one is much easier:
    #   We just have to find the index of the col with a leading 1 
    #   make all other cols have 0's in that index
    #   do this for each row starting from the bottom 

    for r in range(len(M.store)-1, -1, -1):
        
        # get col with leading entry
        # Might have to worry about zero cols, but not sure
        c = -1
        for i in range(len(M.getRow(r+1))):
            if M.getRow(r+1)[i] == 0:
                c = i
            else:
                break
        c += 1

        #print M.store[r],c
        #make the leading entry equal to one
        E1(M, 1/float(M.store[r][c]), r+1)

        #make all the entries in the same col in the rows below it zero
        for j in range(r):
            E2(M, -M.store[j][c], j+1, r+1)

    return M

def ge(M,y):
    if not isinstance(M, Matrix) or not isinstance(y, Matrix):
        raise TypeError("Arguement is not matrix.")
    return ge_bwd(ge_fwd(augment(M,y)))

"""
M = Matrix([[1, -3, 1], [2, -8, 8], [-6, 3, -15]])
y = Matrix([[4],[-2],[9]])
print augment(M, y).get()
print
print ge_fwd(augment(M, y)).get()
print
print ge_bwd(ge_fwd(augment(M, y))).get()
print 
print multiply(M.Inverse(),y).get()
"""


