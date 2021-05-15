from matrix_lib import *

#Some helpers
def getDiagonal(M,row,col):
    if not isinstance(M, Matrix):
        raise TypeError("Input is not a matrix.")
        return False
    if not (0 < row <= len(M.store)):
        raise TypeError("Index is out of range.")
    if not (0 < col <= len(M.store[0])):
        raise TypeError("Index is out of range.")
    #There's not really a great way to uniquely specify a diagonal,
    #so this just gets the diagonal that the entry r,c lies in

    out = [M.store[row-1][col-1]]
    #Going up the diagonal
    r = row+1
    c = col+1
    while r <= len(M.store) and c <= len(M.store[0]):
        out += [M.store[r-1][c-1]]
        r += 1
        c += 1

    #going down the diagonal
    r = row-1
    c = col-1
    while r > 0 and c > 0:
        out = [M.store[r-1][c-1]] + out
        r -= 1
        c -= 1

    return out

def getSkewDiagonal(M,row,col):
    if not isinstance(M, Matrix):
        raise TypeError("Input is not a matrix.")
        return False
    if not (0 < row <= len(M.store)):
        raise TypeError("Index is out of range.")
    if not (0 < col <= len(M.store[0])):
        raise TypeError("Index is out of range.")
    #There's not really a great way to uniquely specify a diagonal,
    #so this just gets the diagonal that the entry r,c lies in

    out = [M.store[row-1][col-1]]
    #Going up the diagonal
    r = row-1
    c = col+1
    while r > 0 and c <= len(M.store[0]):
        out += [M.store[r-1][c-1]]
        r -= 1
        c += 1

    #going down the diagonal
    r = row+1
    c = col-1
    while r <= len(M.store) and c > 0:
        out = [M.store[r-1][c-1]] + out
        r += 1
        c -= 1

    return out

def SkewTranspose(M):
    if not isinstance(M, Matrix):
        raise TypeError("Input is not a matrix.")
        return False
    if not M.isSquare():
        raise TypeError("Input must be a square matrix.")

    out = []
    for c in range(len(M.store[0])-1,-1,-1):
        temp = []
        for r in range(len(M.store)-1,-1,-1):
            temp += [M.store[r][c]]
        out += [temp]
    return Matrix(out)

#Generate unqiue matrices
#Sortcuts for common matrices
def Zero(m,n):
    #m x n denotes rows x columns by convension
    if m < 1 or n < 1:
        raise TypeError("Matrix dimensions must be positive.")
        return None
    if m != int(m) or n != int(n):
        raise TypeError("Matrix dimensions must be integer.")
        return None
    out = []
    for i in range(m):
        out += [[0]*n]
    return Matrix(out)

def I(n):
    if n < 1:
        raise TypeError("Matrix dimensions must be positive.")
        return None
    if n != int(n):
        raise TypeError("Matrix dimensions must be integer.")
        return None
    M_out = Zero(n,n)
    for i in range(n):
        M_out.store[i][i] = 1
    return M_out

def Exchange(n):
    if n < 1:
        raise TypeError("Matrix dimensions must be positive.")
        return None
    if n != int(n):
        raise TypeError("Matrix dimensions must be integer.")
        return None
    return Matrix(list(reversed(I(n).store)))

def Hilbert(m,n):
    #m x n denotes rows x columns by convension
    if m < 1 or n < 1:
        raise TypeError("Matrix dimensions must be positive.")
        return None
    if m != int(m) or n != int(n):
        raise TypeError("Matrix dimensions must be integer.")
        return None
    out = []
    for i in range(1,n+1):
        temp = []
        for j in range(1,m+1):
            temp += [1/float(i+j-1)]
        out += [temp]
    return Matrix(out)

def Lehmer(n):
    if n < 1:
        raise TypeError("Matrix dimensions must be positive.")
        return None
    if n != int(n):
        raise TypeError("Matrix dimensions must be integer.")
        return None
    out = []
    for i in range(1,n+1):
        temp = []
        for j in range(1,n+1):
            temp += [min(i,j)/float(max(i,j))]
        out += [temp]
    return Matrix(out)

