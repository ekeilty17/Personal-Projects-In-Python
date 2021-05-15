from makeFrame import *

#This is a strange version of bubble sort, but it works
def bubblesort(inp):
    #some error checks if they are needed
    try:
        A = list(inp)
    except:
        return False
    
    if A == []:
        return False
    if len(A) == 1:
        return False
    
    for i in A:
       if (type(i) != int):
           return False

    cnt = 0
    swapped = True
    while swapped:
        swapped = False
        for i in range(1,len(A)):
            if A[i-1] > A[i]:
                temp = A[i-1]
                A[i-1] = A[i]
                A[i] = temp
                swapped = True
                makeFrame(A)
    return A

#the way people normally do bubble sort
def bubblesort2(inp):
    A = list(inp)
    cnt = 0
    for i in range(0,len(A)-1):
        for j in range(1,len(A)-i):
            if A[j-1] > A[j]:
                temp = A[j-1]
                A[j-1] = A[j]
                A[j] = temp
                makeFrame(A)
    return A
