def binary_iter(n):
    B = 0
    t = 1
    while n != 0:
        B = B + t*(n%2)
        t *= 10
        n //= 2
    return B

def binary_rec(n):
    if n == 0:
        return 0
    return n%2 + 10*binary_rec(n//2)

print binary_iter(57)
print
print binary_rec(57)
