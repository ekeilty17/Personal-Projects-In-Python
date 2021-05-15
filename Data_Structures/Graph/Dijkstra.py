from graph import Graph
from queue import Queue

def Dijkstra(G, s):

    # Initialize all distances as infinite (represented with -1)
    dist = [-1] * len(G)
    # Initialize all paths as undefined
    path = [[]] * len(G)
    # Create a vertex set initialized with all verteces
    Q = list(range(len(G)))
    # This is technically not necessary, but significantly speeds things up
    visited = [False] * len(G)

    # Initializing dist and path for starting node
    dist[s] = 0
    path[s] = [s]

    while len(Q) != 0:
        
        # Approximate count for interations
        #print len(Q)

        # Find vertex with min distance to previous node and remove it
        u = -1
        min_dist = -1
        for n in range(len(G)):
            if dist[n] == -1 or visited[n]:
                continue
            if u == -1 or dist[n] < min_dist:
                u = n
                min_dist = dist[n]
        
        # If no node was found, then all nodes must have been visited
        # and we should stop searching
        if u == -1:
            Q = []
            continue
        Q.remove(u)
        visited[u] = True
        
        # Getting neighbors of u still in Q
        Neighbors = G.getNeighbors(u)
        Neighbors = list(filter(lambda x: x in Q, Neighbors))
        # Ordering them by weight as a heuristic for efficiency
        Neighbors = list(sorted(Neighbors, key=lambda x: G.getWeight(u, x)))
        
        # Test all unvisited neighbors still in Q
        for v in Neighbors:
            if not visited[v]:
                # if current path shorter than previous path (remember -1 = inf)
                if ( dist[v] == -1 ) or ( dist[u] + G.getWeight(u, v) < dist[v]) :
                    dist[v] = dist[u] + G.getWeight(u, v)
                    path[v] = path[u] + [v]
        
        # possibly add this for efficiency
        # Q = [ node for node in Q if not visited[node] ]

    return dist, path

if __name__ == "__main__":
    G = Graph()
    G.addVertex(N=5, names=['s', 't', 'x', 'y', 'z'])
    
    G.addEdge(0, 1, True, 10)
    G.addEdge(0, 3, True, 5)

    G.addEdge(1, 2, True, 1)
    G.addEdge(1, 3, True, 2)

    G.addEdge(2, 4, True, 4)

    G.addEdge(3, 1, True, 3)
    G.addEdge(3, 2, True, 9)
    G.addEdge(3, 4, True, 2)

    G.addEdge(4, 0, True, 7)
    G.addEdge(4, 2, True, 6)
    
    dist, path = Dijkstra(G, 0)
    for d, p in zip(dist, path):
        print(f"distance: {d}, path: {' --> '.join([G.Names[v] for v in p])}")