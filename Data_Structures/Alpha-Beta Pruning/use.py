from general_alphabeta_tree import *

class specific_alphabeta_tree(general_alphabeta_tree):

    def __init__(self, val, isMaximizingPlayer=True):
        general_alphabeta_tree.__init__(self, val, isMaximizingPlayer)

    def evaluation(self):
        # Parameter:        void
        # Return Type:      float
        #   A higher is a more prefered state
        # Implementation:   REQUIRED
        return self.val.evaluation()

    def isLeaf(self):
        # Parameter:        void
        # Return Type:      boolean
        #   True = Node is a leaf node, i.e. no more Edges exist
        #   False = Node is not a lead node
        # Implementation:   REQUIRED
        return self.val.isComplete()

    def getEdges(self):
        # Parameter:        void
        # Return Type:      A list of Edges
        #   See comments in self.search() for my definition of an Edge
        # Implementation:   REQUIRED
        return self.val.getEdges()

    def copy_node(self):
        # Parameter:        void
        # Return Type:      Child class that implements the general_alphabeta_tree
        # Implementation:   REQUIRED
        return specific_alphabeta_tree( self.val.copy_val(), self.isMaximizingPlayer )

    def evolve(self, E):
        # Parameter:        An Edge
        # Return Type:      Child class that implements the general_alphabeta_tree
        # Implementation:   REQUIRED
        self.val.evolve(E)
        return self

# Using the specific implementation of the general_search_tree
#   If you want the function to search until it hits a leaf node, then set depth = -1
bestChild = specific_alphabeta_tree( curr_state, isMaximizingPlayer ).getBestChild(depth)
