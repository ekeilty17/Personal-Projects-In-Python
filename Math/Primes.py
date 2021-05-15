def nthPrime(n):
    if n < 1:
        return 1

    counter = 0
    candidate = 1
    while counter < n:
        candidate += 1
        if isPrime(candidate):
            counter += 1
    return candidate


#Sieve of Eratosthenes
def Sieve(n):
    #Error Check
    if type(n) != int and type(n) != long:
        raise TypeError("must be integer")
    if n < 2:
        raise ValueError("must be greater than one")
    sieve = [True] * (n+1)
    prime_list = []
    for i in xrange(2,n+1):
        if sieve[i]:
            prime_list += [i]
            #this for loop is analogous to crossing out
            #all multiples of a number in a given range
            for j in xrange(i, n+1, i):
                sieve[j] = False
    return prime_list

    #a cute one liner way of doing it
    #I don't like it though, it's not easy to understand
    """
    return [x for x in range(2,n) 
            if not [y for y in range(2, int(x**0.5)+1)
                if x % y == 0] ]
    """

#Optimized Sieve of Eratosthenes
#1) instead of crossing out all the even numbers, we don't even consider them (except for 2)
#2) we start crossing out at p^2 rather than p
#       take 4 for example, we don't have to check if 8 or 12 are cross out
#       because 4 = 4*2 and 12 = 4*3, our crossing out from 2 and 3 already got rid of them
#3) as a consiquence of 2) we can stop checking as soon as p^2 > n rahter than every number up to n
def Sieve2(n):
    #Error Check
    if type(n) != int and type(n) != long:
        raise TypeError("must be integer")
    if n < 2:
        raise ValueError("must be greater than one")
    m = (n-1) // 2 #list only needs to be half as long bc we dont care about even numbers
    sieve = [True] * m
    i = 0
    p = 3
    prime_list = [2] #add 2 as the exception
    #this while loop is equivilent to the while loop in the first Sieve function
    #it just looks different because the parameters are different
    while p*p < n:
        #if the number hasnt been crossed out we add it
        if sieve[i]:
            prime_list += [p]
            #j is the multiples of p
            j = 2*i*i + 6*i + 3 #j = (p^2-3)/2 where p = 2i+3 (see below comments)
            #this is equivilent to the for loop in the previous Sieve fuction
            while j < m:
                sieve[j] = False
                j += 2*i + 3 #p = 2i+3
        i += 1
        p += 2
        #this is where the p = 2i+3
        #p starts at 3 and is upped by 3, where i starts at 0 and is upped by 1
    #this while loop then adds the remaining primes to the prime list
    while i < m:
        if sieve[i]:
            prime_list += [p]
        i += 1
        p += 2
    return prime_list


#This is called Trial Division
def isPrime(n, limit=1000000):
    #Error check
    if type(n) != int and type(n) != long:
        raise TypeError('must be integer')
    if n < 2:
        raise False
    #check if its an even number to eliminate half of the checks in the below while loop
    if n % 2 == 0:
        return n == 2
    #f is some potential factor
    f = 3
    while f*f <= n:
        if limit < f:
            raise OverflowError('limit exceeded')
        if n % f == 0:
            return False
        f += 2
    return True


#This is integer Factorization by Trial Division
def Prime_Factors(n, limit=1000000):
    #Error Check
    if type(n) != int and type(n) != long:
        raise TypeError('must be integer')
    if n < 2:
        return []
    factors = []
    #as always, take care of the 2s first bc they are easy
    while n % 2 == 0:
        factors += [2]
        n /= 2
    #if n was purely a power of 2, then the function ends here
    if n == 1:
        return factors
    #since we got rid of the 2's potential factors, f, can start at 3
    #other than that, this loop is pretty self explainitory
    f = 3
    while f*f <= n:
        if limit < f:
            raise OverflowError('limit exceeded')
        if n % f == 0:
            factors += [f]
            n /= f
        else:
            f += 2
    return factors + [n]

#this takes advantage of Fermat's Little Theorem:
#       if p is prime, then for any int a, a^p = a (mod p)
#       this is equivilent to saying a^(p-1) = 1 (mod p)
#   if we can find an a that fails the test, then p is definately composite. 
#   However, even if we cannot find an int a that fails, p is not necessarily prime
#       composites that pass this test are called "Carmichael numbers"
#       a Carmichael number is an example of a pseudoprime
#       a pseudoprime is a composite number that acts like a prime in a specific circumstance
#       This is why Carmichael numbers are sometimes called "Fermat Pseudoprimes"
def isPrime_Fermat(n):
    #Error Check
    if type(n) != int and type(n) != long:
        raise TypeError('must be integer')
    if n < 2:
        return False
    #let's just get rid of the evens
    if n % 2 == 0:
        return True
    
    #This is Fermat's Little Theorem
    #It's an algorith to calculate b^e (mod m)
    """
    def exp_mod(b, e, m):
        r = 1
        while e > 0:
            if e % 2 == 1:
                r = (r*b) % m
            e /= 2
            b = (b*b) % m
        return r
    """
    #however, python already has an in-built exp_mod function
    for i in range(2,n-1):        
        if pow(i,n-1,n) != 1:
            return False
    return True


