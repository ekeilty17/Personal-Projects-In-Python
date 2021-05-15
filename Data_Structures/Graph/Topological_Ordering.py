from graph import Graph
from queue import Queue

# FIXME: This doesn't work

def TopologicalOrdering(G):
    # Needs to be a Directed Acyclic Graph (DAG)
    if not G.isDirected():
        return []
    if not G.isAcyclic():
        return []
    
    # List of visited nodes
    visited = [False] * len(G)
    # finding in Degree of nodes
    inDegree = [G.inDegree(v) for v in range(len(G))]
    # adding nodes to queue with inDegree == 0
    Q = Queue([v for v in range(len(G)) if inDegree[v] == 0])
    
    out = []
    while not Q.isEmpty():
        w = Q.pop()
        visited[w] = True
        out += [w]
        #subtracting 1 from inDegree of all nodes w points to
        for p in G.Adj[w]:
            inDegree[p[0]] -= 1
        #adding nodes that now have an inDegree of 0
        #AND that has not already been visited
        for v in range(len(inDegree)):
            if inDegree[v] == 0 and not visited[v]:
                Q.push(v)
    return out

if __name__ == "__main__":
    G = Graph()

    G.addVertex(N=9, names=["undershots", "pants", "belt", "socks", "shoes", "watch", "shirt", "tie", "jacket"])
    
    G.addEdge(0, 1, True)
    G.addEdge(0, 4, True)
    G.addEdge(1, 2, True)
    G.addEdge(1, 4, True)
    G.addEdge(2, 8, True)
    G.addEdge(3, 4, True)
    G.addEdge(6, 7, True)
    G.addEdge(7, 8, True)

    print(G)
    print()

    TO = TopologicalOrdering(G)
    print([G.Names[v] for v in TO])