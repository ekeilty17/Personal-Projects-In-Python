#error checks
def isMatrix(A):
    if A == []:
        return False
    if type(A) != list:
        return False
    if type(A[0]) != list:
        return False
    
    for i in range(0,len(A)):
        if len(A[0]) != len(A[i]):
                return False
    return True

def isSquare(A):
    if isMatrix(A) == False:
        return False
    if len(A) != len(A[0]):
        return False
    return True

def isOrthogonal(A):
    if isSquare(A) == False:
        return False
    if (multiply(A,transpose(A)) == multiply(transpose(A),A)):
        return True
    else:
        return False


#to diplay matrices nicely
def Mprint(A):
    if isMatrix(A) == False:
        return False
    for row in A:
        row_str = ''
        for j in range(0,len(row)):
            #adds a space to make the negatives line up
            if row[j] >= 0:
                row_str += ' '
            #sometimes you can get -0 in python
            #this makes that go away
            if row[j] == 0:
                row_str += str(abs(row[j]))
            else:
                row_str += str(row[j])
            if (j != len(row)-1):
                row_str += '\t'
        print row_str
    return True

#If you know the matrix is all integers, then sometimes
#it's nice to print it without the .0 after
def MprintI(A):
    if isMatrix(A) == False:
        return False
    for row in A:
        row_str = ''
        for j in range(0,len(row)):
            #adds a space to make the negatives line up
            if row[j] >= 0:
                row_str += ' '
            #sometimes you can get -0 in python
            #this makes that go away
            if row[j] == 0:
                row_str += str(int(abs(row[j])))
            else:
                row_str += str(int(row[j]))
            if (j != len(row)-1):
                row_str += '\t'
        print row_str
    return True

def Mprintf(A,acc):
    if isMatrix(A) == False:
        return False
    for row in A:
        row_str = ''
        for j in range(0,len(row)):
            if row[j] >= 0:
                row_str += ' '
            if row[j] == 0:
                row_str += str(abs(round(row[j],acc)))
            else:
                row_str += str(round(row[j],acc))
            if (j != len(row)-1):
                row_str += '\t'
        print row_str
    return True

def MLprint(S):
    #checks if all elements are matrices
    for A in S:
        if isMatrix(A) == False:
            return False
    for A in S:
        Mprint(A)
        print
    return True

def MLprintf(S,acc):
    #checks if all elements are matrices
    for A in S:
        if isMatrix(A) == False:
            return False
    for A in S:
        Mprintf(A,acc)
        print
    return True

def MLprintf(S,acc):
    #checks if all elements are matrices
    for A in S:
        if isMatrix(A) == False:
            return False
    for A in S:
        Mprintf(A,acc)
        print
    return True


#Basic types of matrices
def Iden(n):
    I = []
    for i in range(0,n):
        I_row = []
        for j in range(0,n):
            if (i == j):
                I_row += [1]
            else:
                I_row += [0]
        I += [I_row]
    return I

def Zero(n,m):
    zero = []
    for i in range(0,n):
        zero_row = []
        for j in range(0,m):
            zero_row += [0]
        zero += [zero_row]
    return zero


#operations on 2 matrices
def add(A,B):
    if ((isMatrix(A) == False) or (isMatrix(B) == False)):
        return False
    if len(A) != len(B):
        return False
    
    out = list(A)
    for r in range(0,len(A)):
        for c in range(0,len(A[r])):
            if (len(A[r]) != len(B[r])):
                return False
            out[r][c] += B[r][c]
    return out

def subtract(A,B):
    if ((isMatrix(A) == False) or (isMatrix(B) == False)):
        return False
    if len(A) != len(B):
        return False
    
    out = list(A)
    for r in range(0,len(A)):
        for c in range(0,len(A[r])):
            if (len(A[r]) != len(B[r])):
                return False
            out[r][c] -= B[r][c]
    return A

def scalar(k,A):
    if isMatrix(A) == False:
        return False
    out = list(A)
    for i in range(0,len(A)):
        for j in range(0,len(A[0])):
            out[i][j] = k*out[i][j]
    return out

#I took this from my vector.py code
#this is just to make the multiply function nicer looking
def dot(v,w):
    if len(v) != len(w):
        return False

    accum = 0
    for i in range(0,len(v)):
        accum += v[i]*w[i]
    return accum


