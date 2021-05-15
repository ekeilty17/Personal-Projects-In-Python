#Helper
class queue:
    def __init__(self):
        self.store = []

    def push(self, val):
        self.store += [val]

    def pop(self):
        if self.store == []:
            return False
        r = self.store[0]
        self.store = self.store[1:len(self.store)]
        return r

class stack:
    def __init__(self):
        self.store = []
    
    def push(self,val):
        self.store += [val]

    def pop(self):
        if self.store == []:
            return False
        r = self.store[len(self.store)-1]
        self.store = self.store[0:len(self.store)-1]
        return r

class tree:
    def __init__(self,x):
        self.val = x
        self.children = []
        self.parent = None

    def AddSuccessor(self,T):
        self.children += [T]
        T.parent = self
        return True

    def Print_DepthFirst(self):
        def rec(x,indent):
            print indent + str(x.val)
            indent += "\t"
            for i in range(0,len(x.children)):
                rec(x.children[i],indent)
            return True
        return rec(self,"")

class graph:
    def __init__(self):
        self.adj = []
    
    def addVertex(self,n):
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
    
    def printEdges(self):
        for v in self.adj:
            print v
        return self.adj
    
    def removeEdge(self,v_x,v_y):
        if v_x < 0 or v_x >= len(self.adj):
            return False
        if v_y < 0 or v_y >= len(self.adj):
            return False
        found = -1
        for i in range(0,len(self.adj[v_x])):
            if self.adj[v_x][i][0] == v_y:
                found = i
        if found != -1:
            del self.adj[v_x][found]
            return True
        return False 
    
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

    def traverse(self,start,typeBreadth):
        if start > len(self.adj):
            return False
        #if start == None:
        #   traverses entire graphs
        #else:
        #   start is the index the traversal starts on
        #if typeBreadth == True:
        #   Breadth First Traversal (Queue)
        #if typeBreadth == False:
        #   Depth Firt Traversal (Stack)
        if start != None:
            if start < 0:
                return False
        if typeBreadth != True and typeBreadth != False:
            return False
        
        #making the queue/stack
        C = None
        if typeBreadth:
            C = queue()
        if not typeBreadth:
            C = stack()
        
        #helper lists to keep track of where I've been
        visited = []
        processed = []
        for i in range(0,len(self.adj)):
            visited += [False]
            processed += [False]
        
        #dealing with the weird starting case
        V = self.adj
        n = 0
        if start == None:
            n = len(self.adj)
        else:
            n = 1
        
        out = []
        for i in range(0,n):
            temp = []
            #this is also to deal with the weird start case
            if start == None:
                if visited[i] == False:
                    C.push(i)
                    visited[i] = True
            else:
                if visited[start] == False:
                    C.push(start)
                    visited[start] = True
            #actual algorithm
            #print "\tpushing into C:",start
            while C.store != []:
                #print "C.store =",C.store
                w = C.pop()
                #print "\tw:",w
                if processed[w] == False:
                    temp += [w]
                    processed[w] = True
                for x in V[w]:
                    if visited[x[0]] == False:
                        C.push(x[0])
                        visited[x[0]] = True
                        #print "\tpushing into C:",x[0]
            if temp != []:
                out += [temp]
        return out
    
    def connectivity(self,v_x,v_y):
        out = [False, False]
        #error
        if v_x < 0 or v_x >= len(self.adj):
            return out
        if v_y < 0 or v_y >= len(self.adj):
            return out
        #code
        traversal = self.traverse(v_x, True)
        if v_y in traversal[0]:
            out[0] = True
        traversal = self.traverse(v_y, True)
        if v_x in traversal[0]:
            out[1] = True
        return out
   
    def backTrack(self,leaf,L):
        if leaf.parent == None:
            return L
        L = [leaf.val] + L
        return self.backTrack(leaf.parent,L)

    def genTree(self,root,v_x,v_y,L):
        #L = the list of processed nodes to prevent cycles
        if root == None:
            return False
        for adj in self.adj[root.val]:
            if adj[0] == v_y:
                return self.backTrack(root,[])
            if adj[0] != v_x and adj[0] != root.val and adj[0] not in L:
                t = tree(adj[0])
                root.AddSuccessor(t)
                L += [adj[0]]
                out = self.genTree(t,v_x,v_y,L)
                if out != True and out != False:
                    return out
        return True


    def path(self,v_x,v_y):
        out = [[],[]]
        #error
        if v_x < 0 or v_x >= len(self.adj):
            return out
        if v_y < 0 or v_y >= len(self.adj):
            return out
        #code
        C = self.connectivity(v_x,v_y)
        if C[0] == True:
            t = tree(v_x)
            p = self.genTree(t,v_x,v_y,[])
            #t.Print_DepthFirst()
            out[0] = [v_x] + p + [v_y]
        if C[1] == True:
            t = tree(v_y)
            p = self.genTree(t,v_y,v_x,[])
            #t.Print_DepthFirst()
            out[1] = [v_y] + p + [v_x]
        return out
    
    def cycle(self,v):
        #error
        if v < 0:
            return []
        if v >= len(self.adj):
            return []
        #technically inefficient, but whatever
        out = self.path(v,v)
        return out[0]
    
    def isAcyclic(self):
        for E in self.adj:
            if self.cycle(self.adj[0]) != []:
                return False
        return True
    
    def topologicalOrdering(self):
        #Needs to be a Directed Acyclic Graph (DAG) 
        if not self.isDirected():
            return False
        if not self.isAcyclic():
            return False

        #List if visited nodes
        visited = []
        for i in range(0,len(self.adj)):
            visited += [False]
        
        #finding in Degree of nodes
        inDegree = []
        for i in range(0,len(self.adj)):
            inDegree += [self.inDegree(i)]
        
        #adding nodes to queue with inDegree == 0
        q = queue()
        for i in range(0,len(inDegree)):
            if inDegree[i] == 0:
                q.push(i)
        
        out = []
        while q.store != []:
            w = q.pop()
            #print w
            visited[w] = True
            out += [w]
            #subtracting 1 from inDegree of all nodes w points to
            for p in self.adj[w]:
                inDegree[p[0]] -= 1
            #adding nodes that now have an inDegree of 0
            #AND that has not already been visited
            for i in range(0,len(inDegree)):
                if inDegree[i] == 0 and not visited[i]:
                    q.push(i)
        return out
