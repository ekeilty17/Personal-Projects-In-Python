class Probability_Function(object):

    """ Abstract class for a general probability distribution """

    def __init__(self):
        # checking if it is a valid probability distribution
        try:
            if not self.is_always_positive():
                raise ValueError("Probability Function is not always positive over the domain")
            if not self.is_normalized():
                raise ValueError("Probability Function does not normalize to 1")
        except NotImplementedError as e:
            raise e

    def __call__(self, *args):
        if len(args) != self.dim:
            raise TypeError(f"expected {self.dim} arguments, got {len(args)}")
        return self.distribution(args)

    def set_distribution(self, f):
        self.distribution = f
        self.inp = list(f.__code__.co_varnames)

    def is_always_positive(self):
        raise NotImplementedError("Method 'is_always_positive' not implemented")

    def is_normalized(self):
        raise NotImplementedError("Method 'is_normalized' not implemented")

    def distribution(self, *args):
        raise NotImplementedError("Method 'distribution' not implemented")