class Set(object):
    """ Class whose purpose is to replicate sets in python...just for the fun of it """

    def __init__(self, iter=[], size=101):
        self.size = size
        self._store = [ [] for _ in range(size) ]
        for x in iter:
            self.add(x)
    
    """ Operation Overloading """
    def __str__(self):
        out = ""
        for L in self._store:
            for x in L:
                if type(x) == str:
                    out += "'" + x + "'"
                else:
                    out += str(x)
                out += ", "
        return "Set([" + out[:-2] + "])"
    
    def __len__(self):
        return sum([ len(L) for L in self._store ])
    
    def __or__(self, other_set):
        return self.union(other_set)
    
    def __and__(self, other_set):
        return self.intersection(other_set)

    def __sub__(self, other_set):
        return self.difference(other_set)
    
    def __xor__(self, other_set):
        return self.symmetric_difference(other_set)
    
    def __eq__(self, other_set):
        return self.issubset(other_set) and other_set.issubset(self)
    
    def __ne__(self, other_set):
        return not self.__eq__(other_set)
    
    def __lt__(self, other_set):
        return self.issubset(other_set) and len(self) != len(other_set)
    
    def __gt__(self, other_set):
        return self.issuperset(other_set) and len(self) != len(other_set)
    
    def __le__(self, other_set):
        return self.issubset(other_set)
    
    def __ge__(self, other_set):
        return self.issuperset(other_set)

    def __iter__(self):
        return iter( [x for L in self._store for x in L] )
    
    """ Helper Functions """
    def _hash(self, x):
        return abs(hash(x) % self.size)
    
    def clear(self):
        self._store = [ [] for _ in range(size) ]
    
    def copy(self):
        S = Set(size=self.size)
        S._store = [ L[:] for L in self._store ]
        return S

    """ Write to Set """
    def add(self, element):
        if element not in self._store[ self._hash(element) ]:
            self._store[ self._hash(element) ] += [element]
    
    def update(self, other_set):
        for o in other_set:
            self.add(o)
    
    def remove(self, element):
        try:
            self._store[ self._hash(element) ].remove(element)
        except Exception:
            raise KeyError(element)
    
    def discard(self, element):
        try:
            self._store[ self._hash(element) ].remove(element)
        except Exception:
            pass
    
    """ Set Operations """
    def union(self, *other_sets):
        S = self.copy()
        for O in other_sets:
            for x in O:
                S.add(x)
        return S
    
    def intersection(self, *other_sets):
        S = self.copy()
        for O in other_sets:
            for x in S:
                if x not in O:
                    S.discard(x)
        return S

    def intersection_update(self, *other_sets):
        for O in other_sets:
            for x in self:
                if x not in O:
                    self.discard(x)
    
    def difference(self, other_set):
        S = self.copy()
        for element in other_set:
            S.discard(element)
        return S
    
    def difference_update(self, other_set):
        for element in other_set:
            self.discard(element)
    
    def symmetric_difference(self, other_set):
        #return self.union(other_set).difference( self.intersection(other_set) )
        return self.difference(other_set).union( other_set.difference(self) )
    
    def symmetric_difference_update(self, other_set):
        #S = self.union(other_set).difference( self.intersection(other_set) )
        S = self.difference(other_set).union( other_set.difference(self) )
        self._store = S._store
    
    def isdisjoint(self, other_set):
        return len(self.intersection(other_set)) == 0
    
    def issubset(self, other_set):
        #return other_set.issuperset(self)
        for x in self:
            if x not in other_set:
                return False
        return True

    def issuperset(self, other_set):
        #return other_set.issubset(self)
        for o in other_set:
            if o not in self:
                return False
        return True

if __name__ == "__main__":
    S = Set([1, 2, 3, 4])
    T = Set([1, 2, 3, 4, 5])
    print("S =", S)
    print("T =", T)
    print(S == T)
