class Stack(object):

    def __init__(self, store=[]):
        self._store = store[:]

    def __str__(self):
        return str(self._store)
        
    def __len__(self):
        return len(self._store)

    def __getitem__(self, i):
        return self._store[i]

    def __delitem__(self, i):
        del self._store[i]
    
    def __add__(self, S):
        if type(S) == list:
            return Stack(self._store + S)
        return Stack(self._store + S._store)

    def __iter__(self):
        return iter(self._store)

    def isEmpty(self):
        return len(self) == 0
    
    def push(self,val):
        self._store += [val]

    def pop(self):
        if self.isEmpty():
            return False
        r = self._store[-1]
        self._store = self._store[:-1]
        return r
    

if __name__ == "__main__":
    S = Stack()
    print(S)
    S.push(10)
    print(S)
    S.push(20)
    print(S)
    S.push(30)
    print(S)
    S.push(40)
    print(S)
    print()
    for i in range(len(S)):
        S.pop()
        print(S)
