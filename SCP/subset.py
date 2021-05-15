class subset:
    
    def __init__(self, cost, elements):
        
        if type(cost) != int and type(cost) != float:
            raise TypeError("Type of 'cost' needs to be a number")
        self.cost = cost
        
        if type(elements) == list:
            print "Warning: Conversion of list to sets will remove duplicate elements"
            self.elements = set(elements)
        elif type(elements) == tuple:
            print "Warning: Conversion of tuple to sets will remove duplicate elements"
        elif type(elements) != set:
            raise TypeError("Type of 'elements' needs to be a set")
        self.elements = elements

    def Display(self):
        out = "Id: " + str(id(self)) + ",\t\tCost: " + str(self.cost) + ",\tElements: " + str(self.elements)
        print out
        return out
    
    # Getters and Setters
    def getId(self):
        return id(self)
    
    def getCost(self):
        return self.cost

    def getElements(self):
        return self.elements

    def setCost(self, cost):
        self.cost = cost

    def setElements(self, elements):
        if type(elements) == list:
            print "Warning: Conversion of list to sets will remove duplicate elements"
            self.elements = set(elements)
        elif type(elements) == tuple:
            print "Warning: Conversion of tuple to sets will remove duplicate elements"
        elif type(elements) != set:
            raise TypeError("Type of 'elements' needs to be a set")
        self.elements = elements
