from pdf import PDF
import numpy as np
from scipy.special import gamma

class Gamma(PDF):

    name = "Gamma"
    short = "G"
    inp = ["x"]
    parameters = ["a", "b"]

    def __init__(self, a, b):
        self.a = a
        self.b = b
        super(Gamma, self).__init__(domain=[(0, 20)])
    
    def distribution(self, x):
        return (1.0/(self.b**self.a * gamma(self.a))) * x**(self.a-1) * np.exp(-x/self.b)

if __name__ == "__main__":
    G = Gamma(2, 3)
    G.plot()