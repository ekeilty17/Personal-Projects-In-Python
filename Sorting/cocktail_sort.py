from sorter import Sorter

class CocktailSort(Sorter):

    name = "Cocktail Sort"

    def __init__(self):
        super(CocktailSort, self).__init__()
    
    def sort(self, L):
        swapped = True
        while swapped:
            swapped = False
            for i in range(1, len(L)):
                if L[i-1] > L[i]:
                    L[i-1], L[i] = L[i], L[i-1]
                    swapped = True
                    self._log(L)
            if not swapped:
                break
            swapped = False
            for i in reversed(range(1, len(L))):
                if L[i-1] > L[i]:
                    L[i-1], L[i] = L[i], L[i-1]
                    swapped = True
                    self._log(L)
        return L

if __name__ == "__main__":
    S = CocktailSort()
    S.test(n=20)