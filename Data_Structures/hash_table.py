class HashTable(object):
    """ Class whose purpose is to replicate dictionaries in python...just for the fun of it """

    def __init__(self, size=101):
        self.size = size
        self._store = [ [] for _ in range(size) ]
    
    """ Operation Overloading """
    def __len__(self):
        return sum([ len(L) for L in self._store ])

    def __str__(self):
        out = ""
        for L in self._store:
            for k, v in L:
                if type(k) == str:
                    out += "'" + k + "'"
                else:
                    out += str(k)
                out += ": "
                if type(v) == str:
                    out += "'" + v + "'"
                else:
                    out += str(v)
                out += ", "
        return "{" + out[:-2] + "}"
    
    def __setitem__(self, key, value):
        return self.add(key, value)

    def __getitem__(self, key):
        return self.get(key)

    def __delitem__(self, key):
        self.pop(key)

    def __add__(self, H):
        T = self.copy()
        T.update(H)
        return TabError

    def __iter__(self):
        return iter(self.keys())

    """ Helper Functions """
    def _hash(self, x):
        return abs(hash(x) % self.size)
    
    def pretty(self):
        out = ""
        for k in sorted(self, key=str):
        #for k in self:
            v = self[k]
            out += '\033[92m'
            if type(k) == str:
                out += "'" + k + "'"
            else:
                out += str(k)
            out += "\033[0m: "
            if type(v) == str:
                out += "\033[93m'" + v + "'\033[0m"
            elif type(v) == int or type(v) == float:
                out += "\033[96m" + str(v) + "\033[0m"
            elif type(v) == bool or v == None:
                out += "\033[95m" + str(v) + "\033[0m"
            else:
                out += str(v)
            out += "\n"
        return out[:-1]

    def clear(self):
        self._store = [ [] for _ in range(size) ]
    
    def copy(self):
        H = HashTable(self.size)
        H._store = [ L[:] for L in self._store ]
        return H
    
    """ Writing to Hash Table """
    def add(self, key, val):
        for i, (k, v) in enumerate(self._store[ self._hash(key) ]):
            if k == key:
                self._store[ self._hash(key) ][i] = (key, val)
                return None
        else:
            self._store[ self._hash(key) ] += [(key, val)]
    
    def setdefault(self, key, default_value=None):
        for k, v in self._store[ self._hash(key) ]:
            if k == key:
                return None
        self.add(key, default_value)

    def delete(self, key, val):
        for k, v in self._store[ self._hash(key) ]:
            if k == key and v == val:
                self._store[ self._hash(key) ].remove((k, v))
    
    def pop(self, key):
        for k, v in self._store[ self._hash(key) ]:
            if k == key:
                self._store[ self._hash(key) ].remove((k, v))
                return (k, v)
        else:
            raise IndexError

    def update(self, H):
        for key, val in H.items():
            self.add(key, val)
    
    def fromkeys(self, Keys):
        if type(Keys) != list:
            raise TypeError
        for key in Keys:
            self.add(key, None)

    """ Reading from Hash Table """
    def get(self, key):
        for k, v in self._store[ self._hash(key) ]:
            if k == key:
                return v
        else:
            raise IndexError
    
    def _key_from_value(self, val):
        for L in self._store:
            for k, v in L:
                if v == val:
                    return k
        else:
            raise IndexError

    def items(self):
        return [ (k, v) for L in self._store for k, v in L ]

    def keys(self):
        return [ k for L in self._store for k, _ in L ]

    def values(self):
        return [ v for L in self._store for _, v in L ]
    
    
    

if __name__ == "__main__":
    H = HashTable()
    H["My firstname"] = "Eric"
    H["person"] = "Cleo"
    H["my lastname"] = "Keilty"
    H["Hello"] = "World!"
    H["Streaming"] = "Netflix"
    H["GF"] = "Nkemjika"
    H["great show"] = "The Office"
    H["prof"] = "Nebu"
    H["course"] = "Praxis!"
    H["prof"] = "Me"
    H["character"] = "Micheal Scott"
    H[2] = 1
    H["test"] = 10.0
    H["test2"] = ("hi", [1, 2])
    H["test3"] = True
    H["test4"] = None
    print(H.pretty())