def Pascal(n):
    if n < 1:
        raise TypeError("Matrix dimensions must be positive.")
        return None
    if n != int(n):
        raise TypeError("Matrix dimensions must be integer.")
        return None
    
    #A recursive method that totally works, but I'm sure if very ineffiecent
    """
    if n == 1:
        return Matrix([[1]])
    if n == 2:
        return Matrix([[1, 1],[1, 2]])
    temp = Pascal(n-1)
    out = temp.store
    out += [[1]*len(out[0])]
    for r in range(len(out)):
        out[r] += [1]

    #now we just have to iterate over the last row and last col
    for c in range(1, len(out[0])):
        out[-1][c] = out[-1][c-1] + out[-2][c]
    for r in range(1, len(out)):
        out[r][-1] = out[r][-2] + out[r-1][c]
    return Matrix(out)
    """
    def factorial(n):
        if n == 0:
            return 1
        accum = 1
        for i in range(1,n+1):
            accum *= i
        return accum
    def nCr(n,r):
        return factorial(n)/(factorial(r) * factorial(n-r))
    out = []
    for i in range(n):
        temp = []
        for j in range(n):
            temp += [nCr(i+j,i)]
        out += [temp]
    return Matrix(out)

def Redheffer(m, n):
    #m x n denotes rows x columns by convension
    if m < 1 or n < 1:
        raise TypeError("Matrix dimensions must be positive.")
        return None
    if m != int(m) or n != int(n):
        raise TypeError("Matrix dimensions must be integer.")
        return None
    out = []
    for i in range(1,n+1):
        temp = []
        for j in range(1,m+1):
            if j == 1:
                temp += [1]
            elif j % i == 0:
                temp += [1]
            else:
                temp += [0]
        out += [temp]
    return Matrix(out)

#checking types of matrices

#Any mxn matricies can be of these types

#Also called stochastic matrix, probability matrix, transition matrix,and substitution matrix
#The entries in each row are non-negative and sum to 1
def isLeftStochastic(M):
    if not isinstance(M, Matrix):
        raise TypeError("Input is not a matrix.")
        return False
    
    for r in range(len(M.store)):
        for c in range(len(M.store[r])):
            if M.store[r][c] < 0:
                return False
        if sum(M.store[r]) != 1:
            return False
    return True

#The entries in each col are non-negative and sum to 1
def isRightStochastic(M):
    if not isinstance(M, Matrix):
        raise TypeError("Input is not a matrix.")
        return False
    
    for c in range(len(M.store[0])):
        temp = 0
        for r in range(len(M.store)):
            if M.store[r][c] < 0:
                return False
            temp += M.store[r][c]
        if temp != 1:
            return False
    return False

def isDoublyStochastic(M):
    if isLeftStochastic(M) and isRightStochastic(M):
        return True
    return False


#isSquare is the only one of these types of functions that is in the Matrix Class 
#   bc it is needed for the Det() method
#Below are the matrix types that are dependent on the matrix being square
#   Matrices that are a subset of Square

#A*A = A
def isIdempotent(M):
    if not isinstance(M, Matrix):
        raise TypeError("Input is not a matrix.")
        return False
    if not M.isSquare():
        return False

    if M.store == multiply(M,M).store:
        return True
    return False

#A^t = A^-1
def isOrthogonal(M):
    if not isinstance(M, Matrix):
        raise TypeError("Input is not a matrix.")
        return False
    if not M.isSquare():
        return False
    
    if M.transpose() == M.Inverse():
        return True
    return False

#Every entry below the main diagonal is zero
def isLowerTriangular(M):
    if not isinstance(M, Matrix):
        raise TypeError("Input is not a matrix.")
        return False
    if not M.isSquare():
        return False
    
    for r in range(1,len(M.store)):
        for c in range(len(M.store)-r, len(M.store[r])):
            if M.store[r][c] != 0:
                return False
    return True

#Every entry above the main diagaonal is zero
def isUpperTriangular(M):
    if not isinstance(M, Matrix):
        raise TypeError("Input is not a matrix.")
        return False
    if not M.isSquare():
        return False

    for r in range(0,len(M.store)):
        for c in range(0, len(M.store[r])-(r+1)):
            if M.store[r][c] != 0:
                return False
    return True

#Either upper triangular or lower triangular
def isTranglular(M):
    if isLowerTriangular(M) or isUpperTriangular(M):
        return True
    return False

