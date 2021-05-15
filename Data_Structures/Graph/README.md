# Graph

This is an implementation of a general graph, which allows for the implementation of path-finding algorithms such as Dijkstra's algorithm, uniform cost search, A-star, breadth/depth first traversals, etc.

## How to Use

Creating a graph is very simple. I attempted to make the syntax reflect how one would draw a graph by hand.

```python
G = Graph()
G.addVertex(5)              # 5 is the number of verteces being added to the graph
G.addEdge(0, 1, True, 1)    # creating a non-directed connection of weight 1 between node 0 and node 1 of the graph
G.addEdge(0, 2, False, 3)   # creating a directed connection of weight 3 between node 0 and node 2 of the graph
...
print G                     # by default the Graph is represented by an adjacency list
G.printAdjMatrix()          # the adjacency matrix can be generated
```

# Grid

A useful application of the general graph class is an n by m grid. This allows one to more easily visualize the graph and the path-finding algorithms.

## How to use

```python
# Creating Grid
G = Grid(10, 11, diagonals=True)
print
print G

# Removing section of the grid
G.removeRect((5, 1), 1, 5)
G.removeRect((1, 5), 5, 1)
print
print G

# Finding shortest path
dist, path = G.Dijkstra((2,4), (9, 9))
G.display_path(path)
print
print G
print dist
G.reset_display()
```
