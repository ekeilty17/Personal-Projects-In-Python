from pmf import PMF
from nCr import nCr

class NegativeBinomial(PMF):

    name = "Negative Binomial"
    short = "NegBin"
    inp = ["n"]
    parameters = ["k", "p"]

    def __init__(self, k, p):
        if k < 1 or int(k) != k:
            raise ValueError("n must be an integer greater than 1")

        if not (0 <= p <= 1):
            raise TypeError("p is a probability and needs to be in [0, 1]")
        
        self.k = k
        self.p = p
        super(NegativeBinomial, self).__init__(domain=[(k, k + 50)])
    
    def distribution(self, n):
        return nCr(n-1, self.k-1) * self.p**self.k * (1 - self.p)**(n - self.k)
    
if __name__ == "__main__":
    NegBin = NegativeBinomial(3, 0.1)
    NegBin.plot()