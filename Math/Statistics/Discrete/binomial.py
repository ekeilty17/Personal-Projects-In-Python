from pmf import PMF
from nCr import nCr

class Binomial(PMF):

    name = "Binomial"
    short = "Bin"
    inp = ["k"]
    parameters = ["p"]

    def __init__(self, n, p):
        if n < 1 or int(n) != n:
            raise ValueError("n must be an integer greater than 1")

        if not (0 <= p <= 1):
            raise ValueError("p is a probability and needs to be in [0, 1]")

        self.n = n
        self.p = p
        super(Binomial, self).__init__(domain=[(0, n+1)])
    
    def distribution(self, k):
        return nCr(self.n, k) * self.p**k * (1 - self.p)**(self.n - k)


if __name__ == "__main__":
    Bin = Binomial(10, 0.5)
    Bin.plot()