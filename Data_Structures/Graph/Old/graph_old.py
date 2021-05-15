class Graph(object):
    def __init__(self):
        self.adj = []
        self.directed = False
        # self.adj will have the form [ [[node, weight], [node, weight], ...], 
        #                               [[node, weight], [node, weight], ...], ... ]
    
    def __getItem__(self, i):
        return self.adj[i]
    
    def __len__(self):
        return len(self.adj)

    def addVertex(self,n=1):
        if n <= 0:
            return -1

        for i in range(0,n):
            self.adj += [[]]
        return len(self.adj)

    def addEdge(self, from_idx, to_idx, directed=False, weight=1):
        # error checks
        if from_idx < 0 or from_idx >= len(self.adj):
            raise TypeError("Starting node does not exit in the graph.")
        if to_idx < 0 or to_idx >= len(self.adj):
            raise TypeError("Ending node does not exist in the graph.")
        if directed != True and directed != False:
            raise TypeError("variable 'directed' must be a boolean.")
        if weight == 0:
            # A weight of zero implies no connection
            return None

        # I could check if [to_idx,weight] in  self.adj[from_idx]
        # Allow this means this is technically a multigraph, but I will allow it
        # in order to maintain as much generality as possible
        
        self.adj[from_idx] += [[to_idx, weight]]
        if not directed:
            self.adj[to_idx] += [[from_idx, weight]]
        else:
            self.directed = True

    def __str__(self):
        out = ""
        for i in range(len(self.adj)):
            out += "Node " + str(i) + ":\t"
            if i < 10:
                out += '\t'
            for j in range(len(self.adj[i])):
                out += '{(' + str(self.getNode(i, j)) + '), ' + str(self.getWeight(i, j)) + '}'
                if j != len(self.adj[i])-1:
                    out += ', '
            out += '\n'
        return out

    def getNode(self, from_idx, neighbor_idx):
        return self.adj[from_idx][neighbor_idx][0]

    def getWeight(self, from_idx, neighbor_idx):
        return self.adj[from_idx][neighbor_idx][1]
    
    def getNeighbors(self, i):
        return [x[0] for x in self.adj[i]]
    
    # From now on I will use A and B for the starting and ending node respectively
    # It is just shorter than the more descriptive from_idx and to_idx notation
    def removeEdge(self, A, B):
        self.removeSingleEdge(A, B)
        if not self.directed:
            self.removeSingleEdge(B, A)
    
    def removeSingleEdge(self, A, B):
        # Error Checking
        if A < 0 or A >= len(self.adj):
            raise TypeError("Starting node does not exit in the graph.")
        if B < 0 or B >= len(self.adj):
            raise TypeError("Ending node does not exist in the graph.")
        
        found = -1
        for i in range(0,len(self.adj[A])):
            if self.getNode(A, i) == B:
                found = i
        
        if found == -1:
            raise TypeError("Connection not found.")
        
        del self.adj[A][found]

    def AdjMatrix(self):
        out = []
        for i in range(0,len(self.adj)):
            temp = [0] * len(self.adj)
            for j in range(0,len(self.adj[i])):
                temp[self.getNode(i, j)] = self.getWeight(i, j)
            out += [temp]
        return out

    def printAdjMatrix(self):
        M = self.AdjMatrix()
        for r in M:
            print r
    

    # Some functions to tell you infromation about the graph
    
    # This is how you could write it to figure it out computationally
    # but I just stored it as a variable
    """
    def isDirected(self):
        for i in range(0,len(self.adj)):
            for j in range(0,len(self.adj[i])):
                if i not in self.getNeightbors(self.getNode(i, j)):
                    return True
        return False
    """
    def isDirected(self):
        return self.directed

    def Degree(self, v):
        if v < 0 or v >= len(self.adj):
            raise TypeError("That node does not exist in the graph.")
        if self.isDirected():
            raise TypeError("The graph is directed, trying calling the mathods outDegree() or inDegree().")
        return len(self.adj[v])

    def outDegree(self, v):
        if v < 0 or v >= len(self.adj):
            raise TypeError("That node does not exist in the graph.")
        return len(self.adj[v])

    def inDegree(self, v):
        if v < 0 or v >= len(self.adj):
            raise TypeError("That node does not exist in the graph.")
        count = 0
        for i in range(0,len(self.adj)):
            for j in range(0,len(self.adj[i])):
                if self.getNode(i, j) == v:
                    count += 1
        return count

if __name__ == "__main__":
    G = Graph()
    G.addVertex(5)
    G.addEdge(0,1,True,1)
    G.addEdge(0,2,True,1)
    G.addEdge(0,3,True,1)
    G.addEdge(0,4,True,1)
    G.addEdge(1,3,True,1)
    G.addEdge(2,1,True,1)
    G.addEdge(2,4,True,1)
    G.addEdge(3,4,True,1)
    G.addEdge(3,2,True,1)
    print "Represenation of the Graph"
    print G
    print
    print "Remove Edge"
    G.removeEdge(1,3)
    print G
    print
    G.printAdjMatrix()
