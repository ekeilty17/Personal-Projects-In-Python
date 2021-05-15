from pdf import PDF
import numpy as np
from scipy.special import gamma

class ChiSquared(PDF):

    name = "Chi-Squared"
    short = "X^2"
    inp = ["x"]
    parameters = ["nu"]

    def __init__(self, nu):
        self.nu = nu
        super(ChiSquared, self).__init__(domain=[(0, 10)])

    def distribution(self, x):
        return (1.0/(2**(self.nu/2.0) * gamma(self.nu/2.0))) * x**(self.nu/2.0 - 1) * np.exp(-x/2.0)

if __name__ == "__main__":
    X = ChiSquared(3)
    X.plot()