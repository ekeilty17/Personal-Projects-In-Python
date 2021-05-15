class Queue:
    def __init__(self, store=[]):
        self.store = store[:]
    
    def isEmpty(self):
        return len(self.store) == 0

    #had to rename the queue functions
    def push(self, val):
        self.store += [val]

    #so that it works generally
    def pop(self):
        if self.isEmpty():
            return None
        r = self.store[0]
        self.store = self.store[1:]
        return r