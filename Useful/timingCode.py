import time

start = time.time()

#code
for i in range(0,1000000):
    continue

end = time.time()

print
print "Total Time =",end-start
print "Every iteration of a for loop takes",(end-start)/1000000.0,"seconds"
print
