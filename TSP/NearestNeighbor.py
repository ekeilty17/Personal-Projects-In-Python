from graph import *

#helper
def distance(p1, p2):
    return ((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)**(0.5)

def makeGraph(P):
    G = graph()
    G.addVertex(len(P))
    for i in range(0,len(P)):
        for j in range(i,len(P)):
            #G.addEdge(i%len(P),(i+1)%len(P),True,distance(P[i%len(P)],P[(i+1)%len(P)]))
            G.addEdge(i,j,False,distance(P[i],P[j]))
    return G

#something is wrong with the last step
def NearestNeighbor(P, start):
    G = makeGraph(P)
    if start < 0 or start >= len(G.adj):
        return False
    
    def closest(adj):
        weights = []
        for V in adj:
            weights += [V[1]]
        return weights.index(min(weights))

    visited_points = [start]
    i = start #index of point we are on
    while len(visited_points) < len(G.adj):
        p_next = G.adj[i][closest(G.adj[i])][0]
        visited_points += [p_next]
        G.removeEdge(i,p_next)
        G.removeEdge(p_next,i)
        i = p_next
    out = []
    for i in visited_points:
        out += [P[i]]
    return out


P = [(0,0), (1,1), (-1,1), (0,2)] 
print P
print NearestNeighbor(P,0)
print
P = [(-21,0), (11,0), (0,0), (-5,0), (1,0), (-1,0), (3,0)]
print P
print NearestNeighbor(P,0)
print
P = [(0,0), (-23,0), (12,0), (1,0), (-5,0), (-1,0), (3,0)]
print P
print NearestNeighbor(P,0)
