from pmf import PMF

class JointPMF(PMF):

    def __init__(self, *args):
        self.pmfs = list(args)
        domain = []
        for pmf in self.pmfs:
            domain += pmf.domain
        super(JointPMF, self).__init__(domain=domain)
    
        self.name = ' x '.join([pmf.name for pmf in args])
        self.short = "Joint"
        self.inp = []
        self.parameters = []
        for i, pmf in enumerate(self.pmfs):
            # TODO add indexes to repeats
            self.inp += [inp + str(i+1) for inp in pmf.inp]
            self.parameters += [parameter + str(i+1) for parameter in pmf.parameters]

    def distribution(self, *args):
        if len(args) != self.dim:
            raise TypeError(f"expected {self.dim} arguments, got {len(args)}")
        
        accum = 1
        i = 0
        for pmf in self.pmfs:
            accum *= pmf.distribution(*(args[i:i+pmf.dim]))
            i += pmf.dim
        
        return accum

if __name__ == "__main__":
    from binomial import Binomial

    X = Binomial(10, 0.5)
    Y = Binomial(10, 0.3)
    #J = JointPMF(X, Y)
    J = X * Y
    J.plot()