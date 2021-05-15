class general_search_tree(object):
    """ The general search tree class a specific implementation of the tree class """
    def __init__(self,x):
        self.val = x
        self.children = []
        self.parent = None

    def AddSuccessor(self,T):
        self.children += [T]
        T.parent = self
        return True

    """ Helper Methods """
    # Some are optional and some the user MUST define an implementation

    def isSolution(self):
        """
        Parameter:        void \n
        Return Type:      bool \n
            True = state is a solution to the problem being solved
            False = keep searching
        Implementation:   REQUIRED
        """
        raise NotImplementedError("The method 'isSolution(self' was not implemented")

    def prune(self):
        """
        Parameter:        void \n
        Return Type:      bool \n
            True = prune the branch, meaning stop searching down this path
            False = dont prune the branch, meaning continue searching
        Implementation:   OPTIONAL
        """
        return False

    def getEdges(self):
        """
        Parameter:        void \n
        Return Type:      A list of Edges \n
            See comments in self.search() for my definition of an Edge
        Implementation:   REQUIRED
        """
        raise NotImplementedError("The method 'getEdges(self)' was not implemented")

    def heuristic(self, L):
        """
        Parameter:        Unordered list of Edges \n
        Return Type:      Ordered list of Edges \n
        Implementation:   OPTIONAL
        """
        return L

    def copy_node(self):
        """
        Parameter:        void \n
        Return Type:      Child class that implements the general_search_tree class \n
        Implementation:   REQUIRED
        """
        raise NotImplementedError("The method 'copy_node(self)' was not implemented")

    def evolve(self, E):
        """
        Parameter:        An Edge \n
        Return Type:      Child class that implements the general_search_tree class \n
        Implementation:   REQUIRED
        """
        raise NotImplementedError("The method 'evolve(self, E)' was not implemented")

    def Display(self):
        """
        Parameter:        void  \n
        Return Type:      void  \n
        Implementation:   OPTIONAL
        """
        pass

    def search(self):
        # If a node is not properly defined
        # of if we get to the end of the search tree
        if self == None:
            return False

        # Display Node. This is optional.
        self.Display()

        # Break case...solution found
        if self.isSolution():
            return self

        # Prune the path and stop if it proves to be futile
        if self.prune():
            return False

        # Getting set of next possible states
        # Edges is a list of all possible Edges
        #   Edges take the parent node to the child node
        #   For example if the game was chess, an edge would be moving a pawn to a2 to a4
        #   and the evolve function is responsible for handling that logic
        # child = evolve(parent, Edges[i])
        Edges = self.getEdges()

        # Since this is a depth first search rather than breadth first,
        # we are looking at one child at a time rather than all children
        # so if we have some type of heuristic to order which child we should look at
        # it can dramatically improve the time of the search
        Edges = self.heuristic(Edges)

        for E in Edges:
            # creating child
            #   copy.deepcopy() creates a copy of the current node
            #   evolve(parent, E) updates the state of the node to the next state based on the edge
            self.AddSuccessor( self.copy_node().evolve(E) )

            # searching
            r = self.children[-1].search()
            if r != False:
                # back propogating if we have found a solution
                return r
        return False

    def back_track(self, L=[]):
        # Catching bad input
        if self == None:
            return L
        # Break case at the end of the back tracking
        if self.parent == None:
            return L
        return self.parent.back_track([self.val] + L)
