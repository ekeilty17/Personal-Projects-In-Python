class Matrix():

    def __init__(self, L):
        error = False
        if type(L) != list:
            raise TypeError("Input not a 2-dim list.")
            error = True
        row_len = L[0]
        for r in L:
            if type(r) != list:
                raise TypeError("Input not a 2-dim list.")
                error = True
                break
            if len(r) != len(row_len):
                raise TypeError("Rows do not contain the same number of elements.")
                error = True
                break
            for e in r:
                if type(e) != int and type(e) != float:
                    raise TypeError("Elements are not integers.")
                    error = True
        if not error:
            self.store = L
        else:
            self.store = [[]]

    def get(self,acc=4):
        out = ""
        for row in self.store:
            row_str = ""
            for j in range(0,len(row)):
                if row[j] >= 0:
                    row_str += ' '
                if row[j] == 0:
                    row_str += str(abs(round(row[j],acc)))
                else:
                    row_str += str(round(row[j],acc))
                if (j != len(row)-1):
                    row_str += '\t'
            out += row_str + '\n'
        return out[:-1]

    #I wasn't sure the best way to do this
    #I think just returning a row vector is probably easiest
    def getRow(self,r):
        if not (0 < r <= len(self.store)):
            raise TypeError("Index out of range.")
            return []
        return self.store[r-1]
    
    def getCol(self,c):
        if not (0 < c <= len(self.store[0])):
            raise TypeError("Index out of range.")
            return []
        out = []
        for i in range(len(self.store)):
            out += [self.store[i][c-1]]
        return out
    
    def deleteRow(self,r):
        if not (0 < r <= len(self.store)):
            raise TypeError("Index out of range.")
            return self
        self.store = self.store[:r-1] + self.store[r:]
        return self

    def deleteCol(self,c):
        if not (0 < c <= len(self.store[0])):
            raise TypeError("Index out of range.")
            return self
        for i in range(len(self.store)):
            self.store[i] = self.store[i][:c-1] + self.store[i][c:]
        return self

    def set(self,L):
        error = False
        if type(L) != list:
            raise TypeError("Input not a 2-dim list.")
            error = True
        row_len = len(L[0])
        for r in L:
            if type(r) != list:
                raise TypeError("Input not a 2-dim list.")
                error = True
                break
            if len(r) != row_len:
                raise TypeError("Rows do not contain the same number of elements.")
                error = True
                break
            for e in r:
                if type(e) != int and type(e) != float:
                    raise TypeError("Elements are not integers.")
                    error = True
        if not error:
            self.store = L

    def copy(self):
        return Matrix(list(self.store))
    
    def dim(self):
        #m x n denotes rows x cols is the usual convension
        #this return [m, n]
        return [len(self.store),len(self.store[0])]
    
    def isSquare(self):
        if len(self.store) == len(self.store[0]):
            return True
        return False

    def scale(self,k):
        for r in range(len(self.store)):
            for c in range(len(self.store[r])):
                self.store[r][c] *= k
        return self
    
    def transpose(self):
        out = []
        for c in range(len(self.store[0])):
            temp = []
            for r in range(len(self.store)):
                temp += [self.store[r][c]]
            out += [temp]
        return Matrix(out)
    
    def submatrix(self,r,c):
        if not (0 < r <= len(self.store)):
            raise TypeError("Row index is out of range.")
            return None
        if not (0 < c <= len(self.store[0])):
            raise TypeError("Column index is out of range.")
            return None

        row = r-1
        col = c-1
        #getting rid of rth row
        out = self.store[:row] + self.store[row+1:]
        #getting rid of cth col
        for i in range(len(out)):
            out[i] = out[i][:col] + out[i][col+1:]
        return Matrix(out)
    
    def Det(self):
        if not self.isSquare():
            raise TypeError("Determinant is only defined for square matrices.")
            return -1
        if len(self.store) == 1:
            return self.store[0][0]
        if len(self.store) == 2:
            return self.store[0][0]*self.store[1][1] - self.store[0][1]*self.store[1][0]
        else:
            accum = 0
            for i in range(len(self.store)):
                #The Laplace Expansion gives us a lot of flexibility
                #I am iterating over the ith row and 0th col
                accum += ((-1)**(i+1+0+1))*self.store[i][0]*self.minor(i+1,0+1)
            return accum

    def minor(self,r,c):
        return self.submatrix(r,c).Det()
    
    def cof(self,r,c):
        return (-1)**(r+c) * self.minor(r,c)
    
    def cofactor_matrix(self):
        out = []
        for i in range(len(self.store)):
            temp = []
            for j in range(len(self.store[i])):
                temp += [self.cof(i+1,j+1)]
            out += [temp]
        return Matrix(out)

    def adj(self):
        return self.cofactor_matrix().transpose()
    
    def Inverse(self):
        if not self.isSquare():
            raise TypeError("Inverse is only defined for square matrices.")
            return None
        if self.Det() == 0:
            raise TypeError("Inverse does not exist.")
            return None
        return self.adj().scale(1/float(self.Det()))

#Operations between Matrices
def add(A,B):
    if not isinstance(A, Matrix) or not isinstance(B, Matrix):
        raise TypeError("Arguements are not matrices.")
        return None
    if A.dim() != B.dim():
        raise TypeError("Dimensions of matrices do not match.")
        return None
    
    out = []
    for i in range(len(A.store)):
        temp = []
        for j in range(len(A.store[i])):
            temp += [A.store[i][j] + B.store[i][j]]
        out += [temp]
    return Matrix(out)

def subtract(A,B):
    return add(A,B.copy().scale(-1))

def multiply(A,B):
    if not isinstance(A, Matrix) or not isinstance(B, Matrix):
        raise TypeError("Arguements are not matrices.")
        return None
    if A.dim()[1] != B.dim()[0]:
        raise TypeError("Dimensions of matrices do not agree.")
        return None
    
    out = []
    B_t = B.transpose()
    for i in range(len(A.store)):
        temp = []
        for j in range(len(B_t.store)):
            accum = 0
            for k in range(len(A.store[i])):    #using the fact row(A) == col(B)
                accum += A.store[i][k] * B_t.store[j][k]
            temp += [accum]
        out += [temp]
    return Matrix(out)

def multiply_list(L):
    if len(L) == 1:
        return L[0]
    out = L[-1]
    for i in range(len(L)-2,-1,-1):
        out = multiply(L[i], out)
    return out

def augment(A,B):
    if not isinstance(A, Matrix) or not isinstance(B, Matrix):
        raise TypeError("Arguements are not matrices.")
        return None
    if A.dim()[0] != B.dim()[0]:
        raise TypeError("Dimensions of matrices do not agree.")
        return None
    out = []
    for i in range(len(A.store)):   #row(A) == row(B)
        out += [A.store[i] + B.store[i]]
    return Matrix(out)
