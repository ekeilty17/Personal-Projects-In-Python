import multiprocessing as mp
import time
  
start = time.time()

#define an output queue
output = mp.Queue()

#define some function
def factorial(n):
    if n == 0:
        return 1
    accum = 1
    for i in xrange(1,n+1):
        accum *= i
    return accum

def sumDigits(n):
    accum = 0
    while n != 0:
        accum += n%10
        n /= 10
    return accum

def fact_digits(n,output):
    output.put(sumDigits(factorial(n)))

#set up a list of processes that we will run
processes = [mp.Process(target=fact_digits, args=(x,output)) for x in [1234,12345]]

#run process
for p in processes:
    p.start()

#Exit the completed process
for p in processes:
    p.join()

#Get process results from output queue
results = [output.get() for p in processes]
end = time.time()

print results
print "Time =",end-start

print
print

start = time.time()
print sumDigits(factorial(1234))
print sumDigits(factorial(12345))
end = time.time()
print "Time =", end-start
