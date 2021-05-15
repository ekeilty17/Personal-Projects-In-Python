from CoordinateSystem import *
from sympy import *
import sys

class Vector(object):
    def __init__(self, E, V=Cartesian()):
        if type(E) != list:
            raise TypeError("First argument must be a list.")
        if not isinstance(V, Curvillinear):
            raise TypeError("Second arguement must be a Curvillinear object.") 
        if len(E) != len(V.H):
            raise TypeError("Number of basis elements, number of jacobeans, and number of variables must be equal.")
        
        # Basis of coordinate system
        self.E = E
        self.V = V

    """"""""""""""""""""""""""""""""""""""""""""""""
    """         Standard Class Stuff             """
    """"""""""""""""""""""""""""""""""""""""""""""""
    def setVector(self, E):
        if type(E) != list:
            raise TypeError("Argument must be a list")
        if len(E) != len(self.E):
            raise TypeError("Dimensions of new coordinates does not match the dimensions of the vector space") 
        if len(E) != len(self.V.H):
            raise TypeError("Number of basis elements, number of jacobeans, and number of variables must be equal")
        self.E = E

    def setCoordinateSystem(self, V):
        if not isinstance(V, Curvillinear):
            raise TypeError("Second arguement must be a Curvillinear object.")
        if len(self.E) != len(V.H):
            raise TypeError("Number of basis elements, number of jacobeans, and number of variables must be equal")
        self.V = V

    def copy(self):
        return Vector(list(self.E), self.V)
    
    # Display nicely
    def __str__(self):
        out = ""
        for i in range(len(self.E)):
            out += "(" + str(self.E[i]) + ")" + self.V[i]
            if i != len(self.E)-1:
                out += " + "
        return out.encode('utf-8')
    
    # so you can do len(v) instead of len(v.E)
    def __len__(self):
        return len(self.E)
    
    def __getitem__(self, index):
        return self.E[index]

    # check Equality
    def __eq__(self, v):
        if not isinstance(v, Vector):
            return False
        if len(self.E) != len(v.E):
            return False
        for i in range(len(self.E)):
            if self.E[i] != v.E[i]:
                return False
        return True
    def __ne__(self, v):
        return not self.__eq__(v)
    
    # ||v||
    def magnitude(self):
        mag = 0
        for i in range(len(self.E)):
            mag = simplify(mag + self.E[i]**2)
        return mag**0.5
    
    # operations on scaler values
    def __mul__(self, k):
        u = self.copy()
        # even tho it's not good form, I assume if you want to multiply two vectors you want to do dot product
        if isinstance(k, Vector):
            return self.dot(k)
        elif type(k) == int or type(k) == float or isinstance(k, Symbol) or isinstance(k, Pow):
            for i in range(len(self.E)):
                u.E[i] *= k
            return u
        elif isinstance(k, Matrix):
            raise TypeError("Left multiplication of vectors is not defined for matrices")
        else:
            raise TypeError("Operation on this type has not been implemented.")
    def __rmul__(self, k):
        return self.__mul__(k)
    
    def __div__(self, k):
        if isinstance(k, Vector):
            raise TypeError("Vector division has not been implemented.")
        elif isinstance(k, Symbol) or isinstance(k, Pow):
            u = self.copy()
            for i in range(len(self.E)):
                u.E[i] /= k
            return u
        elif type(M) == int or type(M) == float:
            return self.__mul__(1.0/k)
        else:
            raise TypeError("Operation on this type has not been implemented.")

    def __mod__(self, k):
        u = self.copy()
        for i in range(len(self.E)):
            u.E[i] %= k
        return u
    
    def __pow__(self, k):
        if int(k) != k:
            raise TypeError("Noninteger exponents have not been implemented.") 
        if k < 0:
            raise TypeError("Exponents below 0 have not been implemented.")
        if k == 0:
            return 1
        u = self.copy()
        for i in range(int(k)):
            u *= self
        return u

    # operations on other vectors
    def __add__(self, v):
        u = self.copy()
        if isinstance(v, Vector):
            if self.V != v.V:
                raise TypeError("Vectors do not occupy the same coordinate system.")
            for i in range(len(self.E)):
                u.E[i] += v.E[i]
            return u
        # even tho it's not good form, I am assuming if you add a scalar to a vector, you want to add it to every element
        elif type(v) == int or type(v) == float or isinstance(v, Symbol) or isinstance(v, Pow):
            for i in range(len(self.E)):
                u.E[i] += v
            return u
        else:
            raise TypeError("Operation on this type has not been implemented.")
    def __sub__(self, v):
        return self + v * (-1)
    
    # v-hat = v / ||v||
    def normalize(self):
        return self / self.magnitude()
    
    # v*u = ||v|| ||u|| cos(theta)
    def angle(self, v):
        return acos( self.dot(v) / (self.magnitude() * v.magnitude()) )
    
    # projection of u onto v = proj_u (v) = (u*v / ||v||^2) * v
    #   self = u in this function defintion
    def proj(self, v):
        return v.copy().scale( self.dot(u) / self.dot(self) )

    # Vector multiplications
    def dot(self, v):
        if self.V != v.V:
            raise TypeError("Vectors do not occupy the same coordinate system.")
        if len(self.E) != len(v.E):
            raise TypeError("Dimensions of vectors do not match")
        
        out = 0
        for i in range(len(self.E)):
            out += self.E[i] * v.E[i]
        return simplify(out)    
    def cross(self, v):
        if self.V != v.V:
            raise TypeError("Vectors do not occupy the same coordinate system.")
        if len(v.E) != 3:
            raise TypeError("The cross product is only defined in 3 dimensions")
        if len(self.E) != len(v.E):
            raise TypeError("Dimensions of vectors do not match")
        
        return Vector(  [ simplify(self.E[2]*v.E[1] - self.E[1]*v.E[2]), 
                          simplify(self.E[0]*v.E[2] - self.E[2]*v.E[0]),
                          simplify(self.E[1]*v.E[0] - self.E[0]*v.E[1]) ], 
                      self.V)

    # This is just a straight partial derivative, independent of the coordinate system
    def Partial(self, t):
        u = self.copy()
        for i in range(len(self.E)):
            u.E[i] = diff(u.E[i], t)
        return u
        
    # Vector Calculus: these are dependent on the coordinate system
    def Div(self):
        return self.V.Div(self)
    def Curl(self):
        return self.V.Curl(self)
    def Laplacian(self):
        return self.V.Grad(self.Div())

"""
x = Symbol('x')
y = Symbol('y')
z = Symbol('z')
r = Symbol('r')
t = Symbol('t')
p = Symbol('p')


V = Curvillinear([1,1,1])
C = Cartesian3D()
Cy = Cylindrical()
S = Spherical()

v = Vector([r, t**2, z**2], Cy)
u = Vector([y, x, z], C)

print u
print v
print V
print V.reduce(1)
"""
