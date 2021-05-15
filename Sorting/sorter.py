import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as ani

import time
    

class Sorter(object):

    name = "Sorter"

    def __init__(self, interval=1):
        self.iterations = []
        self.interval = interval
    
    def __call__(self, L, reverse=False):
        # error checking
        if not hasattr(L, '__iter__'):
            raise ValueError("First argument must be iterable.")
        L = list(L)
        self.iterations = []
        self._log(L)

        if L == []:
            return L

        L = self.sort(L, reverse=reverse)
        return list(reversed(L)) if reverse else L
    
    def _log(self, L):
        self.iterations.append(list(L))

    def is_sorted(self, L):
        for i in range(1, len(L)):
            if L[i-1] > L[i]:
                return False
        return True

    def sort(self, L):
        raise NotImplementedError("Not Implemented.")

    def animate(self):
        def aniFunc(t=int):
            if t >= len(self.iterations):
                raise StopIteration
            plt.clf()
            plt.grid()
            
            Y = self.iterations[t]
            X = list(range(1, len(Y)+1))
            plt.bar(X, Y, zorder=100)

            plt.title(f"{self.name.title()}")
            plt.xlabel("position")
            plt.ylabel("value")
    
        fig = plt.figure()
        animator = ani.FuncAnimation(fig, aniFunc, interval=self.interval, repeat=False)
        plt.show()
    
    def test(self, n=50, animate=True):
        L_original = np.arange(1, n+1)
        
        L_shuffle = L_original.copy()
        np.random.shuffle(L_shuffle)

        L_alg = self.sort(L_shuffle)

        print(L_shuffle)
        print(L_alg)
        assert list(L_original) == list(L_alg), "Algorithm did not sort correctly"

        self.animate()