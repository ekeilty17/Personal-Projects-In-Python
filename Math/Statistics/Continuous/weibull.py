from pdf import PDF
import numpy as np
from scipy.special import gamma

class Weibull(PDF):

    name = "Weibull"
    short = "W"
    inp = ["x"]
    parameters = ["a", "b"]

    def __init__(self, a, b):
        self.a = a
        self.b = b
        super(Weibull, self).__init__(domain=[(0, 2)])

    def distribution(self, x):
        return self.a*self.b*x**(self.b-1)*np.exp(-self.a*x**self.b)

if __name__ == "__main__":
    W = Weibull(2, 3)
    W.plot()