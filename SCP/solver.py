from subset import * 
from greedy import *
from greedyCost import *

def DisplayCover(U, Cover):
    print
    print "\nSets Chosen: "
    for E in Cover:
        E.Display()
    print
    print "Cover: "
    print "\tU:\t" + str(U)

    cover_union = set([])
    for E in Cover:
        cover_union = cover_union.union(E.getElements())
    print "\tCover:\t" + str(cover_union)
    print
    print "Percent Covered = " + str( round(100 * float(len(cover_union))/float(len(U)), 2) )


U = set(range(1, 14))

E1 = subset(5, set([1, 2]))
E2 = subset(10, set([2, 3, 4, 5]))
E3 = subset(3, set([6, 7, 8, 9, 10, 11, 12, 13]))
E4 = subset(1, set([1, 3, 5, 7, 9, 11, 13]))
E5 = subset(1, set([2, 4, 6, 8, 10, 12, 13]))
S = set([E1, E2, E3, E4, E5])

Cover = greedy(U, S, 1.0)
DisplayCover(U, Cover)
print
