class Stack:
    def __init__(self, store=[]):
        self.store = store[:]
    
    def isEmpty(self):
        return len(self.store) == 0

    def push(self,val):
        self.store += [val]

    def pop(self):
        if self.isEmpty():
            return None
        r = self.store[-1]
        self.store = self.store[:-1]
        return r