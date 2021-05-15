class Heap:

    def __init__(self, store=[], cmp=None):
        self.cmp = self.default_cmp if cmp == None else cmp
        self._store = []
        self.add(store)

    """ Operator Overloading """
    def __str__(self):
        return str(self._store)
    
    def __len__(self):
        return len(self._store)
    
    def __getitem__(self, i):
        return self._store[i]
    
    def __add__(self, arg):
        H = self.copy()
        if isinstance(arg, Heap):
            H.add(arg._store)
        else:
            H.add(arg)
        return H
    
    def __iter__(self):
        return iter(self._store)

    """ Helper Functions """
    def pretty(self):
        def rec(i, indent="", out=""):
            out += indent + str(H[i]) + "\n"
            for c in self.getChildren(i):
                out += rec(c, indent + "\t", "")
            return out
        return rec(0)

    def copy(self):
        return Heap(store=self._store[:], cmp=self.cmp)

    def getParent(self, i):
        if i <= 0:
            return None
        if i % 2 == 0:
            return (i-2)//2
        else:
            return (i-1)//2
    
    def getChildren(self, i):
        if 2*i+1 >= len(self):
            return []
        if 2*i+2 >= len(self):
            return [2*i+1]
        return [2*i+1, 2*i+2]

    def isEmpty(self):
        return len(self) == 0

    def _swap(self, i, j):
        if i < 0:
            i += len(self)
        if j < 0:
            j += len(self)
        self._store[i], self._store[j] = self._store[j], self._store[i]

    def _bubble_up(self, c):
        p = self.getParent(c)
        if p != None:
            if not self.cmp(self[p], self[c]):
                self._swap(p, c)
                self._bubble_up(p)
    
    def _bubble_down(self, p):
        if len(self) > 1:
            # want to swap the parent with the child that maintains the heap structure
            best_swap = p
            for c in self.getChildren(p):
                if not self.cmp(self[best_swap], self[c]):
                    best_swap = c
            if best_swap != p:
                self._swap(p, best_swap)
                self._bubble_down(best_swap)

    """
    The compare function is not very intuitive, but I think this is the best compromise
    Whatever you want the structure of the heap to be is how you write the compare function
    A better name for this function might be isHeap(), but I'm keeping with convensions
    For example, the default_cmp function creates a max heap. So we want the value of the parents
    to be greater than that of its children for all nodes. Therefore p > c == True
    
    When writing to heap_sort(), saying p > c is analogous to saying i > i+1 in the list
    Thus a max heap will produce a descending list
    """
    def default_cmp(self, p, c):
        return p > c

    """ User Functions """
    def add(self, *args):
        for arg in args:
            if type(arg) == list:
                for val in arg:
                    self.add(val)
            else:
                self._store += [arg]
                self._bubble_up(len(self)-1)

    def remove_index(self, i):
        if not self.isEmpty():
            if i < 0:
                i += len(self)
            self._swap(i, -1)
            self._store = self._store[:-1]
            self._bubble_down(i)

    def remove_value(self, key):
        if not self.isEmpty():
            if key in self:
                self.remove_index( self._store.index(key) )
       
    # remove root
    def extract(self):
        if self.isEmpty():
            return None
        root = self[0]
        self.remove_index(0)
        return root

def heap_sort(L, cmp=lambda a, b: a < b):
    H = Heap(store=L, cmp=cmp)
    return [H.extract() for i in range(len(H))]

if __name__ == "__main__":

    def min_heap(p, c):
        return p < c

    H = Heap(cmp=min_heap)
    H.add([1, 20, 10, 30])
    print(H)
    H.add([100, -5, 20])
    print(H)
    print(H.pretty())

    print( heap_sort([1, 20, 10, 30, 100, -5, 20]) )
    
