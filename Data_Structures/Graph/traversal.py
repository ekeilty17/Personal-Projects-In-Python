class queue:
    def __init__(self):
        self.store = []

    #had to rename the queue functions
    def push(self, val):
        self.store += [val]

    #so that it works generally
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

def traverse(G, start, breadth='depth'):
    if start > len(G):
        raise TypeError("Node does not exist in the graph")
    if start != None:
        if start < 0:
            return False
    if typeBreadth != True and typeBreadth != False:
        return False

    # initializing the queue/stack
    C = None
    if typeBreadth:
        C = queue()
    if not typeBreadth:
        C = stack()

    # helper lists to keep track of where I've been
    visited = []
    processed = []
    for i in range(0,len(G.adj)):
        visited += [False]
        processed += [False]

    # dealing with the weird starting case
    V = G.adj
    n = 0
    if start == None:
        n = len(G.adj)
    else:
        n = 1

    out = []
    for i in range(0,n):
        temp = []
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
        while C.store != []:
            w = C.pop()
            if processed[w] == False:
                temp += [w]
                processed[w] = True
            for x in V[w]:
                if visited[x[0]] == False:
                    C.push(x[0])
                    visited[x[0]] = True
        if temp != []:
            out += [temp]
    return out
