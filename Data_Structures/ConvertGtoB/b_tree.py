class binary_tree:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

    def AddLeft(self,B):
        self.left = B
        return True

    def AddRight(self,B):
        self.right = B
        return True

    def Add_in_order(self, val):
        # Error case
        if self == None:
            return False
        
        # recursion
        if self.val > val:
            # Base case
            if self.left == None:
                self.left = binary_tree(val)
                return True
            return self.left.Add_in_order(val)
        else:
            # Base case
            if self.right == None:
                self.right = binary_tree(val)
                return True
            return self.right.Add_in_order(val)
    
    def Print_DepthFirst(self):
        def rec(x,indent):
            print indent + str(x.val)
            indent += "\t"
            if x.right != None:
                rec(x.right,indent)
            if x.left != None:
                rec(x.left,indent)
            return True

        return rec(self,"")
    
    def Print_InOrder(self):
        def rec(node):
            if node == None:
                return None
            rec(node.left)
            print node.val
            rec(node.right)
        rec(self)
