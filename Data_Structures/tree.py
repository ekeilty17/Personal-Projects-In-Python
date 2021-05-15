class Tree(object):
    
    """
    General Tree structure used as the basis for all further tree structures
    """

    def __init__(self, val):
        self.val = val
        self.parent = None
        self.children = []

    """ Magic Methods """
    def __repr__(self):
        def rec(T, indent="", out=""):
            out += indent + str(T.val) + "\n"
            for child in reversed(T.children):
                if child != None:
                    out += rec(child, indent + "\t", "")
            return out
        return rec(self)[:-1]

    # gives number of nodes in the tree
    def __len__(self):
        accum = 1
        for child in self.children:
            accum += len(child)
        return accum

    # logic
    def __lt__(self, other):
        return self.val.__lt__(other.val if isinstance(other, Tree) else other)
    def __gt__(self, other):
        return self.val.__gt__(other.val if isinstance(other, Tree) else other)
    def __le__(self, other):
        return self.val.__le__(other.val if isinstance(other, Tree) else other)
    def __ge__(self, other):
        return self.val.__ge__(other.val if isinstance(other, Tree) else other)
    def __eq__(self, other):
        return self.val.__eq__(other.val if isinstance(other, Tree) else other)
    def __ne__(self, other):
        return self.val.__ne__(other.val if isinstance(other, Tree) else other)
    
    # TODO: implement slice object
    def __getitem__(self, *path):
        # annoying stuff because of how python returns the syntax root[1, 1]
        p = None
        if type(*path) == tuple:
            p, *_ = path
        else:
            p = path
        return self.get_node(*p)

    # TODO: implement slice object
    def __setitem__(self, i, arg):
        return self.insert_at_index(i, arg, extend_children=True)

    def __add__(self, arg):
        return self.copy().insert(arg)

    # Maybe revisit this at some point and see what would be most useful
    def __iter__(self):
        return iter(self.children)

    """ Getter """
    def get_val(self):
        return self.val
    
    def get_children(self):
        return self.children
    
    def get_parent(self):
        return self.parent
    
    def get_siblings(self):
        if self.parent == None:
            return []
        
        siblings = list(self.parent.children)
        siblings.remove(self)
        return list(filter(lambda sibling: sibling != None, siblings))

    """ Writing """
    def create_node(self, val=None):
        return Tree(self.val if val == None else val)
    
    def copy(self):
        T = self.create_node()
        def rec(T1, T2):
            for child in T1:
                if child != None:
                    C = T2.insert(child.val)
                    rec(child, C)
        rec(self, T)
        return T
    
    def convert_index(self, i):
        if i == 'p' or i == None:
            return i
        
        # So we can use the root[-1] convention to get the last element
        if i < 0:
            i += len(self.children)
        
        return i

    def insert_at_index(self, i, arg, extend_children=False):
        
        i = self.convert_index(i)
        T = arg if isinstance(arg, self.__class__) else self.create_node(val=arg)
        
        if i == None:
            self.val = T.val
            return self
        
        if i == 'p':
            # haven't figured out what to do with this
            pass

        if extend_children:
            # If i is still less than 1, we insert in the front. For example:
            #   root[-10] = Tree(10) means the node of value 10 is at position 0 
            #   and everything else gets shifted over so the last value is at index 9 (10 elements total)
            if i < 0:
                self.children = [None] * abs(i) + self.children
                i = 0
            # If we input i = 10, but there are only 4 elements, we insert Nones so that this node is at position 10
            elif i >= len(self.children):
                self.children += [None] * (i - len(self.children) + 1)

        # same as self.insert(T) but just as a specific position
        self.children[i] = T
        T.parent = self
        return T
    
    def insert(self, arg=None, extend_children=True):
        if arg == None:
            return self
        
        if type(arg) == list:
            for val in arg:
                self.insert(val)
            return self

        if None in self.children:
            i = self.children.index(None)
            return self.insert_at_index(i, arg, extend_children=False)
        else:
            self.children += [None]
            return self.insert_at_index(-1, arg, extend_children=extend_children)

    # This delete function will delete the node and all its children as there is really no good way
    # to re-order the children. The deleted subtree is returned
    # If there are no arguments, it clears the data structure
    def delete(self, *path, make_None=False):
        if path == ():
            deleted_node = self.copy()
            self.children = []
            self.val = None
            return deleted_node
        
        # get parent of node to delete and reference to deleted node so we can return it
        deleted_subtree = self.get_node(*path)
        parent = deleted_subtree.parent if deleted_subtree != None else self.get_node(*(path[:-1]))

        # delete node from children list
        if make_None:
            parent.children[ self.convert_index(path[-1]) ] = None
        else:
            del parent.children[ self.convert_index(path[-1]) ]

        return deleted_subtree
    
    def remove_Nones(self):
        self.children = list(filter(lambda child: child != None, self.children))


    """ Reading """
    # 'p' = get parent
    # None = stay at current node
    # int = index of child in children list
    def get_node(self, *path):
        curr = self
        path = list(map(lambda i: self.convert_index(i), list(path)))
        for i in path:
            if i == 'p':
                curr = curr.parent
            elif i == None:
                continue
            else:
                curr = curr.children[i]
        return curr
    
    def node_info(self, less=False):
        if less: 
            children_list = [ child.val if child != None else None for child in self.children]
            return f"{self.parent.val if self.parent != None else None} <-- ({self.val}) --> {children_list}"
        else:
            children_list = [ (child.val, id(child)) if child != None else (None, id(child)) for child in self.children]
            return f"({self.parent.val if self.parent != None else None}, {id(self.parent)}) <-- ({self.val}, {id(self)}) --> {children_list}"

    def get_info(self, less=False):
        def rec(T, indent, out):
            out += indent + T.node_info(less=less) + "\n"
            for child in reversed(T.children):
                if child != None:
                    out += rec(child, indent + "\t", "")
            return out
        return rec(self, "", "")[:-1]

    # TODO: implement...look at the graph code
    def search(self, val, type="depth"):
        if type != "depth" and type != "breadth":
            raise ValueError("The variable 'type' can either be 'depth' or 'breadth'")
        
        C = [self]                          # either a stack or a queue depending on which type of search
        while len(C) != 0:
            node = C.pop()
            if val == node:
                return node
            
            for child in node:
                if child != None:
                    if type == "depth":
                        C.append(child)     # acts like a stack
                    else:
                        C.insert(0, child)  # acts like a queue
        return False

    def get_root(self):
        curr = self
        while curr.parent != None:
            curr = curr.parent
        return curr

    def back_path(self):
        L = []
        curr = self
        while curr != None:
            L.append(curr.val)
            curr = curr.parent
        return list(reversed(L))

    def depth_first(self):
        return self.pre_order()

    def breadth_first(self):
        return self.level_order(flat=True)

    def pre_order(self):
        if self.val == None:
            return []
        def pre_order_rec(node, L):
            L += [node.val]
            for child in node:
                if child != None:
                    L = pre_order_rec(child, L)
            return L
        return pre_order_rec(self, [])

    def post_order(self):
        if self.val == None:
            return []
        def post_order_rec(node, L):
            for child in node:
                if child != None:
                    L = post_order_rec(child, L)
            L += [node.val]
            return L
        return post_order_rec(self, [])

    def level_order(self, flat=False):
        out = []
        Q = [self]
        while len(Q) != 0:
            count = len(Q)
            temp = []
            while count > 0: 
                T = Q.pop()
                temp += [T.val]
                for child in T:
                    if child != None:
                        Q.insert(0, child)
                count -= 1
            out += [temp]
        if flat:
            return [x for L in out for x in L]
        return out
    
    def min(self):
        def min_rec(T, curr_min):
            for child in T.children:
                if child != None:
                    child_min = min_rec(child, curr_min)
                    curr_min = child_min if child_min.val < curr_min.val else child_min
            return T if T.val < curr_min.val else curr_min
        return min_rec(self, self)
    
    def max(self):
        def max_rec(T, curr_max):
            for child in T.children:
                if child != None:
                    child_max = max_rec(child, curr_max)
                    curr_max = child_max if child_max.val > curr_max.val else curr_max
            return T if T.val > curr_max.val else curr_max
        return max_rec(self, self)

