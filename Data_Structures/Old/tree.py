class Tree(object):
    def __init__(self, root):
        self.val = root
        self.children = []

    """ Operator Overloading """
    def __str__(self):
        def rec(T, indent="", out=""):
            out += indent + str(T.val) + "\n"
            for child in T.children:
                out += rec(child, indent + "\t", "")
            return out
        return rec(self)

    # gives number of nodes in the tree
    def __len__(self):
        accum = 1
        for child in self.children:
            accum += len(child)
        return accum
    
    def __getitem__(self, i):
        return self.children[i]
    
    def __add__(self, arg):
        T = self.copy()
        if isinstance(arg, Tree):
            T.add_successor(arg.copy())
        else:
            T.add_successor(arg)
        return T

    def __iter__(self):
        return iter(self.children)

    """ Helper Functions """
    def copy(self):
        T = Tree(self.val)
        def rec(T1, T2):
            for child in T1:
                C = T2.add_successor(child.val)
                rec(child, C)
        rec(self, T)
        return T
    
    def get_node(self, *path):
        curr = self
        for i in path:
            curr = curr[i]
        return curr

    """ User Functions """
    def add_successor(self, arg):
        if isinstance(arg, Tree):
            self.children += [arg]
        elif type(arg) == list:
            self.children += arg
        else:
            self.children += [Tree(arg)]
        return self.children[-1]

    def depth_first(self, L=[]):
        L += [self.val]
        for child in self:
            L = child.depth_first(L)
        return L

    def breadth_first(self):
        return self.level_order(flat=True)

    def level_order(self, flat=False):
        out = []
        q = [self]
        while len(q) != 0:
            count = len(q)
            temp = []
            while count > 0: 
                T = q.pop()
                temp += [T.val]
                for child in T:
                    q.insert(0, child)
                count -= 1
            out += [temp]
        if flat:
            return [x for L in out for x in L]
        return out

if __name__ == "__main__":
    root = Tree(4)
    a = Tree(9)
    b = Tree(10)
    c = Tree(1)
    d = Tree(-1)

    root += [a, b, c, d]
    b.add_successor(100)
    d.add_successor(-30)

    g = Tree(500)
    g.add_successor(501)
    g.add_successor(502)

    print root.depth_first()
    print root.copy()
    print g
    print root.get_node(3, 0) + g
    # ^ is the same as d + g
    """
    print a
    print a.level_order()
    print a.level_order(flat=True)
    """