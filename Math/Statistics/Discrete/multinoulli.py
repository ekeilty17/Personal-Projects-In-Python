from multinomial import Multinomial

class Multinoulli(Multinomial):

    name = "Multinoulli"

    def __init__(self, *P):
        super(Multinoulli, self).__init__(1, *P)

if __name__ == "__main__":
    Mu = Multinoulli(0.3, 0.1)
    Mu.plot()