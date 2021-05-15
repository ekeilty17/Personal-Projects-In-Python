from makeFrame import *

def cocktailsort(A):
    swapped = True
    while swapped:
        swapped = False
        for i in range(1,len(A)):
            if A[i-1] > A[i]:
                temp = A[i-1]
                A[i-1] = A[i]
                A[i] = temp
                swapped = True
                #makeFrame(A)
        if not swapped:
            break
        swapped = False
        for i in range(len(A)-1, 0, -1):
            if A[i-1] > A[i]:
                temp = A[i-1]
                A[i-1] = A[i]
                A[i] = temp
                swapped = True
                #makeFrame(A)
    return A
