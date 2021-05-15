from pmf import PMF
from nCr import multinomial_coef
import numpy as np

class Multinomial(PMF):

    name = "Mutlinomial"
    short = "Mult"

    def __init__(self, n, *P):
        if n < 1 or int(n) != n:
            raise ValueError("n must be an integer greater than 1")

        for p in P:
            if not (0 <= p <= 1):
                raise ValueError("p is a probability and needs to be in [0, 1]")

        # not sure if this needs to be true
        """
        if sum(P) != 1:
            raise ValueError
        """

        self.n = n
        self.P = list(P)
        super(Multinomial, self).__init__(domain=[(0, n+1)]*len(self.P))
        self.inp = ["x" + str(i+1) for i in range(self.dim)]
        self.parameters = ["p" + str(i+1) for i in range(self.dim)]

    def distribution(self, *args):
        return multinomial_coef(self.n, *args) * np.prod([p**x for p, x in zip(self.P, args)])
    
if __name__ == "__main__":

    Mu = Multinomial(10, 0.6, 0.1)
    Mu.plot()