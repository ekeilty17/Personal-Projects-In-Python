from makeFrame import *

def selection_sort(u):
    min_idx = -1
    for i in range(0,len(u)):
        min_idx = i
        for j in range(i,len(u)):
            if u[min_idx] > u[j]:
                min_idx = j
        temp = u[i]
        u[i] = u[min_idx]
        u[min_idx] = temp
        makeFrame(u)
    return True
