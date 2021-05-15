import sys
sys.path.append("..")
from probability_function import Probability_Function

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

class PDF(Probability_Function):

    """ Abstract class for a general Probability Distribution Function (continuous probability function) """
    
    name = "PDF"
    short = "P"
    inp = []
    parameters = []

    def __init__(self, domain):
        self.domain = domain
        self.dim = len(domain)
        super(PDF, self).__init__()

    def __mul__(self, other):
        # because of the circular imports, I need to do it like this
        import joint_pdf
        return joint_pdf.JointPDF(self, other)

    def is_always_positive(self):
        return True

    def is_normalized(self):
        return True
    
    def get_CDF(self):
        pass

    def plot(self, xlabels=None, plabel=None, title=None):
        if self.dim == 1:
            X = np.linspace(*(self.domain[0]), 100)
            P = np.vectorize(self.distribution)(X)
            plt.plot(X, P)

            # labels
            plt.xlabel(self.inp[0])
            plt.ylabel(f"{self.short}({', '.join(self.inp)}{'; ' if len(self.parameters) != 0 else ''}{', '.join(self.parameters)})")
            plt.title(self.name + "Distribution")

            plt.show()
        elif self.dim == 2:

            fig = plt.figure()
            ax = plt.axes(projection='3d')

            X1 = np.linspace(*(self.domain[0]), 100)
            X2 = np.linspace(*(self.domain[1]), 100)
            X1_mesh, X2_mesh = np.meshgrid(X1, X2)
            
            P = np.array([ [self.distribution(x1, x2) for x1 in X1] for x2 in X2 ])
            bottom = np.zeros_like(P)   # zeros in the same of P

            dx1 = np.ones_like(P)       # ones in the same of P
            dx2 = np.ones_like(P)       # ones in the same of P

            ax.plot_surface(X1_mesh, X2_mesh, P, cmap='viridis')

            # labels
            ax.set_xlabel(self.inp[0])
            ax.set_ylabel(self.inp[1])
            ax.set_zlabel(f"{self.short}({', '.join(self.inp)}{'; ' if len(self.parameters) != 0 else ''}{', '.join(self.parameters)})")
            ax.set_title(self.name)
            
            plt.show()

        else:
            raise ValueError("I don't know how to plot things in higher than 3 dimensions")