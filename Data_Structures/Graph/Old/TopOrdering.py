from path import isAcyclic

class queue:
    def __init__(self):
        self.store = []

    def enq(self, val):
        self.store += [val]

    def deq(self):
        if self.store == []:
            return False
        r = self.store[0]
        self.store = self.store[1:len(self.store)]
        return r

def topologicalOrdering(G):
    #Needs to be a Directed Acyclic Graph (DAG) 
    if not G.isDirected():
        return False
    if not isAcyclic(G):
        return False

    #List if visited nodes
    visited = []
    for i in range(0,len(G.adj)):
        visited += [False]

    #finding in Degree of nodes
    inDegree = []
    for i in range(0,len(G.adj)):
        inDegree += [G.inDegree(i)]
    
    #adding nodes to queue with inDegree == 0
    q = queue()
    for i in range(0,len(inDegree)):
        if inDegree[i] == 0:
            q.enq(i)
    
    out = []
    while q.store != []:
        w = q.deq()
        #print w
        visited[w] = True
        out += [w]
        #subtracting 1 from inDegree of all nodes w points to
        for p in G.adj[w]:
            inDegree[p[0]] -= 1
        #adding nodes that now have an inDegree of 0
        #AND that has not already been visited
        for i in range(0,len(inDegree)):
            if inDegree[i] == 0 and not visited[i]:
                q.enq(i)
    return out
