from matrix import *

#Helpers to isREF
def isLeadOne(A):
    #checking that the first nonzero entry in each row is a 1
    for row in A:
        for c in range(0,len(row)-1):
            if row[c] != 0:
                if row[c] != 1:
                    return False
                else:
                    break
    return True

def isLeadsInOrder(A):
    #checking that the leading entries go from right to left top to bottom
    curr = -1
    for row in A:
        for c in range(0,len(row)-1):
            if row[c] != 0:
                if c > curr:
                    curr = c
                    break
                else:
                    return False
    return True

def isZerosBelow(A):
    #checking that any row with all zeros is at the bottom
    zeros = []
    for i in range(0,len(A[0])-1):
        zeros += [0]
    foundZero = False
    for row in A:
        #row[:-1] excludes the last element in the row
        if row[:-1] == zeros:
            foundZero = True
        #this looks a little weird, but it works
        #this is for later rows, if a zero row was found
        #and then a nonzero row was found, it returns false
        if foundZero == True:
            if row[:-1] != zeros:
                return False
    return True

def isREF(A):
    #Note: this tests if the augmented matrix is in REF
    #this means I am neglecting the last column when doing the checks
    if isMatrix(A) == False:
        return False
    if isLeadOne(A) and isLeadsInOrder(A) and isZerosBelow(A):
        return True
    else:
        return False

#Helpers to isREFF
def isOnlyNonzeroInCol(A):
    for row in range(0, len(A)):
        lead = findLead(A,row)
        if lead != -1:
            for r in range(0,len(A)):
                if r != row:
                    if A[r][lead] != 0:
                        return False
    return True

def isRREF(A):
    if isREF(A) and isOnlyNonzeroInCol(A):
        return True
    return False


#Helpers to GE_fwd and GE_bwd
def findLead(A,row):
    #len(A[0])-1 because it's an augmented matrix
    for c in range(0,len(A[0])-1):
        if A[row][c] != 0:
            return c
    #if it gets all the way through the row without finding a nonzero value
    return -1

#It turns out this function wasn't helpful, but it still works
#so why delete it
def subRowsSmart(A,r1,r2):
    diff = []
    #This is a little more that just a subtracting rows helper function
    #It finds where the first nonzero number is in r2, and subtracts relative to that
    leadPos = findLead(A,r2)
    #if the row is all zeros, return -1
    if  leadPos == -1:
        return A[r2]
    #if that position in r1 happens to be zero we need to break the function
    if A[r1][leadPos] == 0:
        return -1
    for c in range(0,len(A[0])):
        diff += [ A[r2][leadPos]*A[r1][c] - A[r1][leadPos]*A[r2][c] ]
    return diff

def subRows(A,r1,r2,leadPos):
    diff = []
    for c in range(0,len(A[0])):
        diff += [ A[r2][leadPos]*A[r1][c] - A[r1][leadPos]*A[r2][c] ]
    return diff

def pivot(inp,r1,r2):
    A = list(inp)
    if isMatrix(A) == False:
        return -1
    if r1 >= len(A):
        return -1
    if r2 >= len(A):
        return -1
    A[r1] = inp[r2]
    A[r2] = inp[r1]
    return A

#I split it up into two functions because it made
#error checking easier
def normalize_row(inp,r):
    A = list(inp)
    col = findLead(A,r)
    #this is in case the entire row is zeros
    #prevents dividing by zero errors
    if col == -1:
        return A[r]
    out_row = []
    for c in range(0,len(A[0])):
        out_row += [A[r][c]/float(A[r][col])]
    return out_row

#I had to make this stupid out row because for some reason
#A and inp were coupled...i don't know why
#I just know this works
def normalize(inp):
    A = list(inp)
    out = []
    for r in range(0,len(A)):
        out += [normalize_row(A,r)]
    return out


