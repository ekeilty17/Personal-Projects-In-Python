from binary_search_tree import BinarySearchTree

class RedBlackTree(BinarySearchTree):
    """ 
    Implements a Red Black Tree, which gaurentees an O(nlogn) search time.
    The rules are the following:
        1. Each node is colored red or black (null or None is considered black)
        2. The root must be black
        3. A red node must always have a black parent and a black child (no such restriction on black nodes)
        4. Every branch path from the root node to a null pointer (or None) passes through the same number
           of black nodes (null or None is considered black)
    """

    def __init__(self, val=None, color='B'):
        super(RedBlackTree, self).__init__(val=val)
        self.color = color

    """ Magic Methods """
    def __repr__(self):
        def rec(T, indent="", out=""):
            color = '\033[91m' if T.color == 'R' else '\033[0m'
            out += indent + color + str(T.val) + '\033[0m' + "\n"
            for child in reversed(T.children):
                if child != None:
                    out += rec(child, indent + "\t", "")
            return out
        return rec(self)[:-1]
    

    """ Writing """
    def create_node(self, val=None, color=None):
        return RedBlackTree(val=self.val if val == None else val, color=self.color if color == None else color)

    # This is tested and does work (at least as far as I can tell)
    # TODO: make is so I don't need to use the syntax root = root.insert
    # and instead insert returns the node that was inserted
    def insert(self, arg):
        # BST insert and color the inserted node (z) red
        z = super(RedBlackTree, self).insert(arg)
        z.color = 'R'

        # an edge cases
        if z.parent == None:            # z is root
            z.color = 'B'
            return z
        if z.parent.parent == None:     # z is child of root
            z.color = 'R'
            return z.parent

        # Now we have 6 cases. Note because of the base cases above, z.parent.parent will always be defined
        while z.parent != None and z.parent.color == 'R':
            # z's parent is a left child
            if z.parent.is_left_child():
                # case 1: z's uncle is red
                uncle = z.parent.parent.get_right()
                if uncle != None and uncle.color == 'R':
                    z.parent.color = 'B'
                    uncle.color = 'B'
                    z.parent.parent.color = 'R'
                    z = z.parent.parent
                else:
                    # case 2: z's uncle is black and z is a right child
                    if z.is_right_child():
                        z = z.parent
                        z.rotate_left(keep_root=False)
                    # case 3: z's uncle is black and z is a left child
                    z.parent.color = 'B'
                    z.parent.parent.color = 'R'
                    z.parent.parent.rotate_right(keep_root=False)
            
            # exactly symmetric with the above
            else:
                # case 4
                uncle = z.parent.parent.get_left()
                if uncle != None and uncle.color == 'R':
                    z.parent.color = 'B'
                    uncle.color = 'B'
                    z.parent.parent.color = 'R'
                    z = z.parent.parent
                else:
                    # case 5
                    if z.is_left_child():
                        z = z.parent
                        z.rotate_right(keep_root=False)
                    # case 6
                    z.parent.color = 'B'
                    z.parent.parent.color = 'R'
                    z.parent.parent.rotate_left(keep_root=False)
            
        # color the root black
        root = z
        while root.parent != None:
            root = root.parent
        root.color = 'B'

        return root

    # helper for delete...not tested
    def fix_up(self, x):
        while x.parent != None and x.color == 'B':
            if x.is_left_child():
                w = x.parent.get_right()
                if w.color == 'R':
                    w.color = 'B'
                    x.parent.color = 'R'
                    x.parent.rotate_left(keep_root=False)
                    w = x.parent.get_right()
                if w.get_left().color == 'B' and w.get_right().color == 'B':
                    w.color = 'R'
                    x = x.parent
                else:
                    if w.get_right().color == 'B':
                        w.get_left().color = 'B'
                        w.color = 'R'
                        w.rotate_right(keep_root=False)
                        w = x.parent.get_right()
                    w.color = x.parent.color
                    x.parent.color = 'B'
                    w.get_right().color = 'B'
                    x.parent.rotate_left(keep_root=False)
            else:
                w = x.parent.get_left()
                if w.color == 'R':
                    w.color = 'B'
                    x.parent.color = 'R'
                    x.parent.rotate_right(keep_root=False)
                    w = x.parent.get_left()
                if w.get_left().color == 'B' and w.get_right().color == 'B':
                    w.color = 'R'
                    x = x.parent
                else:
                    if w.get_left().color == 'B':
                        w.get_right().color = 'B'
                        w.color = 'R'
                        w.rotate_left(keep_root=False)
                        w = x.parent.get_left()
                    w.color = x.parent.color
                    x.parent.color = 'B'
                    w.get_left().color = 'B'
                    x.parent.rotate_right(keep_root=False)
        x.color = 'B'
        return x
    
    # TODO: No f**kin idea if this works lol
    def delete(self, *path):
        if path == ():
            deleted_node = self.copy()
            self.children = []
            self.val = None
            return deleted_node

        D = self.get_node(*path)
        S = D
        S_original_color = S.color
        x = None
        if D.get_left() == None:
            x = D.get_right()
            self.transplant(D, D.get_right())
        elif D.get_right() == None:
            x = D.get_left()
            self.transplant(D, D.get_left())
        else:
            S = D.get_right().min()
            S_original_color = S.color
            x = S.get_right()
            if S.parent is D:
                x.parent = S
            else:
                self.transplant(S, S.get_right())
                S.add_right( D.get_right() )
                S.get_right().parent = S
            self.transplant(D, S)
            S.add_left( D.get_left() )
            S.get_left().parent = S
            S.color = D.color
        if S_original_color == 'B':
            self.fix_up(x)

    
    """ Reading """
    def node_info(self, less=False):
        if less: 
            children_list = [ child.val if child != None else None for child in self.children]
            return f"{self.parent.val if self.parent != None else None} <-- ({self.val}), {self.color} --> {children_list}"
        else:
            children_list = [ (child.val, id(child)) if child != None else (None, id(child)) for child in self.children]
            return f"({self.parent.val if self.parent != None else None}, {id(self.parent)}) <-- ({self.val}, {id(self)}), {self.color} --> {children_list}"

if __name__ == "__main__":
    root = RedBlackTree(80)
    root = root.insert(70)
    root = root.insert(60)
    root = root.insert(50)
    root = root.insert(40)
    root = root.insert(30)
    root = root.insert(20)
    root = root.insert(10)

    print(root)
    print(root.in_order())