#something is wrong with the last step
def NearestNeighbor(P):
    
    def distance(p1, p2):
        return ((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)**(0.5)
    
    def closest(P, i):
        if len(P) == 1:
            return 0
        #P is the list of points
        #i is the reference point
        min_distance = distance(P[i], P[(i+1)%len(P)])
        #this is initialized weird bc it's the only one
        #I could come up with that worked every time
        #have to do the % len(P) in case i is the last index
        min_distance_index = (i+1)%len(P)
        for j in range(0,len(P)):
            if j != i: #if j == i, distance(P[i], P[j]) = 0
                if distance(P[i], P[j]) < min_distance:
                    min_distance = distance(P[i], P[j])
                    min_distance_index = j
        return min_distance_index

    visited_points = [P[0]] #assuming P[0] is starting point
    n = len(P)
    i = 0 #index of point we are on
    while len(visited_points) < n:
        c = closest(P, i)
        p_next = P[c]
        visited_points += [p_next]
        del P[i]
        i = P.index(p_next)
    return visited_points

P = [(0,0), (1,1), (-1,1), (0,2)]
print NearestNeighbor(P)
print
P = [(-21,0), (11,0), (0,0), (-5,0), (1,0), (-1,0), (3,0)]
print NearestNeighbor(P)
print
P = [(0,0), (-23,0), (12,0), (1,0), (-5,0), (-1,0), (3,0)]
print NearestNeighbor(P)
