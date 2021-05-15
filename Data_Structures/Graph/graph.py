from queue import Queue
from stack import Stack

class Graph(object):

    alpha = [   'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 
                'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                'U', 'V', 'W', 'X', 'Y', 'Z'    ]

    def __init__(self, multigraph=False):
        self.Adj = []
        # self.Adj will have the form [ [(index, name, weight), (index, name, weight), ...], 
        #                               [(index, name, weight), (index, name, weight), ...], ... ]
        self.Names = []
        self.multigraph = multigraph

    def __getitem__(self, v):
        return self.Adj[v]
    
    def __len__(self):
        return len(self.Adj)

    def _number_to_base(self, n, b):
        if n == 0:
            return [0]
        digits = []
        while n:
            digits.append(int(n % b))
            n //= b
        return digits[::-1]

    def addVertex(self, names=None, N=1):
        
        # type checking
        if type(N) != int:
            raise TypeError("Variable 'N' must be an integer")
        if N <= 0:
            raise ValueError("Variable 'N' must be greater than zero")
        
        # If user does not specify name, generate names using alphabetical numbers:
        #   A, B, ..., Z, AA, AB, ..., AZ, ...
        if names == None:
            names = []
            for i in range(N):
                digits = self._number_to_base(len(self.Names)+i, 26)
                names.append( "".join([ self.alpha[d-1] if i != len(digits)-1 else self.alpha[d] for i, d in enumerate(digits) ]) )
        # More error checking
        else:
            if type(names) != list:
                names = list(names)
            
            if len(names) != N:
                raise ValueError("The length of the variable 'names' must be the same as the value of the variable 'N'")
            
            for n in names:
                if type(n) != str:
                    raise TypeError("The elements of the variable 'names' must be strings")
        
        # actually adding vertices
        for v in range(N):
            self.Adj += [[]]
        
        self.Names += names

        return len(self.Adj)

    def addEdge(self, from_idx, to_idx, directed=False, weight=1):
        # error checks
        if from_idx < 0 or from_idx >= len(self.Adj):
            raise TypeError("Starting node does not exit in the graph.")
        if to_idx < 0 or to_idx >= len(self.Adj):
            raise TypeError("Ending node does not exist in the graph.")
        if directed != True and directed != False:
            raise TypeError("variable 'directed' must be a boolean.")
        if weight == 0:
            # A weight of zero implies no connection
            return None
        
        if self.multigraph or (to_idx, weight) not in self.Adj[from_idx]:
            self.Adj[from_idx] += [(to_idx, weight)]
        
        if not directed:
            if self.multigraph or (from_idx, weight) not in self.Adj[to_idx]:
                self.Adj[to_idx] += [(from_idx, weight)]

    def __str__(self):
        out = ""
        for v in range(len(self.Adj)):
            out += f"Node {self.Names[v]}:{'':10s}"
            for i, (node, weight) in enumerate(self.Adj[v]):
                out += f"{self.Names[node]}:{weight}"
                if i != len(self.Adj[v])-1:
                    out += ', '
            if v != len(self.Adj)-1:
                out += '\n'
        return out

    def getWeight(self, from_idx, to_idx):
        neighbor_idx = None
        try:
            neighbor_idx = [node for node, _ in self.Adj[from_idx]].index(to_idx)
            return self.Adj[from_idx][neighbor_idx][1]
        except:
            return 0
    
    def V(self):
        return list(range(len(self.Adj)))
    
    def E(self):
        out = []
        for v in range(len(self.Adj)):
            for u, w in self.Adj[v]:
                out += [(v, u, w)]
        return out

    def index(self, name):
        out = []
        for i, n in enumerate(self.Names):
            if name == n:
                out += [i]
        return out if len(out) > 1 else out[0]

    def getNeighbors(self, v):
        return [node for node, _ in self.Adj[v]]
    
    # From now on I will use A and B for the starting and ending node respectively
    # It is just shorter than the more descriptive from_idx and to_idx notation
    def removeEdge(self, A, B):
        self.removeSingleEdge(A, B)
        if not self.isDirected():
            self.removeSingleEdge(B, A)
    
    def removeSingleEdge(self, A, B):
        # Error Checking
        if A < 0 or A >= len(self.Adj):
            raise TypeError("Starting node does not exit in the graph.")
        if B < 0 or B >= len(self.Adj):
            raise TypeError("Ending node does not exist in the graph.")
        
        # This will remove all duplicate edges
        self.Adj[A] = list(filter(lambda x: x[0] != B, self.Adj[A]))

    def AdjMatrix(self):
        out = []
        for i in range(len(self.Adj)):
            temp = [0] * len(self.Adj)
            for node, weight in self.Adj[i]:
                temp[node] = weight
            out += [temp]
        return out

    def printAdjMatrix(self):
        M = self.AdjMatrix()
        print(f"{'':5s} {'  '.join(self.Names)}\n")
        for i, r in enumerate(M):
            print(f"{self.Names[i]:5s}{r}")
    

    """ Some functions to tell you infromation about the graph """
    
    def edge_exists(self, u, v):
        pass
    
    def vertex_exists(self, *args):
        for v in args:
            if v < 0 or v >= len(self):
                return False
        return True
    
    def isDirected(self):
        for i in range(len(self)):
            for node, _ in self[i]:
                if i not in self.getNeighbors(node):
                    return True
        return False

    def Degree(self, v):
        #error
        if not self.vertex_exists(v):
            raise TypeError("That node does not exist in the graph.")
        if self.isDirected():
            raise TypeError("The graph is directed, trying calling the methods outDegree() or inDegree().")
        return len(self.Adj[v])

    def outDegree(self, v):
        if v < 0 or v >= len(self):
            raise TypeError("That node does not exist in the graph.")
        return len(self.Adj[v])

    def inDegree(self, v):
        if v < 0 or v >= len(self):
            raise TypeError("That node does not exist in the graph.")
        count = 0
        for i in range(len(self)):
            for node, _ in self[i]:
                if node == v:
                    count += 1
        return count

    def isConnected(self, A, B):
        #error
        if not self.vertex_exists(A, B):
            return False

        out = (False, False)
        traversal = self.traverse(A, True)
        if B in traversal[0]:
            out[0] = True
        traversal = self.traverse(B, True)
        if A in traversal[0]:
            out[1] = True
        return out
    
    def isCyclic(self):
        for v in range(len(self)):
            if self.AllCycles(v) == []:
                return False
        return True

    def isAcyclic(self):
        return not self.isCyclic()
    
    """ Some functions that do useful things to the graph """
    
    def AllPaths(self, start, end):
        #error
        if not self.vertex_exists(start, end):
            return []
        
        # Note: There is a cleaner way to write this, but for AllCycles() to work
        #       I needed to add some extra conditions

        paths = []
        S = Stack()
        S.push( (start, []) )
        
        while not S.isEmpty(): 
            
            node, path = S.pop()
            if node == end and path != []:
                paths += [path + [end]]
            else:
                for next_node, _ in self[node]:
                    if start == end:
                        if next_node not in path[1:]:
                            S.push( (next_node, path[:] + [node]) )
                    else:
                        if next_node not in path:
                            S.push( (next_node, path[:] + [node]) )
        return paths
    
    def AllCycles(self, v):
        if not self.vertex_exists(v):
            return []
        return self.AllPaths(v, v)

    def traverse(self, start=None, searchType='depth'):
        if start != None:
            if start < 0 or start > len(self):
                raise TypeError("Node does not exist in the graph")
        if searchType != 'depth' and searchType != 'breadth':
            return []
        
        # initializing the queue/stack
        C = Stack() if searchType == 'depth' else Queue()

        # helper lists to keep track of where I've been
        visited = [False] * len(self)
        processed = [False] * len(self)

        # dealing with the weird starting case
        n = len(self) if start == None else 1

        paths = [[i] for i in range(len(self))]
        connected_subgraphs = []
        for i in range(n):
            edges = []
            subgraph = []
            # this is also to deal with the weird start case
            if start == None:
                if visited[i] == False:
                    C.push(i)
                    visited[i] = True
            else:
                if visited[start] == False:
                    C.push(start)
                    visited[start] = True
            # actual algorithm
            while not C.isEmpty():
                u = C.pop()
                if processed[u] == False:
                    subgraph += [u]
                    processed[u] = True
                for v, _ in self.Adj[u]:
                    if visited[v] == False:
                        C.push(v)
                        visited[v] = True
                        paths[v] = paths[u] + [v]
            if subgraph != []:
                connected_subgraphs += [subgraph]
        
        #return connected_subgraphs
        return paths

    def BFS(self, start=None):
        return self.traverse(start=start, searchType='breadth')

    def DFS(self, start=None):
        return self.traverse(start=start, searchType='depth')



if __name__ == "__main__":
    G = Graph()
    
    G.addVertex(N=5)
    G.addEdge(0,1,True,1)
    G.addEdge(0,2,True,1)
    G.addEdge(0,3,True,1)
    G.addEdge(0,4,True,1)
    G.addEdge(1,3,True,1)
    G.addEdge(2,1,True,1)
    G.addEdge(2,4,True,2)
    G.addEdge(3,4,True,1)
    G.addEdge(3,2,True,1)
    G.addEdge(3,2,True,1)
    print("Represenation of the Graph")
    print(G)
    print()
    print("Vertices:", G.V())
    print("Edges:", G.E())
    print(f"Node {G.Names[0]}: {G[0]}")
    print()
    print("Breadth-First Search:", G.BFS())
    print("Depth-First Search:", G.DFS())
    print()
    print(f"All paths from vertex {2} to vertex {3}:", G.AllPaths(2, 3))
    print(f"All cycles from vertex {1}:", G.AllCycles(1))
    print()
    print(G)
    print()
    G.printAdjMatrix()
    
    """
    print("Remove Edge")
    G.removeEdge(1,3)
    G.removeEdge(2,4)
    G.removeEdge(0,0)
    """

    """
    TP = G.TopologicalOrdering()
    print(TP)
    """

