from makeFrame import *

def insertionsort(inp):
    A = list(inp)
    for i in range(1,len(A)):
        j = i
        while (j>0) and (A[j] < A[j-1]):
            temp = A[j-1]
            A[j-1] = A[j]
            A[j] = temp
            j -= 1
            makeFrame(A)
    return A
