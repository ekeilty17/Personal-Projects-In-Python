from binary_tree import BinaryTree
# TODO: make a custom compare function so that you can call add() to a tuple or a list (add a variable unpack=True to add_in_order)

class BinarySearchTree(BinaryTree):
    """ 
    Implements a binary search tree where the user no longer has control over the configuration of nodes.
    The rules are the following:
        1. The value of a given node is greater than the value of all nodes to its left
        2. The value of a given node is less than the value of all nodes to its right
    """
    
    def __init__(self, val):
        super(BinarySearchTree, self).__init__(val=val)

    """ Magic Methods """
    def __add__(self, arg):
        arg = arg.pre_order() if isinstance(arg, BinarySearchTree) else arg
        return self.copy().insert(arg)

    """ Writing to Tree """
    def create_node(self, val=None):
        return BinarySearchTree(self.val if val == None else val)

    def insert(self, arg=None):
        if arg == None:
            return self
        
        if type(arg) == list:
            for val in arg:
                self.insert(val)
            return self

        curr = self
        while curr != None:
            if arg < curr:
                if curr.get_left() == None:
                    curr.add_left(arg)
                    return curr.get_left()
                curr = curr.get_left()
            else:
                if curr.get_right() == None:
                    curr.add_right(arg)
                    return curr.get_right()
                curr = curr.get_right()

    def merge(self, B):
        if not isinstance(B, BinarySearchTree):
            raise TypeError("Argument needs to be of type BinarySearchTree")
        self.insert(B.pre_order())
        return self

    # Helper function for delete
    def transplant(self, u, v):
        """ replaces the subtree rooted at u with the subtree rooted at v 
            Note: does not put u back in v's place, v remains.
            For example: 
                            root        -->         root
                        u           v           v           v
        """
        if u.parent == None:
            # making v the root
            self.val = v.val
            self.add_left( v.get_left() )
            self.add_right( v.get_right() )
        elif u is u.parent.get_left():
            u.parent.add_left(v.copy() if v != None else None)
        else:
            u.parent.add_right(v.copy() if v != None else None)
        
        if v != None:
            v.parent = u.parent

    # This is from CLRS, I can't be bothered to comment each line
    # essentially what it's doing is replacing the deleted node with its right subtree
    # and then adding the left subtree to the left child of the left-most node in the right subtree.
    # Thus maintaining the BST property
    def delete(self, *path):
        if path == ():
            deleted_node = self.copy()
            self.children = []
            self.val = None
            return deleted_node
        
        # D = deleted node
        # P = parent of deleted node
        # S = sucessor of deleted node
        D = self.get_node(*path)
        P = D.parent                # to return
        if D.get_left() == None:
            self.transplant(D, D.get_right())
        elif D.get_right() == None:
            self.transplant(D, D.get_left())
        else:
            S = D.successor()
            if not (S.parent is D):
                self.transplant(S, S.get_right())
                S.add_right( D.get_right() )
                S.get_right().parent = S
            self.transplant(D, S)
            S.add_left( D.get_left() )
            S.get_left().parent = S
        
        # This is the only sensible thing to return 
        # since the node no longer exists and its children get moved around
        return P

    """ Read from Tree """
    def search(self, val):
        curr = self
        while curr != None:
            if val == curr:
                return curr
            elif val < curr:
                curr = curr.get_left()
            else:
                curr = curr.get_right()
        return False

    def min(self):
        curr = self
        while curr.get_left() != None:
            curr = curr.get_left()
        return curr
    def max(self):
        curr = self
        while curr.get_right() != None:
            curr = curr.get_right()
        return curr
    
    def predecessor(self):
        return self.get_left().max()
    
    def successor(self):
        return self.get_right().min()

def binary_tree_sort(L):
    B = BinarySearchTree(L[0])
    B.insert(L[1:])
    return B.in_order()

if __name__ == "__main__":
    
    """ How to create a Generally Binary Tree """

    # Using class instances
    """
    root = BinarySearchTree(10)
    root.get_right() = BinarySearchTree(0)
    root.get_left() = BinarySearchTree(20)
    root.get_left().get_left() = BinarySearchTree(30)
    root.get_left().get_left().get_left() = BinarySearchTree(-40)
    """
    
    # Using class methods
    """
    root = BinarySearchTree(10)
    root.add_get_right()(0)
    root.add_get_left()(20)
    root.get_node(-1).add_get_left()(30)
    root.get_node(-1, -1).add_get_left()(-40)
    """


    """ How to create a Binary Search Tree """

    # Adding items one at a time
    root = BinarySearchTree(10)
    root.insert(0)
    root.insert(20)
    root.insert(30)
    root.insert(40)
    root.insert(-10)
    root.insert(5)

    # Adding items all at once
    """
    root = BinarySearchTree()
    root.insert([10, 0, 20, 30, 40])
    # This also works
    #root += [10, 0, 20, 30, 40]
    """

    # One line
    #root = BinarySearchTree([10, 0, 5, -10, 20, 30, 40])
    
    print(root)
    print()
    print("Depth-First Traversal:", root.depth_first())
    print("Breadth-First Traversal:", root.breadth_first())
    print("Level Order Traversal:", root.level_order())
    print("Pre-Order Traversal:", root.pre_order())
    print("In-Order Traversal:", root.in_order())
    print("Post-Order Traversal:", root.post_order())
    print()
    print("Min Node:", root.min())
    print("Max Node:", root.max())

    root += [23, 45, 31]
    print(root)
    print(root.in_order())

    print("\nDeleting Node 30:")
    root.delete(1, 1)
    print(root)
    print(root.in_order())
    

    # Sorting a list using the binary tree
    L = [10, 40, -4, 2, 100, 0, -4]
    print("\nSorting", L, "using Binary Search Tree:", binary_tree_sort(L))