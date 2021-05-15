from pdf import PDF
import numpy as np
from scipy.special import gamma

class TDistribution(PDF):

    name = "T"
    short = "T"
    inp = ["t"]
    parameters = ["nu"]

    def __init__(self, nu):
        self.nu = nu
        super(TDistribution, self).__init__(domain=[(-5, 5)])
    
    def distribution(self, t):
        return gamma((self.nu+1)/2.0) / (gamma(self.nu/2.0) * np.sqrt(np.pi * self.nu)) * (1 + t**2/self.nu)**(-(self.nu+1)/2.0)

if __name__ == "__main__":
    T = TDistribution(5)
    T.plot()