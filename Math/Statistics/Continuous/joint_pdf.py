from pdf import PDF

from normal import Normal
from gamma import Gamma

class JointPDF(PDF):

    def __init__(self, *args):
        self.pdfs = list(args)
        domain = []
        for pdf in self.pdfs:
            domain += pdf.domain
        super(JointPDF, self).__init__(domain=domain)

        self.name = ' x '.join([pdf.name for pdf in args])
        self.short = "Joint"
        self.inp = []
        self.parameters = []
        for i, pdf in enumerate(self.pdfs):
            # TODO add indexes to repeats
            self.inp += [inp + str(i+1) for inp in pdf.inp]
            self.parameters += [parameter + str(i+1) for parameter in pdf.parameters]
    
    def distribution(self, *args):
        if len(args) != self.dim:
            raise TypeError(f"expected {self.dim} arguments, got {len(args)}")
        
        accum = 1
        i = 0
        for pdf in self.pdfs:
            accum *= pdf.distribution(*(args[i:i+pdf.dim]))
            i += pdf.dim
        
        return accum

if __name__ == "__main__":
    

    X = Normal(5, 1)
    Y = Gamma(2, 3)
    #J = JointPDF(X, Y)
    J = X * Y
    J.plot()