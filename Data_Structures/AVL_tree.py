from binary_search_tree import BinarySearchTree

class AVLTree(BinarySearchTree):
    """ 
    Implements an AVL Tree (named after Adelson-Velsky and Landis), which guarentees O(nlogn) search time.
    The rules are the following:
        1. The sub-trees of every node differ in height by at most one
        2. Every sub-tree is an AVL tree
    """

    def __init__(self, val=None):
        super(AVLTree, self).__init__(val=val)
        #self.height = self.assign_heights()
        self.height = 0

    """ Magic Methods """

    """ Writing """
    def create_node(self, val=None):
        return AVLTree(self.val if val == None else val)

    def assign_heights(self):
        L = -1
        R = -1
        if self.get_left() != None:
            L = self.get_left().assign_heights()
        if self.get_right() != None:
            R = self.get_right().assign_heights()
        
        self.height = max(L, R) + 1
        return self.height
        
    def balance_factor(self):
        bf = 0
        if self.get_left() != None:
            bf -= self.get_left().height+1
        if self.get_right() != None:
            bf += self.get_right().height+1
        return bf

    def balance(self):
        self.assign_heights()
        bf = self.balance_factor()
        bf_L = 0
        bf_R = 0

        # balancing through rotations
        if bf < -1:             # root is left heavy 
            if bf_L > 0:        # left child is right heavy
                self.get_left().rotate_left()
            self.rotate_right()
        
        elif bf > 1:            # root is right heavy
            if bf_R < 0:        # right child is legt heavy
                self.get_right().rotate_right()
            self.rotate_left()
        return self
    
    def insert(self, arg):
        x = super(AVLTree, self).insert(arg=arg)
        curr = x
        while curr != None:
            curr.balance()
            curr = curr.parent
        return x

    def delete(self, *path):
        P = super(AVLTree, self).delete(*path)
        curr = P
        while curr != None:
            curr.balance()
            curr = curr.parent
        return P


    """ Reading """
    def node_info(self, less=False):
        if less: 
            children_list = [ child.val if child != None else None for child in self.children]
            return f"{self.parent.val if self.parent != None else None} <-- ({self.val}), {self.balance_factor()} --> {children_list}"
        else:
            children_list = [ (child.val, id(child)) if child != None else (None, id(child)) for child in self.children]
            return f"({self.parent.val if self.parent != None else None}, {id(self.parent)}) <-- ({self.val}, {id(self)}), {self.balance_factor()} --> {children_list}"

def avl_tree_sort(L):
    B = AVLTree(L[0])
    for val in L[1:]:
        B.add(val)
    return B.in_order()

if __name__ == "__main__":

    """ How to create an AVL Binary Tree """

    # Adding items one at a time
    root = AVLTree(0)
    root.insert(10)
    root.insert(20)
    root.insert(30)
    root.insert(40)
    root.insert(50)
    root.insert(60)
    root.insert(70)
    root.insert(80)

    # Adding items all at once
    #AVLTree()
    #root.add(range(0, 110, 10))
    # This also works
    #root += range(0, 110, 10)

    print(root)
    print(root.get_info(less=True))
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

    # Sorting a list using the AVL tree, 
    # which theoretically should be faster than the plain binary tree
    #print( avl_tree_sort([10, 40, -4, 2, 100, 0, -4]) )