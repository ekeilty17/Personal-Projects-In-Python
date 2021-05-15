def PathDistance(P):
    
    def distance(p1, p2):
        return ((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)**(0.5)
    
    accum = 0
    for i in range(0,len(P)-1):
        accum += distance(P[i],P[i+1])
    if len(P) > 2:
        accum += distance(P[len(P)-1],P[0])
    return accum