#Miller came up with a strong version of this test
#       assuming n is a prime it must be odd (2 is just an exception) therefore n-1 = d*2^s (d is odd by assumption)
#       again, assuming n is prime then either a^d = 1 (mod n) or a^(d*2^r) = -1 (mod n) where 0 <= r <= s-1
#           You'll just have to take my word for it, look it up if you are curious
#    Some base a passes the test if one of the two statements is true 
#       if base a passes the test, we say it is a witness for the compositeness of n
#       if base a does not the test, we say a is a "strong liar" and n is a "strong pseudoprime"
#   There great thing about Millar's Test is that
#   if we assume the Riemann hypothesis any number n has a witness less than 70(ln n)^2
#   So this is a full proof test (given the Riemann hypothesis), rather than Fermat's probabilistic test
def isPrime_Miller(n):
    #Error Checking
    if type(n) != int and type(n) != long:
        raise TypeError('must be integer')
    if n < 2:
        return False
    #this is so we can eliminate easy ones
    #obviously the advtantage of this test comes with large numbers
    prime_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 
                  43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    
    #This is Miller's test
    #spsp means "Strong Pseudoprime"
    def is_spsp(n,a):
        # assuming n is prime, then n-1 = d*2^s
        d = n-1
        s = 0
        while d%2 == 0:
            d /= 2
            s += 1
        t = pow(a,d,n) #t = a^d (mod n)
        #this is the first statement, a^d = 1 (mod n)
        if t == 1:
            return True
        #we check for all r = [1, s-1]
        #r=0 was checked in the above if statement
        while s > 0:
            if t == n-1: #-1 = n-1 (mod n)
                return True
            t = (t*t) % n #this is equivilent to t = a^(d*2^r) (mod n)
            s -= 1
        return False
    
    #just some logic to finish things off
    if n in prime_list: 
        return True
    #the more primes we have in the initial list, the more sure we can be that the number is prime
    for p in prime_list:
        if not is_spsp(n,p):
            return False
    return True


#Sun Zi's Chinese Remainder Theorem:
#       if r and s are relatively prime ( gcd(r,s) = 1 )
#       then there extists an n such that n = a (mod r) = b (mod s)
#   Basically you can use this fact to find any number just by looking at
#   its remainders when divided by prime numbers
#The Quadratic Congreuent random number generator
#       x^2+c (mod n) (where c != 0, -2) generates a pseudo-random x
#       by the Chinese Remainder Theorem
#           if n = p*q
#           then x (mod n) corresponds uniquely to { x (mod p), x (mod q) }
#       therefore x_k+1 = [x_k (mod p)]^2 + c (mod p)
#       and       x_k+1 = [x_k (mod q)]^2 + c (mod q)
#       Therefore we can identify the value of p when
#           x_k+1 (mod p) = x_k (mod p)  (also called being congruent modulo p)
#           this is the same as gcd(|x_k - x_k+1|,n) = p, p = [1,n]
#   It's possible that the p, q, and c chosen cause 
#   the random number generator to reach a cycle before a factor is found
#Robert Floyd's tortoise-and-hare cycle-detection method
#       we set x_k running twice with two different initial numbers, call them t and h
#       h is incremented twice as fast as t (the hare runs twice as fast as the tortoise)
#       if t = h (mod n) before a factor is found, then thats a cycle
#   If this happens either we use a different factorization method or we pick a different c
#
#The actual algorithm itself
#       f(x) = x^2 + c (mod n)
#       compute f(2), f(f(2)), f(f(f(2))), etc
#           by the Chinese Remainder Theorem each term in the sequence 
#           relates uniquely to { x_k (mod p), x_k (mod q) }
#       therefore gcd(|x - f(x)|,n) = p, p must be a factor of n since n = p*q by assumption
#       if gcd(|x - f(x)|,n) = 1, then try another iteration
#       if we enter into a cycle, then try another c value
#
#If you are wondering how using random numbers can be an efficient way to factor large numbers
#look up the birthday paradox, it's unituitive for the same reason as the birthday paradox
#The number of possible combinations is very large and it is very easy to guess right
#This method was called "Monte Carlo Factorization" by Pollard because of the use of random numbers
#
#Pollard's Rho Method
def rho_factors(n, limit=1000000):
    #Error Checking
    if type(n) != int and type(n) != long:
        raise TypeError('must be integer')
    
    #finding the Greatest Common Divisor
    #This is the Euclidean Algorithm
    #   It takes adtantage of 3 facts
    #       1) any number can be written in this form a = qb + r
    #       2) gcd(a,b) = gcd(b,r)
    #       3) gcd(n,0) = n
    #   once r = 0 we have found the gcd of a and b
    def gcd(a,b):
        while b:
            temp = a
            a = b
            b = temp%b
        return abs(a)
    
    #this function just finds 1 prime factor
    def rho_factor(n, c, limit):
        f = lambda(x): (x*x+c) % n #creating a prototype of x^2+c (mod n)
        t = 2 #tortoise
        h = 2 #hair
        d = 1
        #here's the clever part of the algorithm, Floyd's method for detecting cycles
        #works in tandum with finding p
        #since t and h both start at 2, f(f(h)) is the same as f(f(t)), 
        #and f(x) = x in the next iteration
        #this means gcd(t-h,n) is the same as gcd(x-f(x),n)
        while d == 1:
            if limit == 0:
                raise OverflowError('limit exceeded')
            t = f(t)        #tortoise goes 1 step
            h = f(f(h))     #while the hare goes 2 steps
            d = gcd(t-h,n)
        if d == n: #the factor gave no new information, so try another c value
            return rho_factor(n, c+1, limit)
        if isPrime_Miller(d): #if the factor is a prime, then yay we did it
            return d
        return rho_factor(d, c+1, limit)
    
    if -1 <= n <= 1: #account for degenerate cases
        return [n]
    if n < -1: #cute way to account for negatives
        return [-1] + rho_factors(-n, limit)
    prime_factors = []
    while n % 2 == 0: #get rid of the other degenerate case
        n = n // 2
        prime_factors += [2]
    if n == 1:
        return prime_factors
    while not isPrime_Miller(n):
        f = rho_factor(n, 1, limit)
        n = n / f
        prime_factors += [f]
    return sorted(prime_factors + [n])
