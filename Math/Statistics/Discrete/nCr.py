import operator as op
from functools import reduce
from scipy.special import binom

def nCr(n, r):
    r = min(r, n-r)
    numer = reduce(op.mul, range(n, n-r, -1), 1)
    denom = reduce(op.mul, range(1, r+1), 1)
    return numer / denom

def multinomial_coef(*args):
    if len(args) == 1:
        return 1
    return binom(sum(args), args[-1]) * multinomial_coef(args[:-1])