#All entries are zero except the main diagonal
def isDiagonal(M):
    if not isinstance(M, Matrix):
        raise TypeError("Input is not a matrix.")
        return False
    if not M.isSquare():
        return False

    for r in range(len(M.store)):
        for c in range(len(M.store[r])):
            if r != c and M.store[r][c] != 0:
                return False
    return True

#All entries are zero except the main skew diagonal
def isAntiDiagonal(M):
    if not isinstance(M, Matrix):
        raise TypeError("Input is not a matrix.")
        return False
    if not M.isSquare():
        return False

    for r in range(len(M.store)):
        for c in range(len(M.store[r])):
            if (len(M.store) - 1 - r) != c and M.store[r][c] != 0:
                return False
    return True

#All entries in main diagonal are zero
def isHollow(M):
    if getDiagonal(1,1) == [0]*len(M.store):
        return True
    return False

#All elements in first row and first column are nonzero
#Rest are zero
def isArrowhead(M):
    if not isinstance(M, Matrix):
        raise TypeError("Input is not a matrix.")
        return False
    if not M.isSquare():
        return False
    
    #Checking upper part
    for r in range(1,len(M.store)):
        for c in range(r+1, len(M.store[r])):
            if M.store[r][c] != 0:
                return False

    #Checking lower part
    for r in range(1,len(M.store)):
        for c in range(1, len(M.store[r]) - r):
            if M.store[len(M.store) - r][c] != 0:
                return False
    return True

#A^t = -A
def isSkew(M):
    if M.scale(-1).store == M.transpose().store:
        return True
    return False

#A^t = A
#(Symmetric about the main diagonal)
def isSymmetric(M):
    if not isinstance(M, Matrix):
        raise TypeError("Input is not a matrix.")
        return False
    if not M.isSquare():
        return False

    if M.store == M.transpose().store:
        return True
    return False

#Symmetric about the main skew diagonal
def isPersymmetric(M):
    if not isinstance(M, Matrix):
        raise TypeError("Input is not a matrix.")
        return False
    if not M.isSquare():
        return False

    if M.store == SkewTranspose(M).store:
        return True
    return False

#Matrix is symmetric about its center. Hard to explain just look up an image
#boils down to it being symmetric about the main diagonal and the main skew diagonal
#Or its both symmetric and presymmetric
def isCentrosymmetric(M):
    if not isinstance(M, Matrix):
        raise TypeError("Input is not a matrix.")
        return False
    if not M.isSquare():
        return False
    
    if isSymmetric(M) and isPresymmetric(M):
        return True
    return False

#Matrix is an elementary matrix, i.e.
#   E1(k, i)        scale a row by a constant
#   E2(k, i, j)     add a scaled row to another row
#   E3(i, j)        switch two rows
def isElementary(M):
    return False

#also called Monomial
#The matrix is just the identity with the rows shuffled
def isPermutation(M):
    if not isinstance(M, Matrix):
        raise TypeError("Input is not a matrix.")
        return False
    if not M.isSquare():
        return False

    if list(reversed(sorted(M.store))) == I(M.dim()[0]).store:
        return True
    return False

#Not sure yet lol
def isCompound(M):
    return False

#Every entry on a common diagonal contains the same value
def isToeplitz(M):
    if not isinstance(M, Matrix):
        raise TypeError("Input is not a matrix.")
        return False
    if not M.isSquare():
        return False

    for r in range(len(M.store)):
        if getDiagonal(M,r+1,1)[1:] != getDiagonal(M,r+1,1)[:-1]:
            return False
        if getDiagonal(M,r+1,len(M.store[0]))[1:] != getDiagonal(M,r+1,len(M.store[0]))[:-1]:
            return False
    return True

#Every entry on a common skew diagonals contain the same value
def isHankel(M):
    if not isinstance(M, Matrix):
        raise TypeError("Input is not a matrix.")
        return False
    if not M.isSquare():
        return False

    for r in range(len(M.store)):
        if getSkewDiagonal(M,r+1,1)[1:] != getSkewDiagonal(M,r+1,1)[:-1]:
            return False
        if getSkewDiagonal(M,r+1,len(M.store[0]))[1:] != getSkewDiagonal(M,r+1,len(M.store[0]))[:-1]:
            return False
    return True
