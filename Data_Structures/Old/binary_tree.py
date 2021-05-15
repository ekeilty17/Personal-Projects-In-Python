# TODO: add deletion

class BinaryTree(object):
    """ A general binary tree, not a binary search tree. The user has full control over what values go into each node """

    def __init__(self, val=None):
        self.val = None
        self.left = None
        self.right = None
        if type(val) == list:
            for x in val:
                self.add_in_order(x)
        elif isinstance(val, self.__class__):
            self = val.copy()
        else:
            self.val = val

    """ Operator Overloading """
    def __str__(self):
        if self.val == None:
            return ""
        def rec(B, indent, out):
            out += indent + str(B.val) + "\n"
            if B.right != None:
                out += rec(B.right, indent + "\t", "")
            if B.left != None:
                out += rec(B.left, indent + "\t", "")
            return out
        return rec(self, "", "")[:-1]

    # gives number of nodes in the tree
    def __len__(self):
        if self.val == None:
            return 0
        accum = 1
        if self.left != None:
            accum += len(self.left)
        if self.right != None:
            accum += len(self.right)
        return accum

    def __getitem__(self, i):
        if self == None or self.val == None:
            raise IndexError
        if i == -1:
            return self.left
        elif i == 0:
            return self
        elif i == 1:
            return self.right
        else:
            raise IndexError

    def __setitem__(self, i, val):
        if self.val == None:
            raise IndexError
        if i == -1:
            self.add_left(val)
        elif i == 0:
            if isinstance(val, self.__class__):
                self.val = val.val
            else:
                self.val = val
        elif i == 1:
            self.add_right(val)
        else:
            raise IndexError

    """ Helper Functions """
    def copy(self):
        B = self.__class__(self.val)
        def rec(B1, B2):
            if B1.left != None:
                B2.add_left(B1.left.val)
                rec(B1.left, B2.left)
            if B1.right != None:
                B2.add_right(B1.right.val)
                rec(B1.right, B2.right)
        rec(self, B)
        return B
    
    def get_node(self, *path):
        curr = self
        for i in path:
            curr = curr[i]
        return curr

    """ Writing to Tree """ 
    def add_left(self, B):
        if self.val == None:
            raise TypeError
        if isinstance(B, self.__class__):
            self.left = B
        else:
            self.left = self.__class__(B)

    def add_right(self, B):
        if self.val == None:
            raise TypeError
        if isinstance(B, self.__class__):
            self.right = B
        else:
            self.right = self.__class__(B)
    
    def delete_left(self):
        self.left = None
    
    def delete_right(self):
        self.right = None

    """ Rotations """
    def rotate_right(self):
        if self.left == None:
            return None
        
        t1 = self.left
        t2 = t1.right
        t1.right = self
        self.left = t2
        return t1

    def rotate_left(self):
        if self.right == None:
            return None

        t1 = self.right
        t2 = t1.left
        t1.left = self
        self.right = t2
        return t1

    def double_rotate_left(self):
        if self.right == None:
            return self
        
        self.right = self.right.rotate_right()
        return self.rotate_left()
    
    def double_rotate_right(self):
        if self.left == None:
            return self

        self.left = self.left.rotate_left()
        return self.rotate_right()

    """ Reading From Tree """
    def depth_first(self):
        return self.pre_order()
    
    def breadth_first(self):
        return self.level_order(flat=True)
    
    def pre_order(self):
        if self.val == None:
            return []
        def pre_order_rec(node, L):
            L += [node.val]
            if node.left != None:
                pre_order_rec(node.left, L)
            if node.right != None:
                pre_order_rec(node.right, L)
            return L
        return pre_order_rec(self, [])

    def in_order(self):
        if self.val == None:
            return []
        def in_order_rec(node, L):
            if node.left != None:
                in_order_rec(node.left, L)
            L += [node.val]
            if node.right != None:
                in_order_rec(node.right, L)
            return L
        return in_order_rec(self, [])
    
    def post_order(self):
        if self.val == None:
            return []
        def post_order_rec(node, L):
            if node.left != None:
                post_order_rec(node.left, L)
            if node.right != None:
                post_order_rec(node.right, L)
            L += [node.val]
            return L
        return post_order_rec(self, [])
    
    def level_order(self, flat=False):
        if self.val == None:
            return []
        out = []
        q = [self]
        while len(q) != 0:
            count = len(q)
            temp = []
            while count > 0: 
                B = q.pop()
                temp += [B.val]
                if B.left != None:
                    q.insert(0, B.left)
                if B.right != None:
                    q.insert(0, B.right)
                count -= 1
            out += [temp]
        if flat:
            return [x for L in out for x in L]
        return out
    
    # Have to write it this way since I cannot gaurentee the user will use the add_in_order function
    def min(self):
        def min_rec(B, curr_min):
            L = B if B.val < curr_min.val else curr_min
            R = B if B.val < curr_min.val else curr_min
            if B.left != None:
                L = min_rec(B.left, L)
            if B.right != None:
                R = min_rec(B.right, R)
            return L if L.val < R.val else R
        return min_rec(self, self)
    
    def max(self):
        def max_rec(B, curr_max):
            L = B if B.val > curr_max.val else curr_max
            R = B if B.val > curr_max.val else curr_max
            if B.left != None:
                L = max_rec(B.left, L)
            if B.right != None:
                R = max_rec(B.right, R)
            return L if L.val > R.val else R
        return max_rec(self, self)

if __name__ == "__main__":
    
    """ How to create a Generally Binary Tree """

    # Using .right and .left class variables
    root = BinaryTree(40)
    root.right = BinaryTree(20)
    root.left = BinaryTree(10)
    root.left.left = BinaryTree(-10)
    root.left.left.left = BinaryTree(-40)

    # Using .get_node() method
    """
    root = BinaryTree(40)
    root.right = BinaryTree(20)
    root.left = BinaryTree(10)
    root.get_node(-1).left = BinaryTree(-10)
    root.get_node(-1, -1).left = BinaryTree(-40)
    """

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