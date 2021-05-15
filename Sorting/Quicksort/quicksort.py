from makeFrame import *

def partition(A, lo, hi):
    pivot = A[lo]
    i = lo - 1
    for j in range(lo, hi+1):
        if A[j] < pivot:
            i += 1
            temp = A[i]
            A[i] = A[j]
            A[j] = temp
            makeFrame(A)
    if A[hi] < A[i+1]:
        temp = A[i+1]
        A[i+1] = A[hi]
        A[hi] = temp
        makeFrame(A)
    return i+1    

def quicksort_rec(A, lo, hi):
    if lo < hi:
        p = partition(A, lo, hi)
        quicksort_rec(A, lo, p-1)
        makeFrame(A)
        quicksort_rec(A, p+1, hi)
        makeFrame(A)
    return A

def quicksort(A):
    makeFrame(A)
    return quicksort_rec(A, 0, len(A)-1)
