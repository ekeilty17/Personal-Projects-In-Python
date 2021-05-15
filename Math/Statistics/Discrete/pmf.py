import sys
sys.path.append("..")
from probability_function import Probability_Function

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import matplotlib.cm as cm
from mpl_toolkits.mplot3d import Axes3D

class PMF(Probability_Function):

    """ Abstract class for a general Probability Mass Function (discrete probability function) """
    
    name = "PMF"
    short = "P"
    inp = []
    parameters = []

    def __init__(self, domain):
        self.domain = domain
        self.dim = len(domain)
        super(PMF, self).__init__()

    def __mul__(self, other):
        # because of the circular imports, I need to do it like this
        import joint_pmf
        return joint_pmf.JointPMF(self, other)

    def is_always_positive(self):
        return True

    def is_normalized(self):
        return True
    
    def get_CMF(self):
        pass

    def plot(self):
        if self.dim == 1:
            X = np.arange(*(self.domain[0]))
            P = np.vectorize(self.distribution)(X)
            plt.bar(X, P, align='center', width=1.0, edgecolor='black')
            plt.xticks(ticks=X, labels=X)
            
            # labels
            plt.xlabel(self.inp[0])
            plt.ylabel(f"{self.short}({', '.join(self.inp)}{'; ' if len(self.parameters) != 0 else ''}{', '.join(self.parameters)})")
            plt.title(self.name + " Distribution")
            
            plt.show()
        
        elif self.dim == 2:
            
            fig = plt.figure()
            ax = Axes3D(fig)
            
            X1 = np.arange(*(self.domain[0]))
            X2 = np.arange(*(self.domain[1]))
            X1_mesh, X2_mesh = np.meshgrid(X1, X2)
            
            P = np.array([ self.distribution(x1, x2) for x1 in X1 for x2 in X2 ])
            bottom = np.zeros_like(P)   # zeros in the same of P

            dx1 = np.ones_like(P)       # ones in the same of P
            dx2 = np.ones_like(P)       # ones in the same of P

            # getting colors
            offset = P + np.abs(P.min())
            fracs = offset.astype(float)/offset.max()
            norm = colors.Normalize(fracs.min(), fracs.max())
            color_values = cm.jet(norm(fracs.tolist()))

            ax.bar3d(X1_mesh.flatten(), X2_mesh.flatten(), bottom, dx1, dx2, P, shade=True, color=color_values)
            
            # labels
            ax.set_xlabel(self.inp[0])
            ax.set_ylabel(self.inp[1])
            ax.set_zlabel(f"{self.short}({', '.join(self.inp)}{'; ' if len(self.parameters) != 0 else ''}{', '.join(self.parameters)})")
            ax.set_title(self.name)
            
            plt.show()
        else:
            raise ValueError("I don't know how to plot things in higher than 3 dimensions")


if __name__ == "__main__":

    P = PMF(domain=[(0, 10)])
    P.set_distribution(lambda x: x**2)
    P.plot()