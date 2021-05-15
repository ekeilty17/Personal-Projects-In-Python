from sorter import Sorter

class QuickSort(Sorter):

    name = "Quick Sort"

    def __init__(self):
        super(QuickSort, self).__init__()

    def sort(self, L):
        self._log(L)
        return self.quick_sort(L, 0, len(L)-1)

    def partition(self, L, lo, hi):
        # choose pivot
        pivot = L[hi]

        # partition list by values < and > pivot
        i = lo
        for j in range(lo, hi):     # don't do index hi, because that's where the pivot is
            if L[j] < pivot:
                L[i], L[j] = L[j], L[i]
                self._log(L)
                i += 1
        
        L[i], L[hi] = L[hi], L[i]
        self._log(L)
        return i    

    def quick_sort(self, L, lo, hi):
        if lo < hi:
            p = self.partition(L, lo, hi)
            
            self.quick_sort(L, lo, p-1)
            self._log(L)
            
            self.quick_sort(L, p+1, hi)
            self._log(L)
        
        return L


if __name__ == "__main__":
    S = QuickSort()
    S.test(n=50)