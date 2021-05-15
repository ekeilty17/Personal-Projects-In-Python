#does not require any helper files

def Dijkstra(G,start):
    N = len(G.adj)

    L = range(0,N)
    dist = [-1]*N # we'll call this infinity since -1 doesn't overlap legit values of dist
    prev = [-1]*N # we'll call this undefined since -1 doesn't overlap legit values of vertex indices

    dist[start] = 0
    while len(L) != 0:
        # I: find minIdx in L s.t. dist[minIdx] is minimized
        minDist = -1
        minIdx  = -1
        for i in L:
            if dist[i] !=  -1:
                if (minDist == -1) or ((minDist != -1) and (dist[i] < minDist)):
                    minDist = dist[i]
                    minIdx  = i
        if minIdx == -1:
            return [False,dist,prev]

        # II: remove minIdx from L
        L.remove(minIdx)

        # III:  for all neighbors,x, of minIdx that are in L
        #           if d < dist[minIdx]:
        #               update dist[x] = d
        #               update prev[x] = minIdx
        for x in sorted(G.adj[minIdx]):
            if x[0] in L: # x[0] is the vertex
                d = minDist + x[1] # x[1] is the weight

                if (dist[x[0]] == -1) or ((dist[x[0]] != -1) and (d < dist[x[0]])):
                    dist[x[0]] = d
                    prev[x[0]] = minIdx
    return [dist, prev]

#not done
def ShortestPath(G,v0,vf):
    out = Dijkstra(G,v0)
    return False
