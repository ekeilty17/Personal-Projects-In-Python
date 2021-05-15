from pdf import PDF
import numpy as np

class Normal(PDF):

    name = "Normal"
    short = "N"
    inp = ["x"]
    parameters = ["mu", "sigma"]

    def __init__(self, mu, sigma):
        self.mu = mu
        self.sigma = sigma
        super(Normal, self).__init__(domain=[(mu - 4*sigma, mu + 4*sigma)])

    def distribution(self, x):
        return 1.0/(np.sqrt(2 * np.pi) * self.sigma) * np.exp( -(x - self.mu)**2 / (2*self.sigma**2) )
    
    # z-score
    def Z(self, x):
        return (x - self.mu) / self.sigma


class StandardNormal(Normal):

    name = "Standard Normal"
    short = "Z"
    parameters = []

    def __init__(self):
        super(StandardNormal, self).__init__(0, 1)


if __name__ == "__main__":
    N = Normal(4, 6)
    N.plot()
    
    Z = StandardNormal()
    Z.plot()