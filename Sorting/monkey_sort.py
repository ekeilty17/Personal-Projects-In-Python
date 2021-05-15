from sorter import Sorter
from random import shuffle

class MonkeySort(Sorter):

    name = "Monkey Sort"

    def __init__(self):
        super(MonkeySort, self).__init__()

    def sort(self, L):
        
        while not self.is_sorted(L):
            shuffle(L)
            self._log(L)
        
        return L


if __name__ == "__main__":
    S = MonkeySort()
    S.test(n=5)