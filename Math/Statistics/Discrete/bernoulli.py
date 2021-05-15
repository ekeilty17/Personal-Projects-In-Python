from binomial import Binomial

class Bernoulli(Binomial):

    name = "Bernoulli"
    short = "Bern"
    inp = ["x"]
    parameters = ["p"]

    def __init__(self, p):
        super(Bernoulli, self).__init__(1, p)

if __name__ == "__main__":
    Bern = Bernoulli(0.3)
    Bern.plot()