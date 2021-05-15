from graph import Graph

def residual_graph(G, flow):

    G_f = Graph()
    G_f.addVertex(N=len(G), names=G.Names)

    for u, v, capacity in G.E():
        inc = capacity - flow[u][v]
        dec = flow[u][v]

        if inc != 0:
            G_f.addEdge(u, v, True, inc)
        if dec != 0:
            G_f.addEdge(v, u, True, dec)

    return G_f

def Ford_Fulkerson(G, s, t):

    # initializing flows
    flow = [ [0] * len(G) for _ in G ]

    G_f = residual_graph(G, flow)
    paths = G_f.AllPaths(s, t)
    while len(paths) != 0:
        
        # pick some path from s --> t
        p = paths[0]

        # get minimum capacity edge (bottle neck)
        path_edges = list(zip(p[::], p[1::]))
        min_edge = min(path_edges, key=lambda e: G_f.getWeight(*e))
        c_f = G_f.getWeight(*min_edge)

        # update flows
        for u, v in path_edges:
            if G.getWeight(u, v) != 0:
                flow[u][v] += c_f

        # update residual graph
        G_f = residual_graph(G, flow)
        paths = G_f.AllPaths(s, t)
    
    # max_flow is the sum of the flows coming out ofs t of the final G_f
    return sum([ w for v, w in G_f.Adj[t] ])

# Only difference between Edmonds-Karp and Ford-Fulkerson algorithm is we use a BFS to find the augmenting path
def Edmonds_Karp(G, s, t):

    # initializing flows
    flow = [ [0] * len(G) for _ in G ]

    G_f = residual_graph(G, flow)
    paths = G_f.BFS(s)
    p = paths[t]
    while p != [t]:
        
        # get minimum capacity edge (bottle neck)
        path_edges = list(zip(p[::], p[1::]))
        min_edge = min(path_edges, key=lambda e: G_f.getWeight(*e))
        c_f = G_f.getWeight(*min_edge)

        # update flows
        for u, v in path_edges:
            if G.getWeight(u, v) != 0:
                flow[u][v] += c_f

        # update residual graph
        G_f = residual_graph(G, flow)
        p = G_f.BFS(s)[t]
    
    # max_flow is the sum of the flows coming out ofs t of the final G_f
    return sum([ w for v, w in G_f.Adj[t] ])

if __name__ == "__main__":
    G = Graph()

    G.addVertex(N=6, names=['s', 'v1', 'v2', 'v3', 'v4', 't'])

    G.addEdge(0, 1, True, 16)
    G.addEdge(0, 2, True, 13)

    G.addEdge(1, 3, True, 12)

    G.addEdge(2, 1, True, 4)
    G.addEdge(2, 4, True, 14)

    G.addEdge(3, 2, True, 9)
    G.addEdge(3, 5, True, 20)

    G.addEdge(4, 3, True, 7)
    G.addEdge(4, 5, True, 4)

    print(G)
    print()
    print()
    #max_flow = Ford_Fulkerson(G, 0, 5)
    max_flow = Edmonds_Karp(G, 0, 5)
    print("Max Flow:", max_flow)