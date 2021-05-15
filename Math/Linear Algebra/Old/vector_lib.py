import math

#Defining a vector
class Vector():

    def __init__(self, L):
        error = False
        if type(L) != list:
            raise TypeError("Vector was not set. Input was not a list.")
            error = True
        for x in L:
            if type(x) != int and type(x) != float:
                raise TypeError("Vector was not set. Entries were not numbers.")
                error = True
                break
        if not error:
            #for convience I will make them row vectors instead of column vectors
            self.store = L
        else:
            self.store = []
    
    def get(self):
        out = "["
        for x in self.store:
            out += str(x) + " "
        return out[:-1] + "]"

    def set(self, L):
        if type(L) == list and type(L[0]) == int:
            #for convience I will make them row vectors instead of column vectors
            self.store = L
    
    def copy(self):
        if not isinstance(self, Vector):
            raise TypeError("Input was not a vector.")
            return None
        return Vector(list(self.store))
    
    def dim(self):
        return len(self.store)
    
    def scale(self, k):
        for i in range(len(self.store)):
            self.store[i] = self.store[i]*k
        return self

    def magnitude(self):
        accum = 0
        for x in self.store:
            accum += x*x
        return accum**(0.5)

    def normalize(self):
        self.scale(1/float(self.magnitude()))
        return self

#Defining operations between vectors
def add(u,v):
    #error checks
    if not isinstance(u, Vector) or not isinstance(v, Vector):
        raise TypeError("Arguements are not vectors.")
        return None
    if u.dim() != v.dim():
        raise TypeError("Dimensions of arguements do not match.")
        return None
    #function
    out = []
    for i in range(len(u.store)):
        out += [u.store[i] + v.store[i]]
    return Vector(out)

def subtract(u,v):
    return add(u,v.copy().scale(-1))

def dot(u, v):
    #error checks
    if not isinstance(u, Vector) or not isinstance(v, Vector):
        raise TypeError("Arguements are not vectors.")
        return -1
    if u.dim() != v.dim():
        raise TypeError("Dimensions of arguements do not match.")
        return -1
    #function
    accum = 0
    for i in range(u.dim()):
        accum += u.store[i] * v.store[i]
    return accum

def cross(u, v):
    #error checks
    if not isinstance(u, Vector) or not isinstance(v, Vector):
        raise TypeError("Arguements are not vectors.")
        return None
    if not (u.dim() == v.dim() == 3):
        raise TypeError("Arguments do no lie in R^3.")
        return None
    #function
    return Vector(  [   (u.store[1]*v.store[2]-u.store[2]*v.store[1]), 
                        (u.store[2]*v.store[0]-u.store[0]*v.store[2]), 
                        (u.store[0]*v.store[1]-u.store[1]*v.store[0])
                     ])

def angle(u, v):
    return math.acos( dot(u,v) / (u.magnitude() * v.magnitude()) )

def proj(u, v):
    return v.copy().scale( dot(v,u) / dot(v,v) )


#Testing
"""
v = Vector([1, -2, 0])
u = Vector([1, 1, 0])
print "u",u.get()
print "v",v.get()
print "u+v",add(u,v).get()
print "u-v",subtract(u,v).get()
print "dot(u,v)",dot(u,v)
print "cross(u,v)",cross(u,v).get()
print "angle",angle(u,v)
print "proj(u,v)",proj(u,v).get(),proj(u,v).magnitude()
print "u",u.get()
print "v",v.get()
"""
