def factors(n):
    if n == 0:
        return []
    if n < 0:
        n *= -1
    if n == 1:
        return [1]
    f = [1,n]
    for i in range(2,n//2+1):
        if n % i == 0:
            f += [i]
    return sorted(f)

def num_factors(n):
    f = 1
    counter = 0
    while n % 2 == 0:
        counter += 1
        n = n/2
    f *= (counter + 1)
    p = 3
    while n != 1:
        counter = 0
        while n % p == 0:
            counter += 1
            n /= p
        f *= (counter + 1)
        p += 2
    return f
