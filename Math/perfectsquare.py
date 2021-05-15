import math
from decimal import *

#We can start using properties of sqrts to eliminate some
#For example: sqrts always end in [0, 1, 4, 5, 6, 9]
#and the digital sum of a sqrt is always [1, 4, 7, 9]
def getDigits(n):
    out = []
    while n != 0:
        out = [n%10] + out
        n /= 10
    return out

def DigitalSum(n):
    while n >= 10:
        n = sum(getDigits(n))
    return n

#If it returns False, the number is def not a perfect square
#If it returns True, it might be
def isPerfectSquare_checks(n):
    #easy checks
    if n%10 not in [0, 1, 4, 5, 6, 9]:
        return False
    if DigitalSum(n) not in [1, 4, 7, 9]:
        return False
    return True

#This is accurate, but has a linear running time. but takes way to long even with the approximation of x
def isPerfectSquare_brute(n):
    if not isPerfectSquare_checks(n):
        return False
    x = 10**int(math.log10(n)/2.0)
    while x*x < n:
        x += 1
    return x*x == n

print isPerfectSquare_brute(100)
print isPerfectSquare_brute(125)
print isPerfectSquare_brute(1234*1234)
print isPerfectSquare_brute(1000*1000)
print
print

#This is very efficient with constant running time, 
#but becomes innaccurate for large integers
#only works for integers less than about 10^14
def isPerfectSquare_comp(n):
    if not isPerfectSquare_checks(n):
        return False
    #if math.sqrt(n) == int(math.sqrt(n)):      #This is just as accuract as the below
    if n**0.5 == int(n**0.5):
        return True
    return False

for i in range(0,20):
    print "10^",i,'\t',isPerfectSquare_comp(10**i * 10**i), isPerfectSquare_comp(10**i * 10**i + 1)
print
print


#This is the most accurate sqrt function
#This should be used
def isPerfectSquare(n):
    if not isPerfectSquare_checks(n):
        return False
    #You just need a few decimals of accuracy
    getcontext().prec = 10
    if Decimal(n).sqrt() == int(Decimal(n).sqrt()):
        return True
    return False


for i in range(0,100):
    print "10^",i,'\t',isPerfectSquare(10**i * 10**i), isPerfectSquare(10**i * 10**i + 1)
print
print
