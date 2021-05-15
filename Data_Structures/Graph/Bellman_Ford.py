from graph import Graph

def Bellman_Ford(G, s):
    # Initialize all distances as infinite (represented with -1)
    dist = [None] * len(G)
    # Initialize all paths as undefined
    path = [[]] * len(G)

    dist[s] = 0
    path[s] = [s]

    for i in range(len(G)-1):
        for u, v, w in G.E():
            # Relax edge (u, v)
            if (dist[v] == None and dist[u] != None) or dist[v] > dist[u] + w:
                dist[v] = dist[u] + w
                path[v] = path[u] + [v]
    
    # checking for negative cycles
    for u, v, w in G.E():
        if dist[v] > dist[u] + w:
            return None, []
    
    return dist, path

if __name__ == "__main__":
    G = Graph()
    G.addVertex(N=5, names=['s', 't', 'x', 'y', 'z'])
    
    G.addEdge(0, 1, True, 6)
    G.addEdge(0, 3, True, 7)

    G.addEdge(1, 2, True, 5)
    G.addEdge(1, 3, True, 8)
    G.addEdge(1, 4, True, -4)

    G.addEdge(2, 1, True, -2)

    G.addEdge(3, 2, True, -3)
    G.addEdge(3, 4, True, 9)

    G.addEdge(4, 0, True, 2)
    G.addEdge(4, 2, True, 7)

    #print(G)
    #print(G.E())

    dist, path = Bellman_Ford(G, 0)
    for d, p in zip(dist, path):
        print(f"distance: {d}, path: {' --> '.join([G.Names[v] for v in p])}")
