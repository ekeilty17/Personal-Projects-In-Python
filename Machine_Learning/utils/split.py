import numpy as np

def train_test_split(data, frac=None, n=None, randomize=True, seed=None):
    
    if frac == None and n == None:
        raise ValueError("Either 'frac' or 'n' needs to be populated")
    if frac != None and n != None:
        raise ValueError("Both 'frac' and 'n' cannot be populated")

    if len(data) > 1:
            for i in range(len(data)-1):
                if data[i].shape[0] != data[i+1].shape[0]:
                    raise ValueError("All inputs must have the same number of elements")
    
    if frac != None and (frac < 0 or frac > 1):
        raise ValueError("Variable 'frac' must be between 0 and 1")

    data = data if type(data) == tuple else (data, )
    N = data[0].shape[0]
    
    if n != None and (n < 0 or n > N):
        raise ValueError("Variable 'n' must be between 0 and the length of 'data'")

    if randomize:
        indices = np.arange(N)
        np.random.seed(seed)
        np.random.shuffle(indices)
        data = tuple([d[indices] for d in data])
    
    n = int(N * frac) if n == None else n
    out = tuple([ d[:(N-n)] for d in data ])
    out += tuple([ d[(N-n):] for d in data ])
    return out