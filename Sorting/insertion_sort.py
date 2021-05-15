from sorter import Sorter

class InsertionSort(Sorter):

    name = "Insertion Sort"

    def __init__(self):
        super(InsertionSort, self).__init__()

    def sort(self, L):
        for i in range(1,len(L)):
            j = i
            while (j>0) and (L[j] < L[j-1]):
                L[j-1], L[j] = L[j], L[j-1]
                j -= 1
                self._log(L)
        return L

if __name__ == "__main__":
    S = InsertionSort()
    S.test(n=20)