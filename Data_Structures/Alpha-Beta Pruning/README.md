# Alpha-Beta Pruning Tree

This is an abstract implementation of an alpha-beta pruning search tree. which allows the search algorithm to be quickly and easily applied to specific problems with just a few method definitions.

## How to Use

The logic of the alpha-beta search algorithm is in `general_alphabeta_tree.py`. This is what you import in order to preform the alpha-beta pruning search. Import using `from general_alphabeta_tree import *`.

`use.py` is a template of how to implement the `general_alpha_beta_tree`. First let's look at the class defintion.

```python
class specific_alpha_beta_tree(general_alpha_beta_tree):

    def __init__(self, x, isMaximizingPlayer=True):
        general_alpha_beta_tree.__init__(self, val, isMaximizingPlayer)

    def evaluation(self):
        pass

    def isLeaf(self):
        pass
    
    def getEdges(self):
        pass

    def copy_node(self):
        pass

    def evolve(self, E):
        pass
```

You can name `specific_alphabeta_tree` whatever you want, the implication of the name is that this is a specific implementation of the `general_alpha_beta_tree` class. I think of the `general_alphabeta_tree` class as a abstract class and it's intended use is to define specific instances of it to solve a specific, well-defined problem.

For each method defined below the `__init__()` function, I have included information about the parameters, return type, and whether or not an implementation is required. I have also included how I have implemented these functions when I have used this class (with place holder names for the functions). This can all be found inside `use.py`.

Once you have correctly defined an implementation for each method you get 2 methods for free: `search()` and `getBestChild()`. The former returns the evaluation of the node based on the alpha-beta search and the latter gets you the child with the best evaulation from the `.search()` function. In order to use the `search()` and `getBestChild()` method, just define some `initial_state` variable, whether this node is a maximizer, and the depth in which you want to search and execute the following.

```python
bestChild = specific_alphabeta_tree( curr_state, isMaximizingPlayer ).getBestChild(depth)
```
Note: if you want the tree to keep searching until it hits a leaf node, then set depth equal to -1.
