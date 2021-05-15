from sorter import Sorter

class RadixSort(Sorter):

    name = "Radix Sort"

    def __init__(self, base=10):
        super(RadixSort, self).__init__(interval=750)
        self.base = base

    def sort(self, L):
        maxval = max(L)

        k = 0
        self._log(L)
        while self.base ** k <= maxval:
            L = self.buckets_to_list(self.list_to_buckets(L, self.base, k))
            k += 1
            self._log(L)

        return L

    @staticmethod
    def list_to_buckets(array, base, iteration):
        buckets = [[] for _ in range(base)]
        for number in array:
            digit = (number // (base ** iteration)) % base
            buckets[digit].append(number)
        return buckets

    @staticmethod
    def buckets_to_list(buckets):
        numbers = []
        for bucket in buckets:
            for number in bucket:
                numbers.append(number)
        return numbers

if __name__ == "__main__":
    S = RadixSort(base=2)
    S.test(n=50)