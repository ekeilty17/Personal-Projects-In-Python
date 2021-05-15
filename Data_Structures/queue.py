class Queue(object):
    
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

    def __add__(self, Q):
        if type(Q) == list:
            return Queue(self._store + Q)
        return Queue(self._store + Q._store)

    def __iter__(self):
        return iter(self._store)

    def isEmpty(self):
        return len(self) == 0
    
    def enq(self, val):
        self._store += [val]

    def deq(self):
        if self.isEmpty():
            return False
        r = self._store[0]
        self._store = self._store[1:]
        return r
    

if __name__ == "__main__":
    Q = Queue()
    print(Q)
    Q.enq(10)
    print(Q)
    Q.enq(20)
    print(Q)
    Q.enq(30)
    print(Q)
    Q.enq(40)
    print(Q)
    print()   
    for i in range(len(Q)):
        Q.deq()
        print(Q)
    
