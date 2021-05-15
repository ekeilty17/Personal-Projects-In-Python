# General Search Tree

This is an abstract implementation of a Depth-First search tree, which allows the search algorithm to be quickly and easily applied to specific problems with just a few method definitions.

## What is a Depth-First Search?

There are 2 useful ways to search a general tree: _Breadth-First_ and _Depth-First_.

**Breadth-First:** For some node, process self, process all siblings, then process children. </br>
**Depth-First:** For some node, process self, process children, then process siblings.

If we have the following tree:

```
								 A
							/	 |    	  \
						   B		 C		D
						   |		/ \
						   E	       F   G		
```

Then for each type of search they are processed in the following order: </br>
**Breadth-First:** ABCDEFG </br>
**Depth-First:** ABECFGD

### Main Advantage of a Depth-First Search

There is nothing special about the order each type of search processes the nodes of the tree, it's all about the memory. If you do a complete Breadth-First Search, then you need to store every node of the tree in the memory. But when you do a Depth-First Search you only need to store one branch at a time.

A Breadth-First search will generally take up c<sup>h</sup> units of memory, where c is the average number of children of each node and h is the height of the tree. Whereas a Depth-First search will at most need to store h units of memory. This makes processing all the nodes much faster and allows for deeper searches.

## How to Use

The logic of the Depth-First search and the abstract class definition is in `general_search_tree.py`. This is what you import in order to preform the Depth-First search. Import using `from general_search_tree import *`.

`use.py` is a template of how to implement the `general_search_tree`. First let's look at the class definition.

```python
class specific_search_tree(general_search_tree):

    def __init__(self, val):
        general_search_tree.__init__(self, val)

    def isSolution(self):
        pass

    def prune(self):
        pass

    def getEdges(self):
        pass

    def heuristic(self, L):
        pass

    def copy_node(self):
        pass

    def evolve(self, E):
        pass

    def Display(self):
        pass
```

You can name the `specific_search_tree` class whatever you want, the implication of the name is that this is a specific implementation of the `general_search_tree` class. I think of the `general_search_tree` class as a abstract class and it's intended use is to define specific instances of it to solve a specific, well-defined problem.

For each method defined below the `__init__()` function, I have included information about the parameters, return type, and whether or not an implementation is required. I have also included how I have implemented these functions when I have used this class (with place holder names for the functions). This can all be found inside `use.py`.

Once you have correctly defined an implementation for each method you get 2 methods for free: `search()` and `back_track()`. The former does the Depth-First search and the latter gets you the path from the root node to the end of the search. In order to use the `search()` method, just define some `initial_state` variable and execute the following.


`leaf = specific_search_tree(intial_state).search()`

`leaf.val` will be the final state of the search. To get the path the computer took in order to get from the initial staet to the final state, execute the following:

```python
if leaf == False:
    print []
else:
    L = leaf.back_track()
    for x in L:
        x.Display()
```

## Why I Made This

In my `Games` directory I began making AIs that could solve the game, in particular `Sudoku` and `Knight's Tour`. I noticed that the searching algorithms for both of these games were very similar and I wanted to create an abstract implementation of the search that I could easily use in other cases. I found it a very fun and fulfilling excercise to figure out how to extract the essense of a Depth-First search algorithm and implement it in a clean, simple, and easy to use way.

I always find that examples online of class inheritance are kind of dumb. It's always like they make a pet class and then a dog class is an instance of a pet. It's a nice way to show the syntax, but not a good way to show how inheritance is actually useful. I think this is an amazing example of the power that class inheritance can have.