if __name__ == "__main__":
    root = Tree(4)
    # inserts at the end of root.children list
    root.insert(9)
    root.insert(100)
    root.insert(1)
    root.insert(-30)
    root.get_node(1).insert(10)
    root.get_node(3).insert(-1)

    g = Tree(500)
    g.insert(501)
    g.insert(502)
    # since there aren't 10 children, it add Nones so g goes to the 0th index and len(root.children) == 10
    root[-10] = g

    root.insert(19)

    print(root)
    print(root.get_info())
    print()
    print("Siblings:", [sibling.val for sibling in root[0].get_siblings()])
    print("Depth-First Traversal:", root.depth_first())
    print("Breadth-First Traversal:", root.breadth_first())
    print("Level-Order Traversal:", root.level_order())
    print()
    print("Min Node:")
    print(root.min())
    print("Max Node:")
    print(root.max())
    print()
    print("Children of Root:", [child.val if child != None else None for child in root.children])
    d = root.delete(0)
    print("\nDelete Node 0:")
    print(d)
    print("\nChildren of Root:", [child.val if child != None else None for child in root.children])
    d = root.delete(1)
    print("\nDelete Node 1:")
    print(d)
    print("\nChildren of Root:", [child.val if child != None else None for child in root.children])
    print("\nNew Tree:")
    print(root)
    print()
    print("Operations")
    print(f"{root.get_node(0).val} == {root.get_node(5).val} evaluates to: {root.get_node(0) == 100}")
    print()
    print(root.get_node(-1, 0).back_path())
    print()
    print("Searching")
    print(root.search(100, type="depth"))