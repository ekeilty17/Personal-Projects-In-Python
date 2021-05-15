from binary_search_tree import BinarySearchTree

class SplayTree(BinarySearchTree):
    """ 
    Splay Tree. Amortized O(lg n) for almost every algorithm
    """

    def __init__(self, val=None):
        super(SplayTree, self).__init__(val=val)

    def create_node(self, val=None):
        return SplayTree(self.val if val == None else val)

    def splay(self):
        while self.parent != None:      # while x not root
            p = self.parent
            # Zig
            if p.parent == None:     # p is root
                if self.is_left_child():
                    self.parent.rotate_left(keep_root=False)
                else:
                    p.rotate_right(keep_root=False)
            # Zig-Zig
            elif self.is_left_child() and p.is_left_child():
                p.parent.rotate_right(keep_root=False)
                p.rotate_right(keep_root=False)
            elif self.is_right_child() and p.is_right_child():
                p.parent.rotate_left(keep_root=False)
                p.rotate_left(keep_root=False)
            # Zig-Zag
            elif self.is_left_child() and p.is_right_child():
                p.rotate_right(keep_root=False)
                self.parent.rotate_left(keep_root=False)      # x has a new parent
            else:
                p.rotate_left(keep_root=False)
                self.parent.rotate_right(keep_root=False)     # x has a new parent
        return self

    def insert(self, arg):
        x = super(SplayTree, self).insert(arg=arg)
        return x.splay()
    
    def search(self, val):
        x = super(SplayTree, self).search(val)
        if x == False:
            return False
        return x.splay()
    
    def delete(self, *path):
        x = super(SplayTree, self).delete(*path)
        return x.splay()
    
    def split(self, x):
        x.splay()
        return x.get_left(), x.get_right()


if __name__ == "__main__":

    root = SplayTree(5)
    root[-1] = 3
    root[1] = 6
    root[-1][-1] = 2
    root[-1][1] = 4

    print(root)
    x = root[-1, -1]
    #x = root.get_node(-1, -1)
    print(root.in_order())
    root = x.splay()
    print(root)
    print(root.in_order())