class graph:
    def __init__(self):
        self.adj = []
    
    def addVertex(self,n=1):
        if n <= 0:
            return -1
        
        for i in range(0,n):
            self.adj += [[]]
        return len(self.adj)

    def addEdge(self,from_idx,to_idx,directed,weight):
        #error checks
        if from_idx < 0 or from_idx >= len(self.adj):
            return False
        if to_idx < 0 or to_idx >= len(self.adj):
            return False
        if directed != True and directed != False:
            return False
        if weight == 0:
            return False
        
        #should I check if [to_idx,weight] in  self.adj[from_idx]?

        self.adj[from_idx] += [[to_idx,weight]]
        if not directed:
            self.adj[to_idx] += [[from_idx,weight]]
        return True
    
    def removeEdge(self,v_x,v_y):
        if v_x < 0 or v_x >= len(self.adj):
            return False
        if v_y < 0 or v_y >= len(self.adj):
            return False
        found = -1
        for i in range(0,len(self.adj[v_x])):
            if self.adj[v_x][i][0] == v_y:
                found = i
        print found
        if found != -1:
            del self.adj[v_x][found]
            return True
        return False
    
    def printEdges(self):
        for v in self.adj:
            print v
        return self.adj
    
    def makeAdjMatrix(self):
        out = []
        for i in range(0,len(self.adj)):
            temp = [0] * len(self.adj)
            for j in range(0,len(self.adj[i])):
                temp[self.adj[i][j][0]] = self.adj[i][j][1]
            out += [temp]
        return out
    
    def isDirected(self):
        for i in range(0,len(self.adj)):
            for j in range(0,len(self.adj[i])):
                if [i,self.adj[i][j][1]] not in self.adj[self.adj[i][j][0]]:
                    return True
        return False
    
    def Degree(self,v):
        if v < 0 or v >= len(self.adj):
            return None
        if self.isDirected():
            return None
        return len(self.adj[v])

    def outDegree(self,v):
        if v < 0 or v >= len(self.adj):
            return None
        return len(self.adj[v])

    def inDegree(self,v):
        if v < 0 or v >= len(self.adj):
            return None
        count = 0
        for i in range(0,len(self.adj)):
            for j in range(0,len(self.adj[i])):
                if self.adj[i][j][0] == v:
                    count += 1
        return count
