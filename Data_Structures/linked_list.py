# TODO make more efficient by storing length and end node

class List(object):
    """ Class whose purpose is to replicate lists in python...just for the fun of it """

    def __init__(self, *args, unpack=True):
        self.val = None
        self.next = None
        self.isEmpty = True
        
        if not unpack:
            self.val = args[0]
            self.isEmpty = False
        else:
            if len(args) == 1:
                try:
                    args = iter(args[0])
                except Exception:
                    pass
            if args != ():
                for x in args:
                    self.append(x)
                self.isEmpty = False
    
    """ Operation Overload """
    def __str__(self):
        if self.isEmpty:
            return "[]"
        out, curr = "[", self
        while curr != None:
            out += str(curr.val) + ", "
            curr = curr.next
        return out[:-2] + "]"

    def __len__(self):
        if self.isEmpty:
            return 0
        curr = self
        cnt = 0
        while curr != None:
            cnt += 1
            curr = curr.next
        return cnt
    
    # This is definitely not optimized
    def __getitem__(self, index):
        if type(index) == slice:
            L = List()
            start = index.start if index.start != None else 0
            stop = index.stop if index.stop != None else len(self)
            if stop < 0:
                stop += len(self)
            step = index.step if index.step != None else 1
            
            for i in range(start, stop, step):
                L.append(self.get_node(i).val)
            return L
        else:
            return self.get_node(index).val
    
    # This is definitely not optimized
    def __setitem__(self, index, x):
        if type(index) == slice:
            start = index.start if index.start != None else 0
            stop = index.stop if index.stop != None else len(self)
            if stop < 0:
                stop += len(self)
            step = index.step if index.step != None else 1

            # edge case
            if (start, stop, step) == (0, len(self), 1):
                self.clear()
                self.extend(x)
            # edge case
            elif start > len(self):
                self.extend(x)
            # we want to be able to assing an arbitrary length if slice object is contiguous
            elif step == 1:
                # edge case
                if stop == len(self):
                    self.get_node(start-1).next = None
                else:
                    start_node = self.get_node(start)
                    for i in range(start, stop, step):
                        # replace start_node with values of successor
                        start_node.val = start_node.next.val
                        start_node.next = start_node.next.next
                    # insert list into what we just deleted
                    for i, val in enumerate(reversed(x)):
                        self.insert(start, val)
            # if step isn't 1, then you can't assign arbitrary length
            else:
                for i, val in zip(range(start, stop, step), x):
                    self.get_node(i).val = val
        else:
            self.get_node(index).val = x
    
    def __delitem__(self, index):
        curr = self.get_node(index)
        curr.val = curr.next.val
        curr.next = curr.next.next

    def __add__(self, other):
        if not isinstance(other, List):
            raise TypeError("'" + str(type(other)) + "' object is not iterable")
        L = self.copy()
        L.extend(other)
        L.isEmpty = self.isEmpty and other.isEmpty
        return L
    
    def __mul__(self, other):
        if type(other) != int:
            raise TypeError("can't multiply sequence by non-int of type '" + type(other) + "'")
        if self.isEmpty or other <= 0:
            return List()
        L = self.copy()
        for i in range(other-1):
            for x in self:
                L.append(x)
        L.isEmpty = False
        return L

    def __iter__(self):
        return self.copy()
    def __next__(self):
        if self.isEmpty:
            raise StopIteration
        x = self.val
        try:
            self.val = self.next.val
            self.next = self.next.next
        except Exception:
            self.val = None
            self.next = None
            self.isEmpty = True
        return x
    def next(self):
        return self.__next__()

    """ Helper Functions """
    def get_node(self, index):
        if self.isEmpty:
            raise IndexError("List index out of range")
        if index < 0:
            index += len(self)
        curr = self
        for i in range(index):
            try:
                curr = curr.next
            except Exception:
                raise IndexError("List index out of range")
        return curr
    
    def next_node(self, n):
        curr = self
        for i in range(n):
            curr = curr.next
        return curr

    def get_last_node(self):
        if self == None:
            return self
        curr = self
        while curr.next != None: curr = curr.next
        return curr
    
    def get_info(self):
        out, curr = "", self
        while curr != None:
            out += "node: " + str(id(curr)) + ", " + str(curr.val) + "\tnext: " + str(id(curr.next)) + ", " + str(curr.next) + "\n"
            curr = curr.next
        return out[:-1]

    """ User Functions """
    def append(self, x):
        if self.isEmpty:
            self.val = x
            self.isEmpty = False
        else:
            curr = self
            while curr.next != None: curr = curr.next
            curr.next = List(x, unpack=False)
    
    def extend(self, L):
        for x in L:
            self.append(x)
        
    def insert(self, index, x):
        # index == 0 is a weird edge case since I can't change the address of self, so I have to manipulate the class variables instead
        if index == 0:
            old_head_val = self.val
            old_head_next = self.next
            self.val = x
            self.next = List(old_head_val, unpack=False)
            self.next.next = old_head_next
        else:
            prev = self.get_node(index-1)
            curr = prev.next
            prev.next = List(x, unpack=False)
            prev.next.next = curr
    
    def pop(self, index=-1):
        if index == 0:
            return None
        else:
            prev = self.get_node(index-1)
            x = prev.next.val
            prev.next = prev.next.next
            return x
    
    def remove(self, x):
        curr = self
        while curr != None:
            if curr.val == x:
                curr.val = curr.next.val
                curr.next = curr.next.next
                break
            curr = curr.next
        else:
            raise ValueError("List.remove(x): x not in List")
    
    def index(self, x):
        curr = self
        cnt = 0
        while curr != None:
            if curr.val == x:
                return cnt
            curr = curr.next
            cnt += 1
        else:
            raise ValueError(str(x) + " is not in List")
    
    def count(self, x):
        curr = self
        cnt = 0
        while curr != None: 
            if curr.val == x:
                cnt += 1
            curr = curr.next
        return cnt
    
    def copy(self):
        if self.isEmpty:
            return List()
        L = List(self.val, unpack=False)
        curr, new_node = self, L
        curr = curr.next
        while curr != None:
            new_node.next = List(curr.val, unpack=False)
            new_node, curr = new_node.next, curr.next
        return L
    
    def clear(self):
        self.val = None
        self.next = None
        self.isEmpty = True

if __name__ == "__main__":
    L = List(0, 1, 2, 3, 4, 5, 6, 7)
    print(L)

        