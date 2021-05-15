from pdf import PDF
import numpy as np
from scipy.special import gamma

class Poisson(PDF):

    name = "Poisson"
    short = "Poi"
    inp = ["x"]
    parameters = ["lambda", "t"]

    def __init__(self, L, t):
        self.L = L
        self.t = t
        super(Poisson, self).__init__(domain=[(0, 20)])

    def distribution(self, x):
        return np.exp(-self.L * self.t) * (self.L * self.t)**x / gamma(x+1)

if __name__ == "__main__":
    Poi = Poisson(10, 0.1)
    Poi.plot()
