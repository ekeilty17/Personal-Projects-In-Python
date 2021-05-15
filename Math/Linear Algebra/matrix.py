from CoordinateSystem import *
from vector import *
from sympy import *
import sys
from random import randint

class Matrix(object):
    def __init__(self, L, Vin=None, Vout=None):
        
        # Error checks on L
        if type(L) != list:
            raise TypeError("Input not a 2-dim list.")
        # making sure input is a rectangle
        row_len = L[0]
        for r in L:
            if type(r) != list:
                raise TypeError("Input not a 2-dim list.")
            if len(r) != len(row_len):
                raise TypeError("Rows do not contain the same number of elements.")
            # making sure each element is a number or a sympy symbol
            for e in r:
                if type(e) != int and type(e) != float and isinstance(e, Symbol) or isinstance(e, Pow):
                    raise TypeError("Elements are not integers.")
        
        # Setting default vector spaces
        if Vin == None and Vout == None:
            Vin = Cartesian(len(L))
            Vout = Cartesian(len(L[0]))
        
        # Error Checks on Vector spaces
        if not isinstance(Vin, Curvillinear):
            raise TypeError("Second arguement must be a Curvillinear object.")
        if not isinstance(Vout, Curvillinear):
            raise TypeError("Third arguement must be a Curvillinear object.")
        
        # Check that L and V are compatible
        if len(L) != len(Vin):
            raise TypeError("Number of rows in input list must match dimension of the input vector space.")
        if len(L[0]) != len(Vout):
            raise TypeError("Number of cols in input list must match dimension of the out vector space.")

        self.L = L
        self.Vin = Vin
        self.Vout = Vout
        self.accuracy = 20
    
    """"""""""""""""""""""""""""""""""""""""""""""""
    """         Standard Class Stuff             """
    """"""""""""""""""""""""""""""""""""""""""""""""
    def setMatrix(self, L):
        if type(L) != list:
            raise TypeError("Input not a 2-dim list.")
        # making sure input is a rectangle
        row_len = L[0]
        for r in L:
            if type(r) != list:
                raise TypeError("Input not a 2-dim list.")
            if len(r) != len(row_len):
                raise TypeError("Rows do not contain the same number of elements.")
            # making sure each element is a number or a sympy symbol
            for e in r:
                if type(e) != int and type(e) != float and isinstance(e, Symbol) or isinstance(e, Pow):
                    raise TypeError("Elements are not integers.")
        if len(L) != len(self.Vin):
            raise TypeError("Number of rows in input list must match dimension of the input vector space.")
        if len(L[0]) != len(self.Vout):
            raise TypeError("Number of cols in input list must match dimension of the out vector space.")
        
        self.L = L
    
    def setCoordinateSystem(self, Vin, Vout):
        # Error Checks on Vector spaces
        if not isinstance(Vin, Curvillinear):
            raise TypeError("Second arguement must be a Curvillinear object.")
        if not isinstance(Vout, Curvillinear):
            raise TypeError("Third arguement must be a Curvillinear object.")

        # Check that L and V are compatible
        if len(L) != len(Vin):
            raise TypeError("Number of rows in input list must match dimension of the input vector space.")
        if len(L[0]) != len(Vout):
            raise TypeError("Number of cols in input list must match dimension of the out vector space.")
        
        self.Vin = Vin
        self.Vout = Vout
    
    def setAccuracy(self, accuracy):
        self.accuracy = accuracy

    # FIX: There are still bugs in this
    def printf(self,acc=4):
        out = ""
        
        def num_digits(x):
            # number of digits = number of digits before decimal point + number of digits after decimal point
            n = str(float(abs(x)))[::1].find('.') + str(float(x))[::-1].find('.')
            # removing a digit because the above counts 4.0 as 2 digits not 1
            if x == int(x):
                n -= 1
            return n

        # getting maximum number of digits comprising matrix
        max_digits = 1
        for row in self.L:
            for e in row:
                if num_digits(round(e,acc)) > max_digits:
                    max_digits = num_digits(round(e,acc))
        tab_space = 6

        for row in self.L:
            row_str = ""
            for j in range(0,len(row)):
                # add a space for the sign of the number
                if row[j] >= 0:
                    row_str += ' '
                # This is because python will sometimes print '-0.000'
                if row[j] == 0:
                    row_str += str(0)
                else:
                    # so we it prints '4' instead of '4.0'
                    if row[j] == int(row[j]):
                        row_str += str(row[j])
                    else:
                        row_str += str(round(row[j],acc))
                # add correct spacing between columns
                if j != len(row)-1:
                    #row_str += '\t'
                    curr_digits = num_digits(round(row[j],acc))
                    row_str += '\t'*( ((max_digits-curr_digits)/tab_space + 1) )
            out += row_str + '\n'
        return out[:-1]

    def __str__(self):
        # floating points only maintain a certain level of accuracy
        return self.printf(self.accuracy)
    
    # This will be compatible with a_ij notation
    def __getitem__(self, index):
        return self.L[index]
    
    def copy(self):
        out = []
        for r in self.L:
            out += [list(r)]
        M = Matrix(out, self.Vin, self.Vout)
        M.setAccuracy(self.accuracy)
        return M

    def dim(self):
        #m x n denotes rows x cols is the usual convension
        #this return [m, n]
        return [len(self.L),len(self.L[0])]
    
    
    """"""""""""""""""""""""""""""""""""""""""""""""
    """              Matrix Types                """
    """"""""""""""""""""""""""""""""""""""""""""""""
    # if number of rows = number of cols
    def isSquare(self):
        if len(self.L) == len(self.L[0]):
            return True
        return False
    
    # A*A = A
    def isIdempotent(self):
        if not self.isSquare():
            return False
        return self*self == self

    # A^t = A
    def isSymmetric(self):
        return self.transpose() == self
    
    # A^t = -A
    def isSkew(self):
        return self.transpose() == self * (-1)
    
    # A^t = A^-1
    def isOrthogonal(self):
        if not self.isSquare():
            return False
        return self.transpose() == self.inverse()
    
    # Symmetric about the main skew diagonal
    def isPersymmetric(self):
        return self == self.skew_transpose()

    #Matrix is symmetric about its center. Hard to explain just look up an image
    #boils down to it being symmetric about the main diagonal and the main skew diagonal
    #Or its both symmetric and presymmetric
    def isCentrosymmetric(self):
        return (self.isSymmetric() and self.isPresymmetric())
    
    # All entries are zero except the main diagonal
    def isDiagonal(self):
        if not self.isSquare():
            return False
        for r in range(len(self.L)):
            for c in range(len(self.L[r])):
                if r != c and self.L[r][c] != 0:
                    return False
        return True

    # All entries are zero except the main skew diagonal
    def isAntiDiagonal(self):
        if not self.isSquare():
            return False
        for r in range(len(self.L)):
            for c in range(len(self.L[r])):
                if (len(self.L)-1 - r) != c and self.L[r][c] != 0:
                    return False
        return True

    # All entries in main diagonal are zero
    def isHollow(self):
        return self.getDiagonal(1,1) == [0]*len(self.L)

    # All elements in first row and first column are nonzero
    # The rest are zero
    def isArrowhead(self):
        if not self.isSquare():
            return False

        # Checking upper part
        for r in range(1,len(self.L)):
            for c in range(r+1, len(self.L[r])):
                if self.L[r][c] != 0:
                    return False

        # Checking lower part
        for r in range(1,len(self.L)):
            for c in range(1, len(self.L[r]) - r):
                if self.L[len(self.L) - r][c] != 0:
                    return False
        return True
    
    # Every entry below the main diagonal is zero
    def isLowerTriangular(self):
        if not self.isSquare():
            return False
        for r in range(1,len(self.L)):
            for c in range(len(self.L)-r, len(self.L[r])):
                if self.L[r][c] != 0:
                    return False
        return True
    
    # Every entry above the main diagaonal is zero
    def isUpperTriangular(self):
        if not self.isSquare():
            return False
        for r in range(0,len(self.L)):
            for c in range(0, len(self.L[r])-(r+1)):
                if self.L[r][c] != 0:
                    return False
        return True
    
    # Either upper triangular or lower triangular
    def isTranglular(self):
        return (self.isLowerTriangular() or self.isUpperTriangular())
    
    #Matrix is an elementary matrix, i.e.
    #   E1(k, i)        scale a row by a constant
    #   E2(k, i, j)     add a scaled row to another row
    #   E3(i, j)        switch two rows
    def isElementary(self):
        return False
    
    # Also called a probability matrix, transition matrix,and substitution matrix
    # The entries in each row are non-negative and sum to 1
    def isLeftStochastic(self):
        for r in range(len(self.L)):
            for c in range(len(self.L[r])):
                if self.L[r][c] < 0:
                    return False
            if sum(self.L[r]) != 1:
                return False
        return True

    # The entries in each col are non-negative and sum to 1
    def isRightStochastic(self):
        for c in range(len(self.L[0])):
            temp = 0
            for r in range(len(self.L)):
                if self.L[r][c] < 0:
                    return False
                temp += self.L[r][c]
            if temp != 1:
                return False
        return True

    # Both left and right stochastic
    def isDoublyStochastic(self):
        return (self.isLeftStochastic() and self.isRightStochastic())
    
    #also called Monomial
    #The matrix is just the identity with the rows shuffled
    def isPermutation(self):
        if not self.isSquare():
            return False
        if list(reversed(sorted(self.L))) == I(self.dim()[0]).L:
            return True
        return False

    #Not sure yet lol
    def isCompound(self):
        return False
    
    #Every entry on a common diagonal contains the same value
    def isToeplitz(self):
        if not self.isSquare():
            return False
        for r in range(len(self.L)):
            if self.getDiagonal(r+1,1)[1:] != self.getDiagonal(r+1,1)[:-1]:
                return False
            if self.getDiagonal(r+1,len(self.L[0]))[1:] != self.getDiagonal(r+1,len(self.L[0]))[:-1]:
                return False
        return True
    
    #Every entry on a common skew diagonals contain the same value
    def isHankel(self):
        if not self.isSquare():
            return False
        for r in range(len(self.L)):
            if self.getSkewDiagonal(r+1,1)[1:] != self.getSkewDiagonal(r+1,1)[:-1]:
                return False
            if self.getSkewDiagonal(r+1,len(self.L[0]))[1:] != self.getSkewDiagonal(r+1,len(M.store[0]))[:-1]:
                return False
        return True


    """"""""""""""""""""""""""""""""""""""""""""""""
    """    Row and Column operations on Matrix   """
    """"""""""""""""""""""""""""""""""""""""""""""""
    def getRow(self,r):
        if not (0 < r <= len(self.L)):
            raise TypeError("Index out of range.")
        return self.L[r-1]

    def getCol(self,c):
        if not (0 < c <= len(self.L[0])):
            raise TypeError("Index out of range.")
        out = []
        for i in range(len(self.L)):
            out += [self.L[i][c-1]]
        return out

    def deleteRow(self,r):
        if not (0 < r <= len(self.L)):
            raise TypeError("Index out of range.")
        self.L = self.L[:r-1] + self.L[r:]
        # Need to update Vin
        return self

    def deleteCol(self,c):
        if not (0 < c <= len(self.L[0])):
            raise TypeError("Index out of range.")
        for i in range(len(self.L)):
            self.L[i] = self.L[i][:c-1] + self.L[i][c:]
        # Need to update Vout
        return self

    def addRow(self, row, r):
        if len(row) != len(self.L[0]):
            raise TypeError("Number of element in input row does not match number of columns in matrix")
        if not (0 < r <= len(self.L)):
            raise TypeError("Index out of range.")
        self.L = self.L[:r] + [row] + self.L[r:]
        # TODO Need to update Vin
        return self

    def addCol(self, col, c):
        if len(col) != len(self.L):
            raise TypeError("Number of element in input col does not match number of rows in matrix")
        if not (0 < c <= len(self.L[0])):
            raise TypeError("Index out of range.")
        for i in range(len(self.L)):
            self.L[i] = self.L[i][:c] + [col[i]] + self.L[i][c:]
        # TODO Need to update Vout
        return self
    
    def augment(self, M):
        # TODO Need to change that Vout's match
        if not isinstance(M, Matrix):
            raise TypeError("Arguement must be a matrix.")
        if self.dim()[0] != M.dim()[0]:
            raise TypeError("Dimensions of matrices do not agree.")
        out = []
        for i in range(len(self.L)):   #row(A) == row(B)
            out += [self.L[i] + M.L[i]]
        # TODO Need to update Vin
        return Matrix(out)

    def getDiagonal(self, row=1, col=1):
        if not (0 < row <= len(self.L)):
            raise TypeError("Index is out of range.")
        if not (0 < col <= len(self.L[0])):
            raise TypeError("Index is out of range.")
        #There's not really a great way to uniquely specify a diagonal,
        #so this just gets the diagonal that the entry r,c lies in

        out = [self.L[row-1][col-1]]
        #Going up the diagonal
        r = row+1
        c = col+1
        while r <= len(self.L) and c <= len(self.L[0]):
            out += [self.L[r-1][c-1]]
            r += 1
            c += 1

        #going down the diagonal
        r = row-1
        c = col-1
        while r > 0 and c > 0:
            out = [self.L[r-1][c-1]] + out
            r -= 1
            c -= 1

        return out
    
    def getSkewDiagonal(self, row=1, col=None):
        if col == None:
            col = len(self.L[0])
        if not (0 < row <= len(self.L)):
            raise TypeError("Index is out of range.")
        if not (0 < col <= len(self.L[0])):
            raise TypeError("Index is out of range.")
        #There's not really a great way to uniquely specify a diagonal,
        #so this just gets the diagonal that the entry r,c lies in

        out = [self.L[row-1][col-1]]
        #Going up the diagonal
        r = row-1
        c = col+1
        while r > 0 and c <= len(self.L[0]):
            out += [self.L[r-1][c-1]]
            r -= 1
            c += 1

        #going down the diagonal
        r = row+1
        c = col-1
        while r <= len(self.L) and c > 0:
            out = [self.L[r-1][c-1]] + out
            r += 1
            c -= 1

        return out

    
    """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    """   Special Matrices contructed from original Matrix   """
    """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    # Special Matrices contructed from original Matrix
    def transpose(self):
        out = []
        for c in range(len(self.L[0])):
            temp = []
            for r in range(len(self.L)):
                temp += [self.L[r][c]]
            out += [temp]
        return Matrix(out, self.Vout, self.Vin)
    
    def skew_transpose(self):
        out = []
        for c in range(len(self.L[0])-1,-1,-1):
            temp = []
            for r in range(len(self.L)-1,-1,-1):
                temp += [self.L[r][c]]
            out += [temp]
        return Matrix(out, self.Vout, self.Vin)

    def submatrix(self,r,c):
        if not (0 < r <= len(self.L)):
            raise TypeError("Row index is out of range.")
        if not (0 < c <= len(self.L[0])):
            raise TypeError("Column index is out of range.")

        row = r-1
        col = c-1
        #getting rid of rth row
        out = self.L[:row] + self.L[row+1:]
        #getting rid of cth col
        for i in range(len(out)):
            out[i] = out[i][:col] + out[i][col+1:]
        
        # TODO update Vin and Vout wihtout changing variables
        return Matrix(out)

    def cofactor_matrix(self):
        out = []
        for i in range(len(self.L)):
            temp = []
            for j in range(len(self.L[i])):
                temp += [self.cof(i+1,j+1)]
            out += [temp]
        return Matrix(out)
    
    def adj(self):
        return self.cofactor_matrix().transpose()
   
    def inverse(self):
        if not self.isSquare():
            raise TypeError("Inverse is only defined for square matrices.")
        if self.Det() == 0:
            raise TypeError("Inverse does not exist.")
        return self.adj() / self.Det()
    

    """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    """    Special Values derivated from original Matrix     """
    """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    # Special Values derivated from original Matrix
    def Det(self):
        if not self.isSquare():
            raise TypeError("Determinant is only defined for square matrices.")
        if len(self.L) == 1:
            return self.L[0][0]
        if len(self.L) == 2:
            return self.L[0][0]*self.L[1][1] - self.L[0][1]*self.L[1][0]
        else:
            accum = 0
            for i in range(len(self.L)):
                #The Laplace Expansion gives us a lot of flexibility
                #I am iterating over the ith row and 0th col
                accum += ((-1)**(i+1+0+1))*self.L[i][0]*self.minor(i+1,0+1)
            return accum
    
    def minor(self,r,c):
        return self.submatrix(r,c).Det()

    def cof(self,r,c):
        return (-1)**(r+c) * self.minor(r,c)
   

    """"""""""""""""""""""""""""""""""""""""""""""""
    """               Operations                 """
    """"""""""""""""""""""""""""""""""""""""""""""""
    def __mul__(self, M):
        if isinstance(M, Matrix):
            if self.Vin != M.Vout:
                raise TypeError("Matrices do not occupy compatible coordinate systems.")
            if self.dim()[1] != M.dim()[0]:
                raise TypeError("Dimensions of matrices do not agree.")
            out = []
            M_t = M.transpose()
            for i in range(len(self.L)):
                temp = []
                for j in range(len(M_t.L)):
                    accum = 0
                    for k in range(len(self.L[i])):    #using the fact row(A) == col(B)
                        accum += self.L[i][k] * M_t.L[j][k]
                    temp += [accum]
                out += [temp]
            return Matrix(out)
        elif isinstance(M, Vector):
            if self.Vin != M.V:
                raise TypeError("Matrix and vector do not occupy compatible coordinate systems.")
            if self.dim()[1] != len(M):
                raise TypeError("Dimensions of matrix and vector do not agree.")
            out = []
            for i in range(len(self.L)):
                accum = 0
                for j in range(len(self.L[i])):
                    accum += self.L[i][j] * M[i]
                out += [accum]
            return Vector(out)
        elif type(M) == int or type(M) == float or isinstance(M, Symbol) or isinstance(M, Pow):
            A = self.copy()
            for i in range(len(A.L)):
                for j in range(len(A.L[i])):
                    A.L[i][j] *= M
            return A
        else:
            raise TypeError("Operation on this type has not been implemented.")

    def __rmul__(self, M):
        # I think this is unnecessary bc I think python checks if __mul__ is defined for the 
        # left variable first, and if it's not it checks if __rmul__ is defined for the right variable
        # but just to keep all bases coovered
        if isinstance(M, Matrix):
            return M.__mul__(self)
        # Same this this, this will actually throw the error on the vector side, not the matrix side
        elif isinstance(M, Vector):
            raise TypeError("Left multiplication of vectors is not defined for matrices")
        elif type(M) == int or type(M) == float or isinstance(M, Symbol) or isinstance(M, Pow):
            return self.__mul__(M)
        else:
            raise TypeError("Operation on this type has not been implemented.")
    
    def __div__(self, k):
        # interpret matrix division as right iultiplication by the inverse
        if isinstance(k, Matrix):
            return self * k.inverse()
        elif isinstance(k, Vector):
            raise TypeError("Vector division of a matrix has not been defined.")
        elif isinstance(k, Symbol) or isinstance(k, Pow):
            A = self.copy()
            for i in range(len(A.L)):
                for j in range(len(A.L[i])):
                    A.L[i][j] /= k
            return A
        elif type(k) == int or type(k) == float:
            return self.__mul__(1.0/k)
        else:
            raise TypeError("Operation on this type has not been implemented.")
       
    def __mod__(self, k):
        A = self.copy()
        for i in range(len(A.L)):
            for j in range(len(A.L[i])):
                A.L[i][j] %= k
        return A

    def __pow__(self, k):
        if int(k) != k:
            raise TypeError("Noninteger exponents have not been implemented.")
        if k < 0:
            raise TypeError("Exponents below 0 have not been implemented.")
        if k == 0:
            return 1
        A = self.copy()
        for i in range(int(k)):
            A *= self
        return A

    def __add__(self, M):
        # Matrix addition
        if isinstance(M, Matrix):
            if self.Vin != M.Vin or self.Vout != M.Vout:
                raise TypeError("Matrices do not occupy the same coordinate system.")
            if self.dim() != M.dim():
                raise TypeError("Dimensions of matrices do not match.")
            out = []
            for i in range(len(self.L)):
                temp = []
                for j in range(len(self.L[i])):
                    temp += [self[i][j] + M[i][j]]
                out += [temp]
            return Matrix(out)
        # addition by a scalar
        elif type(M) == int or type(M) == float or isinstance(M, Symbol) or isinstance(M, Pow):
            A = self.copy()
            for i in range(len(A.L)):
                for j in range(len(A.L[i])):
                    A.L[i][j] += M
            return A
        else:
            raise TypeError("Operation on this type has not been implemented.")
    
    def __sub__(self, M):
        return self + M * (-1)


