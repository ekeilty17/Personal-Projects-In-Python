from makeFrame import *

def slowsort_rec(A, i, j):
    if i >= j:
        return True

    m = (i+j)/2
    slowsort_rec(A,i,m)
    slowsort_rec(A,m+1,j)

    if A[j] < A[m]:
        temp = A[j]
        A[j] = A[m]
        A[m] = temp
        makeFrame(A)

    slowsort_rec(A,i,j-1)
    return True

def slowsort(A):
    return slowsort_rec(A, 0, len(A)-1)
