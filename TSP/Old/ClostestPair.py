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
    
    def minConnect(pairs):
        if len(pairs) == 0:
            return []
        if len(pairs) == 1:
            return [pairs[0]]
        if len(pairs) == 2:
            return pairs
        n = len(pairs[0])
        min_distance = distance(pairs[0][n-1],pairs[1][0])
        min_pair_index = [0,1]
        for i in range(0,len(pairs):
            for j in range(0, len(pairs)):
                if distance(pairs[i][n-1],pairs[j][0]) < min_distance:
                    min_distance = distance(pairs[i][n-1],pairs[j][0])
                    min_pair_index = [i,j]
        return [min_pair_index[0], min_pair_index[1]]

    #first we need to get a list of the shortest connections
    n = len(P)
    out = [minPair(P)] #initialize with the closest pair
    while len(P) != 0:
        c = minPair(P)
        print c
        pairs += [c]
        P.remove(c[0])
        P.remove(c[1])
    pairs += [P]
    
    #now that we have pairs, we need to find the best way to connect them
    i = minConnect(pairs)
    c = [pairs[i[0]], pairs[i[1]]]
    pairs = pairs
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
