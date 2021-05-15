from sorter import Sorter

class SlowSort(Sorter):

    name = "Slow Sort"

    def __init__(self):
        super(SlowSort, self).__init__()

    def sort(self, L):
        return self.slow_sort(L, 0, len(L)-1)
    
    def slow_sort(self, L, i, j):
        if i >= j:
            return L

        m = (i + j)//2
        self.slow_sort(L, i, m)
        self.slow_sort(L, m+1, j)

        if L[j] < L[m]:
            L[j], L[m] = L[m], L[j]
            self._log(L)

        self.slow_sort(L, i, j-1)
        return L


if __name__ == "__main__":
    S = SlowSort()
    S.test(n=50)