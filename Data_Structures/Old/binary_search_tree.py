from binary_tree import BinaryTree
# TODO: make a custom compare function so that you can call add() to a tuple or a list (add a variable unpack=True to add_in_order)

class BinarySearchTree(BinaryTree):
    """ Implements a binary search tree where the user no longer has control over the configuration of nodes.
        The rules are the following:
            1. The value of a given node is greater than the value of all nodes to its left
            2. The value of a given node is less than the value of all nodes to its right
    """
    
    def __init__(self, val=None):
        self.val = None
        self.left = None
        self.right = None
        if type(val) == list:
            for x in val:
                self.add(x)
        elif isinstance(val, BinaryTree):
            self.add(val)
        else:
            self.val = val

    """ Operator Overloading """
    def __add__(self, arg):
        return self.copy().add_in_order(arg)

    """ Helper Functions """
    def _add_in_order(self, val):
        if val < self.val:
            # Base case
            if self.left == None:
                self.left = self.__class__(val)
                return None
            # recursion
            return self.left._add_in_order(val)
        else:
            # Base case
            if self.right == None:
                self.right = self.__class__(val)
                return None
            # recursion
            return self.right._add_in_order(val)

    """ Writing to Tree """
    def add(self, arg):
        if self.val == None:
            if type(arg) == list:
                self.val = arg[0]
                for val in arg[1:]:
                    self._add_in_order(val)
            elif isinstance(arg, BinaryTree):
                self.val = arg.val
                for val in arg.post_order()[1:]:
                    self._add_in_order(val)
            else:
                self.val = arg
        else:
            if type(arg) == list:
                for val in arg:
                    self._add_in_order(val)
            elif isinstance(arg, BinaryTree):
                for val in arg.in_order():
                    self._add_in_order(val)
            else:
                self._add_in_order(arg)
        return self

    """
    def delete(self, node):
        if node == None:
            return self
        vals = node.post_order()[1:]
        node = BinaryTree()
        node.add_in_order(vals)
        return self
    """

    """ Read from Tree """
    def min(self):
        curr = self
        while curr.left != None:
            curr = curr.left
        return curr
    def max(self):
        curr = self
        while curr.right != None:
            curr = curr.right
        return curr

def binary_tree_sort(L):
    return BinarySearchTree(L).in_order()

if __name__ == "__main__":
    
    """ How to create a Generally Binary Tree """

    # Using class instances
    """
    root = BinarySearchTree(10)
    root.right = BinarySearchTree(0)
    root.left = BinarySearchTree(20)
    root.left.left = BinarySearchTree(30)
    root.left.left.left = BinarySearchTree(-40)
    """
    
    # Using class methods
    """
    root = BinarySearchTree(10)
    root.add_right(0)
    root.add_left(20)
    root.get_node(-1).add_left(30)
    root.get_node(-1, -1).add_left(-40)
    """


    """ How to create a Binary Search Tree """

    # Adding items one at a time
    """
    root = BinarySearchTree()
    root.add(10)
    root.add(0)
    root.add(20)
    root.add(30)
    root.add(40)
    """

    # Adding items all at once
    """
    root = BinarySearchTree()
    root.add([10, 0, 20, 30, 40])
    # This also works
    #root += [10, 0, 20, 30, 40]
    """

    # One line
    root = BinarySearchTree([10, 0, 5, -10, 20, 30, 40])
    
    print root
    print
    print root.depth_first()
    print root.breadth_first()
    print root.level_order()
    print root.pre_order()
    print root.in_order()
    print root.post_order()
    print
    print root.min()
    print root.max()

    # Sorting a list using the binary tree
    print binary_tree_sort([10, 40, -4, 2, 100, 0, -4])