"""
Some of these are useful and some of these I made just for the intelectual exercise.
"""

A = [[1,2,3,0], [4,5,6,0], [7,8,9,0]]
print A
print

# Copy a Matrix
A_copy = [x[:] for x in A]

# Flatten a Matrix
print [num for elem in A for num in elem]
print

# Print a Matrix
print ' ' + ' '.join([str(num) for elem in A for num in elem + ['\n']])
print

# Print largest possible number for a given bit/byte size
print '\n'.join("%i Byte = %i Bit = largest number: %i" % (j, j*8, 256**j-1) for j in (1 << i for i in xrange(8)))
print

# Generate a list of prime numbers between 1 and n
n = 100
print [x for x in range(2,n)
        if not [y for y in range(2, int(x**0.5)+1)
            if x % y == 0] ]
print

# Function that returns all subsets of a an input list
f = lambda l: reduce(lambda z, x: z + [y + [x] for y in z], l, [[]])
print f([10, 1, 1, 1, 10, -2]) # treat repeated entries as independent
print
print f(set([10, 1, 1, 1, 10, -2])) # treat repeated entries as the same instance
print

# Print list of all users
#print '\n'.join(line.split(":",1)[0] for line in open("/etc/passwd"))
