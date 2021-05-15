from sympy import *
import sys

class Curvillinear(object):

    def __init__(self, H, X=None):
        if X == None:
            X = []
            for i in range(len(H)):
                X += [Symbol('x' + str(i+1))]
        if type(H) != list:
            raise TypeError("Fist argument must be a list.")
        if type(X) != list:
            raise TypeError("Second argument must be a list.")
        if len(H) != len(X):
            raise TypeError("Number of jacobeans must equal the number of independent variables.")

        # Jacobeans of each coordinate
        self.H = H
        # Independent variables (sympy variables)
        self.X = X
        # Total Jacobean
        self.J = 1
        for h in H:
            self.J *= h

    def __str__(self):
        basis = ""
        variables = ""
        for i in range(len(self.H)):
            basis += self[i]
            variables += str(self.X[i])
            if i != len(self.H)-1:
                basis += ", "
                variables += ", "
        return "(" + basis + ")\t(" + variables + ")"
    
    def __len__(self):
       return len(self.H)
   
    def __eq__(self, V):
        return (isinstance(V, Curvillinear) and self.H == V.H and self.X == V.X)

    def __ne__(self, V):
        return not self.__eq__(V)

    def __getitem__(self, i):
        if type(i) != int:
            raise TypeError("Index must be an integer.")
        if i < (-1*len(self.H)) or i >= len(self.H):
            raise TypeError("There only exists " + str(len(self.H)) + " basis elements.")
        if i < 0:
            return "e" + str( len(self.H) + i )
        return "e" + str(i+1)
    
    def reduce(self, i):
        if type(i) != int:
            raise TypeError("Index must be an integer.")
        if i < 0 or i >= len(self.H):
            raise TypeError("There only exists " + str(len(self.H)) + " basis elements.") 
        return Curvillinear(self.H[:i] + self.H[i+1:], self.X[:i] + self.X[i+1:])

    def Grad(self, f):
        coord = []
        for i in range(len(X)):
            coord += [simplify(diff(f, self.X[i]) / self.H[i])]
        return Vector(coord, self)

    def Div(self, v):
        out = 0
        for i in range(len(v.E)):
            factor = simplify(v.V.J / self.H[i])
            out += diff(factor * v.E[i], self.X[i])
        return simplify(out / self.J)

    def Curl(self, v):

        if len(v.E) != 3:
            raise TypeError("Curl is only defined in 3 dimensions")

        return Vector(  [ (diff(self.X[2]*v.E[2], self.X[1]) - diff(self.X[1]*v.E[1], self.X[2])) / (self.X[1]*self.X[2]),
                          (diff(self.X[0]*v.E[0], self.X[2]) - diff(self.X[2]*v.E[2], self.X[0])) / (self.X[2]*self.X[0]),
                          (diff(self.X[1]*v.E[1], self.X[0]) - diff(self.X[0]*v.E[0], self.X[1])) / (self.X[0]*self.X[1])],
                      self)

    def Laplacian(self, f):
        return self.Grad(f).Div()

# Common Curvillinear Coordinate Systems
class Cartesian2D(Curvillinear):
    def __init__(self, X=[Symbol('x'), Symbol('y')]):
        if len(X) != 2:
            raise TypeError("Number of independent variables must be equal to 2")
        Curvillinear.__init__(self, [1, 1], X)

    def __eq__(self, V):
        return isinstance(V, Cartesian2D)

    def __getitem__(self, i):
        if i == 0:
            return "i"
        elif i == 1:
            return "j"
        else:
            raise TypeError("There are only 2 basis elements")

class Polar(Curvillinear):
    def __init__(self, X=[Symbol('r'), Symbol('t')]):
        if len(X) != 2:
            raise TypeError("Number of independent variables must be equal to 2")
        Curvillinear.__init__(self, [1, X[0]], X)

    def __eq__(self, V):
        return isinstance(V, Polar)

    def __getitem__(self, i):
        if i == 0:
            return "r"
        elif i == 1:
            return u'\u03B8'
        else:
            raise TypeError("There are only 2 basis elements")

