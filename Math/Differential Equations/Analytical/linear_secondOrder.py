from sympy import *

# ay'' + by' + c = g(t)
def linear_secondOrder_constantCoefficients(a, b, c, x=Symbol('x'), g=0):
    if a == 0:
        raise TypeError("coefficients have to be nonzero")
    
    D = b**2 - 4*a*c
    C1 = Symbol('C1')
    C2 = Symbol('C2')
    
    y1 = 0
    y2 = 0
    if D > 0:       # real and distinct eigenvalues
        L1 = (-b + D**0.5)/float(2*a)
        L2 = (-b - D**0.5)/float(2*a)        
        #y_h = C1*exp(L1*x) + C2*exp(L2*x)
        y1 = exp(L1*x)
        y2 = exp(L2*x)

    elif D < 0:     # complex conjugate eigenvalues
        L_a = -b/float(2*a)
        L_b = (-1*D)**0.5/float(2*a)
        #y_h = exp(L_a*x)*( C1*cos(L_b*x) + C2*sin(L_b*x) )
        y1 = exp(L_a*x)*cos(L_b*x)
        y2 = exp(L_a*x)*sin(L_b*x)

    else:
        L = -b/float(2*a)
        #y_h = (C1 + C2*x)*exp(L*x)
        y1 = exp(L*x)
        y2 = x*exp(L*x)
        

    # Using variations of parameters
    W = simplify(y1 * diff(y2, x) -  y2 * diff(y1, x))
    y_p = -y1 * integrate(y2*g/W, x) + y2 * integrate(y1*g/W, x)
        
    y = C1*y1 + C2*y2 + y_p
    print
    print y
    print

t = Symbol('t')
# ay'' + by' + c = g(t)
linear_secondOrder_constantCoefficients(1, -4, 4, t, 0)

