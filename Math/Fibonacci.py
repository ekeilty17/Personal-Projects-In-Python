def fibo_cheating(n):
    phi = 1.61803398875
    root_5 = 2.2360679775
    return int(round((phi**n)/root_5,0))

def fibo_rec(n):
    if n < 0:
        return 0
    if n < 1:
        return 1
    return fibo_rec(n-1) + fibo_rec(n-2)

def fibo_iter(n):
    if n < 0:
        return 0
    a = [0,1]
    for i in range(0,n):
        total = a[0] + a[1]
        a[0] = a[1]
        a[1] = total
    return a[1]

#These functions sum up the previous m numbers to get the next number in the sequence
#fibo only sums up the previous 2 numbers
def fibo_gen_rec(n,m):
    if m <= 0:
        return -1
    if n < 0:
        return 0
    if n < m:
        return 1
    accum = 0
    for i in range(0,m):
        accum += fibo_gen_rec(n-i-1,m)
    return accum

def fibo_gen_iter(n,m):
    if m <= 0:
        return -1
    if n < 0:
        return 0
    a = []
    for i in range(0,m):
        a += [1]
    
    if n < m:
        return a[n]

    for i in range(0,n-(m-1)):
        total = 0
        for j in range(0,m):
            total += a[j]
        for j in range(1,m):
            a[j-1] = a[j]
        a[m-1] = total
    return a[m-1]

print(fibo_cheating(5))
print(fibo_rec(5))
print(fibo_iter(5))
print(fibo_gen_rec(5,4))
print(fibo_gen_iter(9,4))
