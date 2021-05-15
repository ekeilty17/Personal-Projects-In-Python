from subset import *

# Counts the number of elements in u that are also in S
def CoverNum(u, E):
    # u is the 'reduced universal set'
    # E = element in the set S (which is a set) that we are analyzing
    cnt = 0
    for e in E.getElements():
        if e in u:
            cnt += 1
    return cnt

# Algorithm choses that set that will cover the most elements in the universal set
def greedy(U, S, coverage):
    # U = universal set
    # S = set of subsets
    # coverage = percent of U that we want to over with sets in S
    
    u = U.copy()
    # u is the 'reduced universal set'
    #   As we cover more elements, we remove elements that have already been covered
    s = S.copy()
    # s is the 'reduced set of subsets'
    #   As we choose sets, we need to remove ones that we have alreayd used
    
    Cover = set([])
    # Output of the function

    alpha = 1 - float(len(u))/float(len(U))

    while alpha < coverage:
        
        # Getting set with largest cover
        best_cover_cnt = 0
        best_cover_set = None
        for E in s:
            if CoverNum(u, E) > best_cover_cnt:
                best_cover_cnt = CoverNum(u, E)
                best_cover_set = E
        
        
        # If no more sets cover U, then end the loop
        if best_cover_cnt == 0:
            break

        Cover.add(best_cover_set)                       # Adding chosen set to output
        u = u.difference(best_cover_set.getElements())  # removing covered elements
        s.remove(best_cover_set)                        # removing chosen set from list of next possible sets

        alpha = 1 - float(len(u))/float(len(U))

    return Cover

