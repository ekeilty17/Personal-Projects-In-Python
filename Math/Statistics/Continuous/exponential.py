from pdf import PDF
import numpy as np

class Exponential(PDF):

    name = "Exponential"
    short = "Exp"
    inp = ["x"]
    parameters = ["b"]

    def __init__(self, b):
        self.b = b
        super(Exponential, self).__init__(domain=[(0, 20)])
    
    def distribution(self, x):
        return (1.0/self.b) * np.exp(-x/self.b)

if __name__ == "__main__":
    Exp = Exponential(-3)
    Exp.plot()