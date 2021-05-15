#What does the 'is' keyword do?
#It tells you if two variables share the same pointer

A = [1, 2, 3, 4]

B = A
print "B = A"
print "A is B:\t\t",A is B    #will be True

print

C = list(A)
print "C = list(A)"
print "A is C:\t\t",A is C    #will be False

#It gets funky with strings
#With lists, if I were to change A, it would also change B, but it would not change C

print
print

#Let's do the same thing with strings
a = "1234"

b = a
print "b = a"
print "a is b:\t\t",a is b    #will be True

print

b = "12345"
print 'b = "12345"'
print "a is b:\t\t",a is b    #will be False

#Initally python keeps the values of the variables a and b in the same location. But then when you try and change b, since it would be annoying if making strings equal coupled them by default, Python creates a new location in memory
#A cool insight into how Python's memory works
#The same applies for integers and floats

#the is operator is synonomous to id(a) == id(b)

