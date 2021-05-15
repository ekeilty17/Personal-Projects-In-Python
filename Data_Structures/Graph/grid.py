from graph import *

def index_2to1(I, D):
    i, j = I
    n, m = D
    return i + j*n

def index_1to2(i, D):
    n, m = D
    return (i/n, i%n)

class Grid(Graph):

    def __init__(self, n, m=None, diagonals=True, uniform=False):
        # n x m = rows x columns
        if m == None:
            m = n 
        
        self.n = n
        self.m = m

        self.grid = []
        for i in range(self.n):
            temp = []
            for j in range(self.m):
                temp += ['.']
            self.grid += [temp]
        
        # init graph
        Graph.__init__(self)
        
        # Add verteces
        self.addVertex(n*m)
        
        # Connecting grid lines
        for i in range(n):
            for j in range(m):
                
                neighbors = [            (i, j-1),
                             (i-1, j  ),           (i+1, j  ),
                                         (i, j+1)            ]
                """
                neighbors = [(i-1, j-1), (i, j-1), (i+1, j-1),
                             (i-1, j  ),           (i+1, j  ),
                             (i-1, j+1), (i, j+1), (i+1, j+1)]
                """
                neighbors = list(filter(lambda L: L[0] >= 0 and L[0] < self.n and L[1] >= 0 and L[1] < self.m, neighbors))
                neighbors = map(lambda L: L[0] + L[1]*self.n, neighbors)
                for N in neighbors:
                    self.addEdge(i+j*n, N, True, 1)
                
                if diagonals:
                    neighbors = [(i-1, j-1),            (i+1, j-1),
                                 
                                 (i-1, j+1),            (i+1, j+1)]
                    neighbors = list(filter(lambda L: L[0] >= 0 and L[0] < self.n and L[1] >= 0 and L[1] < self.m, neighbors))
                    neighbors = map(lambda L: L[0] + L[1]*self.n, neighbors)
                    for N in neighbors:
                        if uniform:
                            self.addEdge(i+j*n, N, True, 1)
                        else:
                            self.addEdge(i+j*n, N, True, 2**0.5)
    
    def __str__(self):
        out = ""
        for i in range(len(self.grid)-1, -1, -1):
            for j in range(len(self.grid[i])):
                if self.grid[i][j] == '.':
                    out += '\033[40m' + ' ' + self.grid[i][j] + ' ' + '\033[0m'
                elif self.grid[i][j] == '*':
                     out += '\033[43m' + ' ' + self.grid[i][j] + ' ' + '\033[0m'
                else:
                    out += '\033[41m' + ' ' + self.grid[i][j] + ' ' + '\033[0m'
            out += '\n'
        return out[:-1]        
    
    # This method just causes other problems for other methods defined in the general graph code
    # and like when would a user actually need this
    #def __getitem__(self, (i, j)):
    #    return self.adj[i + j*self.n]
    
    def AdjList(self):
        return super(Grid, self).__str__()

    def reset_display(self):
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                if self.grid[i][j] == '*':
                    self.grid[i][j] = '.'

    def display_path(self, path):
        self.reset_display()
        for p in path:
            i, j = p
            self.grid[i][j] = '*'

    def removeNode(self, *args):
        i, j = 0, 0
        if len(args) == 1:
            i, j = args[0]
        if len(args) == 2:
            i, j = args
        
        # Removing all edges
        curr = i + j*self.n
        for N in self.getNeighbors(curr):
            self.removeEdge(curr, N)
        
        # updating node list
        self.grid[j][i] = ' '

    def removeRect(self, P, a, b):
        xi, yi = P
        for i in range(xi, xi+a):
            for j in range(yi, yi+b):
                self.removeNode(i, j)
    
    def Dijkstra(self, (xi, yi), (xf, yf)):
        
        start = xi + yi*self.n
        end = xf + yf*self.n

        dist, path = super(Grid, self).Dijkstra(start, end)
        print path
        path = [ (p/self.n, p%self.n) for p in path ]
        return (dist, path)


if __name__ == "__main__":
    G = Grid(10)
    print G
    print
    print
    #G.removeNode(1, 4)
    G.removeRect((5, 1), 1, 5)
    G.removeRect((1, 5), 5, 1)
    print G
    print
    dist, path = G.Dijkstra((2, 2), (9, 9))
    G.display_path(path)
    print G
    print dist
    print
    #print G.traverse(start=0, searchType='breadth')
    print
    G.reset_display()
    print
    print G
