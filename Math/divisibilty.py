# This is not intended to be efficient computationally,
# These are the algorithms a human would follow
# if they were trying to determine divisibility by hand

def getDigits(n):
    out = []
    while n > 0:
        out = [n%10] + out
        n /= 10
    return out

def isDivisible1(n):
    return True

def isDivisible2(n):
    return int(str(n)[-1])%2 == 0

def isDivisible3(n):
    return sum(getDigits(n))%3 == 0

def isDivisible4(n):
    return int(str(n)[-2:])%4 == 0

def isDivisible5(n):
    return int(str(n)[-1]) == 0 or int(str(n)[-1]) == 5

def isDivisible6(n):
    return isDivisible2(n) and isDivisible3(n)

def isDivisible7(n):
    # Taking an n digit number and turning it
    # into a 3 digit number
    while len(str(n)) > 3:
        D = getDigits(n)
        accum = 0
        neg = 1
        for i in range(len(D)-1, -1, -3):
            if i == 0:
                accum += neg * D[i]
            elif i == 1:
                accum += neg * (10*D[i-1] + D[i])
            else:
                accum += neg * (100*D[i-2] + 10*D[i-1] + D[i])
            neg *= -1
        n = accum

    # Taking a 3 digit number and turning it
    # into a 2 digit number
    D = getDigits(accum)
    if len(D) < 3:
        return accum % 7 == 0
    else:
        return (10*D[0] + D[1] - 2*D[2])%7 == 0

def isDivisible8(n):
    return int(str(n)[-3:])%4 == 0

def isDivisible9(n):
    return sum(getDigits(n))%9 == 0

def isDivisible10(n):
    return int(str(n)[-1]) == 0

def isDivisible11(n):
    D = getDigits(n)
    accum = 0
    neg = 1
    for i in range(len(D)-1, -1, -1):
        accum += neg * D[i]
        neg *= -1
    return accum%11 == 0

def isDivisible12(n):
    return isDivisible3(n) and isDivisible4(n)