""""""""""""""""""""""""""""""""""""""""""""""""
"""             Useful Matrices              """
""""""""""""""""""""""""""""""""""""""""""""""""
def Zero(m,n=None):
    if n == None:
        n = m
    #m x n denotes rows x columns by convension
    if m < 1 or n < 1:
        raise TypeError("Matrix dimensions must be positive.")
    if m != int(m) or n != int(n):
        raise TypeError("Matrix dimensions must be integer.")
    out = []
    for i in range(m):
        out += [[0]*n]
    return Matrix(out)

def Ones(m, n=None):
    if n == None:
        n = m
    #m x n denotes rows x columns by convension
    if m < 1 or n < 1:
        raise TypeError("Matrix dimensions must be positive.")
    if m != int(m) or n != int(n):
        raise TypeError("Matrix dimensions must be integer.")
    out = []
    for i in range(m):
        out += [[1]*n]
    return Matrix(out)

def Random(m, n=None):
    if n == None:
        n = m
    #m x n denotes rows x columns by convension
    if m < 1 or n < 1:
        raise TypeError("Matrix dimensions must be positive.")
    if m != int(m) or n != int(n):
        raise TypeError("Matrix dimensions must be integer.")
    out = []
    for i in range(m):
        temp = []
        for j in range(n):
            temp += [randint(-9, 9)]
        out += [temp]
    return Matrix(out)

def I(n):
    if n < 1:
        raise TypeError("Matrix dimensions must be positive.")
    if n != int(n):
        raise TypeError("Matrix dimensions must be integer.")
    M_out = Zero(n,n)
    for i in range(n):
        M_out[i][i] = 1
    return M_out

def Exchange(n):
    if n < 1:
        raise TypeError("Matrix dimensions must be positive.")
    if n != int(n):
        raise TypeError("Matrix dimensions must be integer.")
    return Matrix(list(reversed(I(n).L)))

"""
A = Matrix([[-1, -2, 0], [4, 4, 3], [2, 3, 0], [1, 2, 2]])
B = Matrix([[8, -2, 3], [1, 2, 3], [0, 0, 1]])
v = Vector([1, 1, 1])
print A
print
print A.transpose()
print
print
print A * A.transpose()
print
print B
print
print v
print
print Random(5)
"""
