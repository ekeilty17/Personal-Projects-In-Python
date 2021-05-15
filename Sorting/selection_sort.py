from sorter import Sorter

class SelectionSort(Sorter):

    name = "Selection Sort"

    def __init__(self):
        super(SelectionSort, self).__init__()

    def sort(self, L):
        min_idx = -1
        for i in range(len(L)):
            min_idx = i
            for j in range(i, len(L)):
                if L[min_idx] > L[j]:
                    min_idx = j
            
            L[i], L[min_idx] = L[min_idx], L[i]
            self._log(L)
        
        return L


if __name__ == "__main__":
    S = SelectionSort()
    S.test(n=100)