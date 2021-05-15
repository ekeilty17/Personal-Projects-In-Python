from makeFrame import *

def radix_sort(array, base=10):
    def list_to_buckets(array, base, iteration):
        buckets = [[] for _ in range(base)]
        for number in array:
            digit = (number // (base ** iteration)) % base
            buckets[digit].append(number)
        return buckets

    def buckets_to_list(buckets):
        numbers = []
        for bucket in buckets:
            for number in bucket:
                numbers.append(number)
        return numbers

    maxval = max(array)

    it = 0
    makeFrame(array)
    while base ** it <= maxval:
        array = buckets_to_list(list_to_buckets(array, base, it))
        it += 1
        makeFrame(array)

    return array
