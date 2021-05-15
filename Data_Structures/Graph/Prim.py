from graph import Graph

def Prim(G, s):
    # Initialize all distances as infinite (represented with -1)
    dist = [-1] * len(G)
    # Initialize all paths as undefined
    parents = [-1] * len(G)

    dist[s] = 0
    Q = list(range(len(G)))

    while len(Q) != 0:
        
        # Getting minimum distance edge in Q
        u = -1
        min_dist = -1
        for v in Q:
            if dist[v] == -1:
                continue
            if u == -1 or dist[v] < min_dist:
                u = v
                min_dist = dist[v]

        for v, w in G.Adj[u]:
            if v in Q and ( dist[v] == -1 or w < dist[v] ):
                dist[v] = w
                parents[v] = u
        Q.remove(u)
    
    E = []
    for v, p in enumerate(parents):
        if p == -1:
            continue
        E.append( (p, v) )
    return E, sum(dist)

if __name__ == "__main__":
    G = Graph()

    G.addVertex(N=9, names=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i'])

    G.addEdge(0, 1, False, 4)
    G.addEdge(0, 7, False, 8)

    G.addEdge(1, 2, False, 8)
    G.addEdge(1, 7, False, 11)

    G.addEdge(2, 3, False, 7)
    G.addEdge(2, 5, False, 4)
    G.addEdge(2, 8, False, 2)

    G.addEdge(3, 4, False, 9)
    G.addEdge(3, 5, False, 14)

    G.addEdge(4, 5, False, 10)
    G.addEdge(5, 6, False, 2)

    G.addEdge(6, 7, False, 1)
    G.addEdge(6, 8, False, 6)

    G.addEdge(7, 8, False, 7)
    
    #print(G)

    E, weight = Prim(G, 0)
    E_named = [(G.Names[u], G.Names[v]) for u, v in E]
    print(E_named, weight)