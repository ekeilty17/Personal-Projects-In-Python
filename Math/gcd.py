def gcd(a, b):
    #accounting for this annoying case
    if b > a:
        a, b = b, a

    #gcd(a,b) = gcd(b,a%b) --> Euclid's Algorithm
    while b != 0:
        a, b = b, a%b
    return a