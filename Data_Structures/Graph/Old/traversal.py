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

def traverse(G,start,typeBreadth):
    if start > len(G.adj):
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
    for i in range(0,len(G.adj)):
        visited += [False]
        processed += [False]

    #dealing with the weird starting case
    V = G.adj
    n = 0
    if start == None:
        n = len(G.adj)
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
