from makeFrame import *

def error(u):
    if type(u) != list:
        return True
    if u == []:
        return True
    for e in u:
        if type(e) != int:
            return True
    return False

def parent(n):
    if n < 1:
        return -1;
    if n%2 == 0:
        return (n-2)/2
    else:
        return (n-1)/2

def bubble_up(u, c):
    if parent(c) == -1:
        return True
    if u[parent(c)] < u[c]:
        temp = u[c]
        u[c] = u[parent(c)]
        u[parent(c)] = temp
        makeFrame(u)
        bubble_up(u, parent(c))
    return True

def heapify(u):
    if error(u):
        return False
    for i in range(1,len(u)):
        bubble_up(u, i)
    return True

def bubble_down(u, p, end):
    if p < 0:
        return False
    
    min_idx = p
    if (2*p+1) < end:
        if u[min_idx] < u[2*p+1]:
            min_idx = 2*p+1
    if (2*p+2) < end:
        if u[min_idx] < u[2*p+2]:
            min_idx = 2*p+2

    if min_idx != p:
        temp = u[p]
        u[p] = u[min_idx]
        u[min_idx] = temp
        makeFrame(u)
        bubble_down(u, min_idx, end)
    return True

def reheapify(u,end):
    if error(u):
        return False
    bubble_up(u,end)
    return True

def heapsort(u):
    if error(u):
        return False
    heapify(u)
    for i in range(0,len(u)):
        temp = u[0]
        u[0] = u[len(u)-1-i]
        u[len(u)-1-i] = temp
        makeFrame(u)

        bubble_down(u, 0, len(u)-i-1)
    return True
