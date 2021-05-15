from general_search_tree import *

# The specific_search_tree inherits all methods from the general_search_tree
#   I think of this like an interface in Java, all you have to do
#   is define specific implementations of the required methods
#   and then you get the self.search() method for free
# I've provided examples of generally what the return statement of each function would look like
class specific_search_tree(general_search_tree):

    def __init__(self, val):
        general_search_tree.__init__(self, val)

    #NOTE: The Methods below assume val is a class, but it doesn't have to be

    def isSolution(self):
        # Parameter:        void
        # Return Type:      boolean
        #   True = state is a solution to the problem being solved
        #   False = keep searching
        # Implementation:   REQUIRED
        return self.val.isSolution()

    def prune(self):
        # Parameter:        void
        # Return Type:      boolean
        #   True = prune the branch, meaning stop searching down this path
        #   False = don't prune the branch, meaning continue searching
        # Implementation:   OPTIONAL
        return False

    def getEdges(self):
        # Parameter:        void
        # Return Type:      A list of Edges
        #   See comments in self.search() for my definition of an Edge
        # Implementation:   REQUIRED
        return self.val.getEdges()

    def heuristic(self, L):
        # Parameter:        Unordered list of Edges
        # Return Type:      Ordered list of Edges
        # Implementation:   OPTIONAL
        return L

    def copy_node(self):
        # Parameter:        void
        # Return Type:      Child class that implements the general_search_tree class
        # Implementation:   REQUIRED
        return specific_search_tree( self.val.copy_val() )

    def evolve(self, E):
        # Parameter:        An Edge
        # Return Type:      Child class that implements the general_search_tree class
        # Implementation:   REQUIRED
        self.val.evolve(E)
        return self

    def Display(self):
        # Parameter:        void
        # Return Type:      Void
        # Implementation:   OPTIONAL
        return self.val.Display()


# Using the specific implementation of the general_search_tree
leaf = specific_search_tree(intial_state).search()

if leaf == False:
    print []
else:
    L = leaf.back_track()
    for x in L:
        x.Display()
