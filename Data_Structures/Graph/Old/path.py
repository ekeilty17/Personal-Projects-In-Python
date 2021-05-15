from traversal import *

#connectivity
def connectivity(G,v_x,v_y):
    out = [False, False]
    #error
    if v_x < 0 or v_x >= len(G.adj):
        return out
    if v_y < 0 or v_y >= len(G.adj):
        return out
    #code
    traversal = traverse(G,v_x, True)
    if v_y in traversal[0]:
        out[0] = True
    traversal = traverse(G,v_y, True)
    if v_x in traversal[0]:
        out[1] = True
    return out

def isStronglyConnected(G):
    for i in range(0,len(G.adj)):
        for j in range(0,len(G.adj)):
            if i != j:
                if not (connectivity(G,i,j) and connectivity(G,j,i)):
                    return False
    return True

def isWeaklyConnected(G):
    for i in range(0,len(G.adj)):
        for j in range(0,len(G.adj)):
            if i != j:
                if not (connectivity(G,i,j) or connectivity(G,j,i)):
                    return False
    return True

#Path
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

def backTrack(leaf,L):
    if leaf.parent == None:
        return L
    L = [leaf.val] + L
    return backTrack(leaf.parent,L)

def genTree(G,root,v_x,v_y,L):
    #L = the list of processed nodes to prevent cycles
    if root == None:
        return False
    for adj in G.adj[root.val]:
        if adj[0] == v_y:
            return backTrack(root,[])
        if adj[0] != v_x and adj[0] != root.val and adj[0] not in L:
            t = tree(adj[0])
            root.AddSuccessor(t)
            L += [adj[0]]
            out = genTree(G,t,v_x,v_y,L)
            if out != True and out != False:
                return out
    return True

def path(G,v_x,v_y):
    out = [[],[]]
    #error
    if v_x < 0 or v_x >= len(G.adj):
        return out
    if v_y < 0 or v_y >= len(G.adj):
        return out
    #code
    C = self.connectivity(v_x,v_y)
    if C[0] == True:
        t = tree(v_x)
        p = genTree(G,t,v_x,v_y,[])
        #t.Print_DepthFirst()
        out[0] = [v_x] + p + [v_y]
    if C[1] == True:
        t = tree(v_y)
        p = genTree(G,t,v_y,v_x,[])
        #t.Print_DepthFirst()
        out[1] = [v_y] + p + [v_x]
    return out

#Cycles
def cycle(G,v):
    #error
    if v < 0:
        return []
    if v >= len(G.adj):
        return []
    #technically inefficient, but whatever
    out = path(G,v,v)
    return out[0]

#check this function, too lazy to analyze it now
def isAcyclic(G):
    for v in G.adj:
        if cycle(G,G.adj[0]) != []:
            return False
    return True