class Cartesian3D(Curvillinear):
    def __init__(self, X=[Symbol('x'), Symbol('y'), Symbol('z')]):
        if len(X) != 3:
            raise TypeError("Number of independent variables must be equal to 3")
        Curvillinear.__init__(self, [1, 1, 1], X)

    def __eq__(self, V):
        return isinstance(V, Cartesian3D)

    def __getitem__(self, i):
        if i == 0:
            return "i"
        elif i == 1:
            return "j"
        elif i == 2:
            return "k"
        else:
            raise TypeError("There are only 3 basis elements")

    def reduce(self, i):
        if type(i) != int:
            raise TypeError("Index must be an integer.")
        if i < 0 or i >= len(self.H):
            raise TypeError("There only exists " + str(len(self.H)) + " basis elements.")
        return Cartesian2D(self.X[:i] + self.X[i+1:])

class Cylindrical(Curvillinear):
    def __init__(self, X=[Symbol('r'), Symbol('t'), Symbol('z')]):
        if len(X) != 3:
            raise TypeError("Number of independent variables must be equal to 3")
        Curvillinear.__init__(self, [1, X[0], 1], X)

    def __eq__(self, V):
        return isinstance(V, Cylindrical)

    def __getitem__(self, i):
        if i == 0:
            return "r"
        elif i == 1:
            return u'\u03B8'
        elif i == 2:
            return "z"
        else:
            raise TypeError("There are only 3 basis elements in Cylindrical Coordinates")
    
    def reduce(self, i):
        if type(i) != int:
            raise TypeError("Index must be an integer.")
        if i < 0 or i >= len(self.H):
            raise TypeError("There only exists " + str(len(self.H)) + " basis elements.")
        if i == 0:
            return Curvillinear(self.H[:i] + self.H[i+1:], self.X[:i] + self.X[i+1:])
        if i == 1:
            return Cartesian2D(self.X[:i] + self.X[i+1:])
        if i == 2:
            return Polar(self.X[:i] + self.X[i+1:])

class Spherical(Curvillinear):
    def __init__(self, X=[Symbol('r'), Symbol('t'), Symbol('p')]):
        if len(X) != 3:
            raise TypeError("Number of independent variables must be equal to 3")
        Curvillinear.__init__(self, [1, X[0], X[0]*sin(X[2])], X)

    def __eq__(self, V):
        return isinstance(V, Spherical)

    def __getitem__(self, i):
        if i == 0:
            return "r"
        elif i == 1:
            return u'\u03B8'
        elif i == 2:
            return u'\u03C6'
        else:
            raise TypeError("There are only 3 basis elements in Spherical Coordinates")

    def reduce(self, i):
        if type(i) != int:
            raise TypeError("Index must be an integer.")
        if i < 0 or i >= len(self.H):
            raise TypeError("There only exists " + str(len(self.H)) + " basis elements.")
        if i == 0:
            return Curvillinear(self.H[:i] + self.H[i+1:], self.X[:i] + self.X[i+1:])
        if i == 1:
            return Polar(self.X[:i] + self.X[i+1:])
        if i == 2:
            return Polar(self.X[:i] + self.X[i+1:])

# Cartesian is just Curvillinear with the stardard basis
class Cartesian(Curvillinear):
    # 3 dimensions is default
    def __init__(self, n=3):
        X = []
        if type(n) == list:
            X = n
            for e in X:
                if not isinstance(e, Symbol):
                    raise TypeError("Variable list must contain elements of type sympy Symbol.")
        else:
            if int(n) != n:
                raise TypeError("Vector spaces must have an integer number of dimensions.")
            if n < 0:
                raise TypeError("Vector spaces must have a positive number of dimensions.")
            if n == 0:
                raise TypeError("A vector space of zero dimensions has not been implemented.")
            for i in range(n):
                X += [Symbol('x' + str(i+1))]
        Curvillinear.__init__(self, [1]*len(X), X)

    def __eq__(self, V):
        return isinstance(V, Cartesian)

    def reduce(self, i):
        if type(i) != int:
            raise TypeError("Index must be an integer.")
        if i < 0 or i >= len(self.H):
            raise TypeError("There only exists " + str(len(self.H)) + " basis elements.")
        return Curvillinear(self.H[:i] + self.H[i+1:], self.X[:i] + self.X[i+1:])
