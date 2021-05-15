from pmf import PMF
from nCr import nCr

class Hypergeometric(PMF):

    name = "Hypergeometric"
    short = "H"
    inp = ["x"]
    parameters = ["N", "n", "k"]

    def __init__(self, N, n, k):
        if n > N:
            raise ValueError("n must be less than or equal to N, since N is the total number of objects and n is the number of trials performed")
        if k > N:
            raise ValueError("k must be less than or equal to N, since N is the total number of objects and k is the number of objects that are labeled successes")

        if int(N) != N or int(n) != n or int(k) != k:
            raise ValueError("All parameters must be integers")
            
        self.N = N
        self.n = n
        self.k = k
        # explanation of domain
        #   if n > N-k (number of failtures), then you have to at least choose n-(N-k) successes,
        #                                   therefore x in [n-(N-k), ...] 
        #   if k > n, then you can't pick more than n successes, therefore x in [..., n]
        #   Otherwise the intutive range of [0, k] applies
        super(Hypergeometric, self).__init__(domain=[(max(0, n+k-N), min(n, k)+1)])
    
    def distribution(self, x):
        return ( nCr(self.k, x) * nCr(self.N-self.k, self.n-x) ) / float(nCr(self.N, self.n))

if __name__ == "__main__":

    H = Hypergeometric(52, 13, 10)
    H.plot()

