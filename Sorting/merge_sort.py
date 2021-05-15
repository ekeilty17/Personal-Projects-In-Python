from sorter import Sorter

class MergeSort(Sorter):

    name = "Merge Sort"

    def __init__(self):
        super(MergeSort, self).__init__()

    def sort(self, L):
        return self.merge_sort(L, 0, len(L)-1)

    def merge(self, A, left, middle, right):
        self._log(A)    # replaced variable named L with A, because L is used for something else in this alg

        # initializing left and right sublists
        L = list(A[left:middle+1])
        R = list(A[middle+1:right+1])

        # sort sublists using 2 pointers l and r
        l = 0
        r = 0
        p = left
        while (l < len(L) and r < len(R)):
            if L[l] <= R[r]:
                A[p] = L[l]
                l += 1
            else:
                A[p] = R[r]
                r += 1
            p += 1
            self._log(A)

        # Either r or l will each the end of its list first
        # Therefore, the rest of the other list needs to be appended to the end of A
        while l < len(L):
            A[p] = L[l]
            l += 1
            p += 1
            self._log(A)
        while r < len(R):
            A[p] = R[r]
            r += 1
            p += 1
            self._log(A)

    def merge_sort(self, A, left, right):
        if left >= right:
            return True
        middle = (left + right)//2

        self.merge_sort(A, left, middle)
        self.merge_sort(A, middle+1, right)

        self.merge(A, left, middle, right)
        return A

if __name__ == "__main__":
    S = MergeSort()
    S.test(n=50)