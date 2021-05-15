from path import isStronglyConnected

def MinimalSpanningTree(G,start):
    if not isStronglyConnected(G) or G.isDirected():
        return False
    #Prim's Algorithm
    return True
