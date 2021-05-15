from pdf import PDF

class Uniform(PDF):

    name = "Uniform"
    short = "Uni"
    inp = ["x"]
    parameters = ["a", "b"]

    def __init__(self, a, b):
        self.a = a
        self.b = b
        super(Uniform, self).__init__(domain=[(a, b)])
    
    def distribution(self, x=None):
        return 1.0 / (self.b - self.a)

if __name__ == "__main__":
    Uni = Uniform(4, 10)
    Uni.plot()