from kary_tree import KaryTree

# TODO: add deletion
class BinaryTree(KaryTree):
    """ 
    A general binary tree, not a binary search tree. 
    The user has full control over what values go into each node 
    """

    def __init__(self, val):
        super(BinaryTree, self).__init__(k=2, val=val)

    """ Magic Methods """

    """ Writing """
    def create_node(self, val=None):
        return BinaryTree(self.val if val == None else val)
    
    def convert_index(self, i):
        if i == 'p' or i == None:
            return i
        
        if i == -1:
            return 0
        elif i == 0:
            return None
        elif i == 1:
            return 1
        else:
            raise IndexError(f"Index out of range, must be either -1 (left child), 0 (self), or 1 (right child)")
    
    def add_left(self, B):
        if B == None:
            self.children[0] = None
            return self
        return self.insert_at_index(-1, B)

    def add_right(self, B):
        if B == None:
            self.children[1] = None
            return self
        return self.insert_at_index(1, B)

    def delete_left(self):
        return self.delete(-1)
    
    def delete_right(self):
        return self.delete(1)
    

    """ Reading """
    def get_left(self):
        return self.children[0]
    
    def get_right(self):
        return self.children[1]

    def in_order(self):
        if self.val == None:
            return []
        def in_order_rec(node, L):
            if node.get_left() != None:
                in_order_rec(node.get_left(), L)
            L += [node.val]
            if node.get_right() != None:
                in_order_rec(node.get_right(), L)
            return L
        return in_order_rec(self, [])
    
    # pre_order and post_order inherited from Tree class
    

    # TODO: add arguments that let you maintain the reference
    """ Rotations """
    # There are less complicated rotation algorithms, but this way I can do it in-place rather than having to return the new root
    # which cleans up the syntax a little for the user
    def rotate_right(self, keep_root=True):
        if self.get_left() == None:
            return None
        
        if keep_root:
            # creating new right node
            new_right = self.create_node(val=self.val)
            if self.get_left().get_right() != None:
                new_right.add_left( self.get_left().get_right() )
                self.get_left().get_right().parent = new_right
            if self.get_right() != None:
                new_right.add_right( self.get_right() )
                self.get_right().parent = new_right
            new_right.parent = self

            # re-assigning root
            self.val = self.get_left().val
            self.add_left( self.get_left().get_left() )
            self.add_right( new_right )

            return self
        else:
            L = self.get_left()
            P = self.parent

            self.add_left( L.get_right() )
            if L.get_right() != None:
                L.get_right().parent = L

            L.add_right( self )
            self.parent = L

            L.parent = P
            if P != None:
                if self is P.get_left():
                    P.add_left( L )
                else:
                    P.add_right( L )
            
            return L

    def rotate_left(self, keep_root=True):
        if self.get_right() == None:
            return None
        
        if keep_root:
            # Creating new left node
            new_left = self.create_node(val=self.val)
            new_left.add_right( self.get_right().get_left() )
            new_left.add_left( self.get_left() )
            
            # setting parents
            if self.get_right().get_left() != None:
                self.get_right().get_left().parent = new_left
            if self.get_left() != None:
                self.get_left().parent = new_left
            new_left.parent = self

            # re-assigning root
            self.val = self.get_right().val
            self.add_right( self.get_right().get_right() )
            self.add_left( new_left )

            return self
        else:
            R = self.get_right()
            P = self.parent

            self.add_right( R.get_left() )
            if R.get_left() != None:
                R.get_left().parent = R

            R.add_left( self )
            self.parent = R

            R.parent = P
            if P != None:
                if self is P.get_left():
                    P.add_left( R )
                else:
                    P.add_right( R )
            
            return R

    def double_rotate_left(self):
        if self.get_right() == None:
            return None
        
        #self.add_right(  )
        self.get_right().rotate_right()
        return self.rotate_left()
    
    def double_rotate_right(self):
        if self.get_left == None:
            return None

        self.add_left( self.get_left().rotate_left() )
        return self.rotate_right()
    
    def is_left_child(self):
        if self.parent == None:
            return False
        return self is self.parent.get_left()
    
    def is_right_child(self):
        if self.parent == None:
            return False
        return self is self.parent.get_right()

if __name__ == "__main__":
    
    """ How to create a Generally Binary Tree """

    # Using get_left() & get_right() add_left() & add_right() and class methods
    root = BinaryTree(4)
    root.add_left(2)
    root.get_left().add_left(1)
    root.get_left().add_right(3)
    root.get_left().get_left().add_left(0)
    root.add_right(6)
    root.get_right().add_left(5)
    root.get_right().add_right(7)
    
    """
    # using indexing (this was an example from one of my homework problems)
    root = BinaryTree('M')
    
    root[-1] = 'N'
    root[-1][1] ='D'
    root[-1][-1] = 'H'
    root[-1][-1][-1] = 'C'
    root[-1][-1][1] = 'R'
    root[-1][-1][1][-1] = 'S'
    root[-1][-1][1][-1][-1] = 'K'
    root[-1][-1][1][-1][-1][-1] = 'W'
    root[-1][-1][1][-1][-1][1] = 'T'
    root[-1][-1][1][1] = 'G'

    root[1] = 'X'
    root[1][-1] = 'I'
    root[1][-1][-1] = 'Y'
    root[1][-1][-1][-1] = 'A'
    root[1][-1][-1][1] = 'J'
    root[1][-1][-1][1][-1] = 'P'
    root[1][-1][-1][1][-1][-1] = 'O'
    root[1][-1][-1][1][-1][1] = 'E'
    root[1][-1][1] = 'Z'
    root[1][1] = 'V'
    root[1][1][-1] = 'B'
    root[1][1][1] = 'U'
    root[1][1][1][-1] = 'L'
    root[1][1][1][-1][-1] = 'Q'
    root[1][1][1][1] = 'F'
    """

    """
    # Using .get_node() method
    root = BinaryTree(40)
    root.add_right(20)
    root.add_left(10)
    root.get_node(-1).add_left(-10)
    root.get_node(-1, -1).add_left(-40)
    """

    print(root)
    print(root.get_info(less=True))
    print()
    print("Depth-First Traversal:", root.depth_first())
    print("Breadth-First Traversal:", root.breadth_first())
    print("Level-Order Traversal:", root.level_order())
    print("Pre-Order Traversal:", root.pre_order())
    print("In-Order Traversal", root.in_order())
    print("Post-Order Traversal:", root.post_order())
    print()
    print("Min Node:")
    print(root.min())
    print("Max Node:")
    print(root.max())

    """
    print()
    print("Children of Root:", [child.val if child != None else child for child in root.children])
    print()
    print(root.get_left().get_left())
    d = root.delete_right()
    print("Delete left child:")
    print(d)
    print("Children of Root:", [child.val if child != None else child for child in root.children])
    print("\nNew Tree:")
    print(root)
    """
    print()
    print(root)
    print(root.in_order())
    print()
    root = root.rotate_left(keep_root=False)
    print(root)
    print(root.in_order())