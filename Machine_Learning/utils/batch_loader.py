import numpy as np

class BatchLoader(object):

    def __init__(self, data, batch_size=None, randomize=True, drop_last=False, seed=None):
        
        # error checking
        if len(data) > 1:
            for i in range(len(data)-1):
                if data[i].shape[0] != data[i+1].shape[0]:
                    raise ValueError("All inputs must have the same number of elements")
        
        self.data = data if type(data) == tuple else (data, )
        self.N = data[0].shape[0]
        self.batch_size = batch_size if batch_size != None else self.N
        self.drop_last = drop_last

        # shuffling data
        if randomize:
            indices = np.arange(self.N)
            np.random.seed(seed)
            np.random.shuffle(indices)
            self.data = tuple([d[indices] for d in self.data])
        
        self.index = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        
        # stop condition
        if self.index >= self.N:
            self.index = 0          # resetting index for next iteration
            raise StopIteration

        # iterating
        self.index += self.batch_size
        
        if self.index > self.N:
            if self.drop_last:
                self.index = 0      # resetting index for next iteration
                raise StopIteration
            else:
                #return self.index - self.batch_size, "end"
                return tuple([ d[self.index - self.batch_size: ] for d in self.data ])
        else:
            #return self.index - self.batch_size, self.index
            return tuple([ d[self.index - self.batch_size: self.index] for d in self.data ])

"""
def BatchLoader():
    
    for i in range(batch_size, N, batch_size):
        yield tuple([ d[i - batch_size: i] for d in data ])
    if not drop_last or N - i == batch_size:
        yield tuple([ d[i: ] for d in data ])

def test_gen(batch_size, N, drop_last=False):
    for i in range(batch_size, N, batch_size):
        yield (i - batch_size, i)
    if not drop_last or N - i == batch_size:
        yield (i, "end")
"""

if __name__ == "__main__":
    import sys
    sys.path.append("..")
    from MNIST.load_MNIST import get_testing_data, plot_image
    
    images, labels = get_testing_data("../MNIST/data")
    print("Full Dataset:", images.shape, '\t', labels.shape)
    
    #for t in test_gen(550, 10000, True):
    #    print(t)

    BL = BatchLoader(data=(images, labels), batch_size=550)
    print("iteration 1")
    for i, (images, labels) in enumerate(BL):
        print(f"batch {i+1}:", images.shape, '\t', labels.shape)
    
    BL.batch_size = 430
    print("iteration 2")
    for i, (images, labels) in enumerate(BL):
        print(f"batch {i+1}:", images.shape, '\t', labels.shape)