def multiply(A,B):
    if ((type(A) != list) or (type(B) != list)):
        return False
    if ((type(A[0]) != list) or (type(B) != list)):
        return False
    if len(A[0]) != len(B):
        return False
    
    mult = []
    for i in range(0,len(A)):
        row_mult = []
        for j in range(0,len(B[0])):
            B_COL = getCol(B,j+1)
            B_col2row = []
            for k in range(0,len(B_COL)):
                B_col2row += B_COL[k]
            row_mult += [dot(A[i],B_col2row)]
        mult += [row_mult]
    return mult

#A function that takes a list of matrices and multiplies them
#This multiplies the list the way you would on paper
#so it actually does it right to left
def Lmult(S):
    #checks if all matrices are square with the same dimension
    dim = len(S[0])
    for A in S:
        if isSquare(A) == False:
            return False
        if len(A) != dim:
            return False
    T = Iden(dim)
    for i in range(len(S)-1, -1, -1):
        T = multiply(S[i],T)
    return T


#operations on a single matrix
def getRow(A,row):
    if isMatrix(A) == False:
        return False
    if row-1 > len(A[0]):
        return False
    return A[row-1]

def getCol(A,col):
    if isMatrix(A) == False:
        return False
    if col-1 > len(A[0]):
        return False
    
    temp = []
    for r in range(0,len(A)):
        temp += [[A[r][col-1]]]
    return temp

def transpose(A):
    if isMatrix(A) == False:
        return False
    
    out = []
    for c in range(0,len(A[0])):
        temp = []
        for r in range(0,len(A)):
            temp += [A[r][c]]
        out += [temp]
    return out


def Det(A):
    if isSquare(A) == False:
        return False
    if len(A) == 1:
        return A[0][0]
    if len(A) == 2:
        return A[0][0]*A[1][1] - A[0][1]*A[1][0]
    else:
        sum = 0
        for i in range(0,len(A)):
            sum += ((-1)**(i+1+0+1))*A[i][0]*minor(A,i+1,0+1)
        return sum

def cofactorSubmatrix(A,r,c):
    row = r-1
    col = c-1
    if row > len(A)-1:
        return False
    if col > len(A[0])-1:
        return False
    
    out = []
    for i in range(0,len(A)):
        temp_row = []
        for j in range(0,len(A)):
            if ((i != row) and (j != col)):
                temp_row += [A[i][j]]
        if temp_row != []:
            out += [temp_row]
    return out

def minor(A,r,c):
    return Det(cofactorSubmatrix(A,r,c))

def cofactor(A):
    if isSquare == False:
        return False

    out = []
    for i in range(0,len(A)):
        temp_row = []
        for j in range(0,len(A)):
            temp_row += [((-1)**(i+1+j+1))*minor(A,i+1,j+1)]
        out += [temp_row]
    return out

def adjoint(A):
    out = transpose(cofactor(A))
    return out
def adjugate(A):
    return adjoint(A)
def adj(A):
    return adjoint(A)

def Inverse(A):
    if Det(A) == 0:
        return False
    if isSquare(A) == False:
        return False
    out = scalar(1/float(Det(A)), adjoint(A))
    return out
def inv(A):
    return Inverse(A)


def augment(A,B):
    #a bunch of checks
    if isMatrix(A) == False:
        return False
    if type(B) != list:
        return False
    for e in B:
        if len(A) != len(B):
            return False
    out = []
    if type(B[0]) == list:
        for i in range(0,len(A)):
            out += [A[i] + B[i]]
        return out
    elif type(B[0]) == int:
        for i in range(0,len(A)):
            out += [A[i] + [B[i]]]
        return out
    else:
        return False
def aug(A,B):
    return augment(A,B)


"""
A1 = [[-1,0],[0,1]]
A2 = [[1,0],[3,1]]
A3 = [[1,0],[0,2]]
A4 = [[1,2],[0,1]]

A = multiply(A3,A4)
A = multiply(A2,A)
A = multiply(A1,A)

Mprint(A)
print
print
print

A = Lmult([A1,A2,A3,A4])
Mprint(A)
MLprint([A1,A2,A3,A4])
"""
