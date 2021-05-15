from binary_search_tree import BinarySearchTree

class AVLTree(BinarySearchTree):
    """ Implements an AVL Tree (named after Adelson-Velsky and Landis), which guarentees O(nlogn) search time.
        The rules are the following:
            1. The sub-trees of every node differ in height by at most one
            2. Every sub-tree is an AVL tree
    """

    def __init__(self, val=None):
        self.val = val
        self.left = None
        self.right = None
        self.height = self.assign_heights()
    
    """ Operation Overloading """
    def __add__(self, arg):
        return self.copy().add(arg)

    """ Helper Functions """
    def get_info(self):
        def rec(T, indent, out):
            out += indent + str(T.val) + ", " + str(T.height) + ", " + str(T.balance_factor()) + "\n"
            if T.right != None:
                out += rec(T.right, indent + "\t", "")
            if T.left != None:
                out += rec(T.left, indent + "\t", "")
            return out
        return rec(self, "", "")[:-1]

    def assign_heights(self):
        L = -1
        R = -1
        if self.left != None:
            L = self.left.assign_heights()
        if self.right != None:
            R = self.right.assign_heights()
        
        self.height = max(L, R) + 1
        return self.height
        
    def balance_factor(self):
        bf = 0
        if self.left != None:
            bf -= self.left.height+1
        if self.right != None:
            bf += self.right.height+1
        
        return bf

    def balance(self):
        bf = self.balance_factor()
        bf_L = 0
        bf_R = 0

        # recursively going down the tree
        if self.left != None:
            self.left = self.left.balance()
            bf_L = self.left.balance_factor()
        if self.right != None:
            self.right = self.right.balance() 
            bf_R = self.right.balance_factor()
        
        # balancing through rotations
        if bf < -1:             # root is left heavy 
            if bf_L > 0:        # left child is right heavy
                self.left = self.left.rotate_left()
            return self.rotate_right()
        
        elif bf > 1:            # root is right heavy
            if bf_R < 0:        # right child is left heavy
                self.right = self.right.rotate_right()
            return self.rotate_left()
        return self
    
    """ User Functions """
    def add(self, arg):
        if self.val == None:
            if type(arg) == list:
                self.val = arg[0]
                for val in arg[1:]:
                    self._add_in_order(val)
                    self.assign_heights()
                    self = self.balance()
                    self.assign_heights()
                    print( self.get_info() )
            elif isinstance(arg, BinaryTree):
                self.val = arg.val
                for val in arg.post_order()[1:]:
                    self._add_in_order(val)
                    self.assign_heights()
                    self = self.balance()
            else:
                self.val = arg
        else:
            if type(arg) == list:
                for val in arg:
                    self._add_in_order(val)
                    self.assign_heights()
                    self = self.balance()
            elif isinstance(arg, BinaryTree):
                for val in arg.in_order():
                    self._add_in_order(val)
                    self.assign_heights()
                    self = self.balance()
            else:
                self._add_in_order(arg)
                self.assign_heights()
                self = self.balance()
        return self


def avl_tree_sort(L):
    B = AVLTree()
    return B.add(L).in_order()

if __name__ == "__main__":

    """ How to create an AVL Binary Tree """

    # Adding items one at a time
    """
    root = AVLTree(0)
    root = root.add(10)
    root = root.add(20)
    root = root.add(30)
    root = root.add(40)
    root = root.add(50)
    root = root.add(60)
    root = root.add(70)
    root = root.add(80)
    """

    # Adding items all at once
    root = AVLTree()
    root = root.add(range(0, 50, 10))
    # This also works
    #root += range(0, 110, 10)

    print root.get_info()
    print
    print root.depth_first()
    print root.breadth_first()
    print root.pre_order()
    print root.in_order()
    print root.post_order()
    print
    print root.max()
    print root.min()

    # Sorting a list using the AVL tree, 
    # which theoretically should be faster than the plain binary tree
    #print avl_tree_sort([10, 40, -4, 2, 100, 0, -4])