def GE_fwd(inp):
    A = list(inp)
    if isREF(A):
        return A
    
    leadPosRow = 0
    leadPosCol = 0
    while leadPosRow < len(A) and leadPosCol < len(A[0]):
        #first I need to make sure that the leading element is not zero
        #If it is then I need to switch that row with the row below it
        #unless that row also starts with a zero
        #so I have to iterate through the rows until one of them has a row that doesnt start with zero
        #If they all start with zero, I up my leading position and start again
        leadPosCol = 0
        relPosRow = 1
        while A[leadPosRow][leadPosCol] == 0:
            #print leadPosRow,leadPosCol
            #checking if we ran out of rows to swap
            #this means all of the rows start with a zero and our
            #leading collumn has to be shifted by one
            #has to be before the row swapping otherwise the leadPosCol
            #will have an off-by-one error
            if leadPosRow + relPosRow == len(A):
                if relPosRow == 1:
                    break
                leadPosCol += 1
                relPosRow = 1
            #If we get all the way through the columns of the matrix
            #this means the matrix is all zeros below the leadPosRow
            #It's minus 1 bc we are dealing with an augmented matrix
            if leadPosCol == len(A[0])-1:
                break
            #swapping rows
            A = pivot(A, leadPosRow, leadPosRow+relPosRow)
            relPosRow += 1
        
        for r in range(leadPosRow+1,len(A)):
            A[r]=subRows(A,leadPosRow,r,leadPosCol)
        leadPosRow += 1
    A = normalize(A)
    if isREF(A):
        return A
    else:
        return Zero(len(A),len(A[0]))
        
def GE_bwd(inp):
    A = list(inp)
    if isREF(A) == False:
        return Zero(len(A),len(A[0]))
    if isRREF(A):
        return A
    
    #I don't have to worry about ordering stuff because
    #I'm assuming it is already in REF from GE_fwd
    #Which makes my life a lot easier
    for r in range(len(A)-1,0,-1):
        lead = findLead(A,r)
        #if the lead = -1 is means it's an all zero row, which we just skip
        if lead != -1:
            #iterates up the rows
            for i in range(1,r+1):
                A[r-i] = subRows(A,r-i,r,lead)
    #I don't need to normalize because that was already done in GE_fwd
    if isRREF(A):
        return A
    else:
        return Zero(len(A),len(A[0]))

def GE(inp):
    return GE_bwd(GE_fwd(inp))

def Elementary(inp):
    A = list(inp)
    if isSquare(A) == False:
        return []
    E = []

    #GE_fwd
    leadPosRow = 0
    leadPosCol = 0
    E_temp = []
    while leadPosRow < len(A) and leadPosCol < len(A[0]):
        E_temp = []
        leadPosCol = 0
        relPosRow = 1
        while A[leadPosRow][leadPosCol] == 0:
            if leadPosRow + relPosRow == len(A):
                if relPosRow == 1:
                    break
                leadPosCol += 1
                relPosRow = 1
            if leadPosCol == len(A[0])-1:
                break
            #swapping rows
            A = pivot(A, leadPosRow, leadPosRow+relPosRow)               
            E_temp = [pivot(Iden(len(A)), leadPosRow, leadPosRow+relPosRow)] + E_temp
            relPosRow += 1
        
        E = [multL(E_temp)] + E
        
        for r in range(leadPosRow+1,len(A)):
            I = Iden(len(A))
            A[r] = subRows(A,leadPosRow,r,leadPosCol)
            I[r] = subRows(I,leadPosRow,r,leadPosCol)
            E = [I] + E
        leadPosRow += 1
    #gotta account for this whole normalizing the rows business
    A = normalize(A)
    
    #GE_bwd
    for r in range(len(A)-1,0,-1):
        lead = findLead(A,r)
        if lead != -1:
            A[r-1] = subRows(A,r-1,r,lead)

A = [[1,1,0,0,0], [0,0,1,-1,0], [0,1,1,0,0], [1,0,0,0,-1], [0,0,0,-1,1]]
B = [20,-20,20,-10,-10]

C = [[2, -4, 4, 0], [1, 1, 5, 3], [1, -1, 3, 1], [1, 1, 1, 1]]
Mprint(aug(GE(C), [0,0,0,0]))

"""
print "Original Matrix"
C = augment(A,B)
Mprint(C)
print
print "REF"
F = GE_fwd(C)
MprintI(F)
print
print "RREF"
G = GE_bwd(F)
MprintI(G)
"""
