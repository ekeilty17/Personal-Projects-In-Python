from graph import *
from traversal import *
from path import *
from TopOrdering import *
from Dijkstra import *

G = graph()
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
G.printEdges()
print
print G.adj
"""
print "Remove Edge"
G.removeEdge(3,2)
G.printEdges()
print
print "Adjacency Matrix"
AM = G.makeAdjMatrix()
for r in AM:
    print r
print
print "Breadth First Transversal"
print traverse(G,None,True)
print
print "Depth First Transversal"
print traverse(G,None,False)
print
print "Topological Ordering"
print topologicalOrdering(G)
"""
