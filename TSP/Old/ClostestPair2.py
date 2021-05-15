#this code is based on my initial misunderstanding of the ClosestPair algorithm
#while this isn't how the original algorithm was designed to work, 
#I didn't want to just delete it

def ClosestPair(P):

    def distance(p1, p2):
        return ((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)**(0.5)
    
    def minPair(P):
        if len(P) == 0:
            return []
        if len(P) == 1:
            return [P[0]]
        if len(P) == 2:
            return P
        min_distance = distance(P[0],P[1])
        min_pair_index = [0,1]
        for i in range(0,len(P)-1):
            for j in range(i+1, len(P)):
                if distance(P[i],P[j]) < min_distance:
                    min_distance = distance(P[i],P[j])
                    min_pair_index = [i,j]
        return [P[min_pair_index[0]], P[min_pair_index[1]]]
    
    #first we need to get a list of the shortest connections
    n = len(P)
    pairs = []
    #there is either an odd number of points or an even number of points
    #once we get to len(P) == 2 or len(P) == 1, we just add whats left of P
    #to the end of pairs
    while len(P) > 2:
        c = minPair(P)
        print c
        pairs += [c]
        P.remove(c[0])
        P.remove(c[1])
    pairs += [P]
    
    #now that we have pairs, we need to find the best way to connect them
    
    return pairs

"""
P = [(0,0), (1,1), (-1,1), (0,2)]
print ClosestPair(P)
print
"""
P = [(-21,0), (11,0), (0,0), (-5,0), (1,0), (-1,0), (3,0)]
print ClosestPair(P)
print
"""
P = [(0,0), (-23,0), (12,0), (1,0), (-5,0), (-1,0), (3,0)]
print ClosestPair(P)
"""
