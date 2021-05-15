from sorter import Sorter

class HeapSort(Sorter):

    name = "Heap Sort"

    def __init__(self):
        super(HeapSort, self).__init__()

    def sort(self, L):
        # create the heap
        self.heapify(L)

        # then iterative extract the max and re-heapify
        for i in range(len(L)):
            L[0], L[-(i+1)] = L[-(i+1)], L[0]
            self._log(L)

            end = len(L)-(i+1)
            self.bubble_down(L, 0, end)
       
        return L

    @staticmethod
    def parent(n):
        if n < 1:
            return -1
        if n%2 == 0:
            return (n-2)//2
        else:
            return (n-1)//2

    def bubble_up(self, L, c):
        if self.parent(c) == -1:
            return True
        
        p = self.parent(c)
        if L[p] < L[c]:
            L[c], L[p] = L[p], L[c]
            self._log(L)
            self.bubble_up(L, p)
        return True

    def bubble_down(self, L, p, end):
        if p < 0:
            return False
        
        min_idx = p
        if (2*p+1) < end:
            if L[min_idx] < L[2*p+1]:
                min_idx = 2*p+1
        if (2*p+2) < end:
            if L[min_idx] < L[2*p+2]:
                min_idx = 2*p+2

        if min_idx != p:
            L[p], L[min_idx] = L[min_idx], L[p]
            self._log(L)
            self.bubble_down(L, min_idx, end)
        return True

    def heapify(self, L):
        for i in range(1,len(L)):
            self.bubble_up(L, i)



if __name__ == "__main__":
    S = HeapSort()
    S.test(n=100)