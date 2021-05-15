from makeFrame import *

def merge(u, left, middle, right):
    makeFrame(u)

    L = []
    sizeL = middle - left + 1
    for i in range(0,sizeL):
        L += [u[left + i]]

    R = []
    sizeR = right - middle
    for i in range(0,sizeR):
        R += [u[middle + 1 + i]]

    l = 0
    r = 0
    a = left
    while (l < sizeL and r < sizeR):
        if L[l] <= R[r]:
            u[a] = L[l]
            l += 1
        else:
            u[a] = R[r]
            r += 1
        a += 1
        makeFrame(u)

    while l < sizeL:
        u[a] = L[l]
        l += 1
        a += 1
        makeFrame(u)
    while r < sizeR:
        u[a] = R[r]
        r += 1
        a += 1
        makeFrame(u)

    return True

def merge_sort_rec(u, left, right):
    if (left >= right):
        return True
    middle = left + (right - left)/2

    merge_sort_rec(u, left, middle)
    merge_sort_rec(u, middle+1, right);

    merge(u, left, middle, right)
    return True

def merge_sort(u):
    return merge_sort_rec(u, 0 ,len(u)-1)
