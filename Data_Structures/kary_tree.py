from tree import Tree

class KaryTree(Tree):

    """
    K-ary Tree implemented from the general Tree data structure where each node can have at most k children
    """

    def __init__(self, k=2, val=None):
        super(KaryTree, self).__init__(val)
        self.children = [None] * k
        self.k = k
    

    """ Magic Methods """


    """ Writing """
    def create_node(self, k=None, val=None):
        return KaryTree(    k=self.k if k == None else k, 
                            val=self.val if val == None else val
                        )
    
    # copy inherited from Tree class

    def convert_index(self, i):
        if i == 'p' or i == None:
            return i
        
        # allows for root[-1] indexing
        if i < 0:
            i += self.k
        
        # checking if valid index
        if i < 0 or i >= self.k:
            raise IndexError(f"Index out of range, there are exactly {self.k} children nodes")
        
        return i

    # insert_at_index inherited from Tree class

    def insert(self, arg=None):
        if arg == None:
            return self
        
        if type(arg) == list:
            for val in arg:
                self.insert(val)
            return self
        
        if None not in self.children:
            raise IndexError(f"Can't have more than {self.k} elements")

        i = self.children.index(None)
        return self.insert_at_index(i, arg)
    
    def delete(self, *path):
        return super(KaryTree, self).delete(*path, make_None=True)
    
    # All reading functions inherited from Tree class

if __name__ == "__main__":
    root = KaryTree(k=4, val=0)
    root.insert(1)
    root.insert(2)
    root.insert(3)
    root.insert(4)
    #root.insert(5)        # Throws error
    root[3] = 40

    root.get_node(0).insert(10)
    root.get_node(0).insert(11)
    root.get_node(1).insert(20)
    root.get_node(1, 0).insert(200)

    print(root)
    print()
    print(root.get_info(less=True))

    print("\nChildren of Root:", [child.val if child != None else None for child in root.children])

    d = root.delete(1)
    print("\nDelete Node 1:")
    print(d)
    print("\nChildren of Root:", [child.val if child != None else None for child in root.children])
    print("\nNew Tree:")
    print(root)