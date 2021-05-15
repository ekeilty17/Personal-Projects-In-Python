from pdf import PDF
import numpy as np
from scipy.special import gamma

class FDistribution(PDF):
    
    name = "F"
    short = "F"
    inp = ["x"]
    parameters = ["v1", "v2"]
    
    def __init__(self, v1, v2):
        self.v1 = v1
        self.v2 = v2
        super(FDistribution, self).__init__(domain=[(0, 4)])
    
    def distribution(self, f):
        coef = ( gamma((self.v1+self.v2)/2.0) * (self.v1/self.v2)**(self.v1/2.0) ) / ( gamma(self.v1/2.0) * gamma(self.v2/2.0) )
        return coef * f**(self.v1/2.0 - 1) / ( (1 + self.v1*f/self.v2)**((self.v1+self.v2)/2) )

if __name__ == "__main__":
    F = FDistribution(2, 3)
    F.plot()