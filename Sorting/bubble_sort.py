from sorter import Sorter

class BubbleSort(Sorter):

    name = "Bubble Sort"

    def __init__(self):
        super(BubbleSort, self).__init__()
    
    def sort(self, L):
        for i in range(len(L)-1):
            for j in range(1, len(L)-i):
                if L[j-1] > L[j]:
                    L[j-1], L[j] = L[j], L[j-1]
                    self._log(L)
        return L

class BubbleSort2(Sorter):

    """ This is a weirder way to doing bubble sort using a while loop """

    name = "Bubble Sort using While Loop"

    def __init__(self):
        super(BubbleSort2, self).__init__()
    
    def sort(self, L):
        swapped = True
        while swapped:
            swapped = False
            for i in range(1, len(L)):
                if L[i-1] > L[i]:
                    L[i-1], L[i] = L[i], L[i-1]
                    swapped = True
                    self._log(L)
        return L

if __name__ == "__main__":
    S = BubbleSort()
    #S = BubbleSort2()
    S.test(n=20)