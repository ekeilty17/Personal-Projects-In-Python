from sympy import *

# y' = f(x) * g(y)
# integral(1/y) = integral(x) + C
def separable(f, g, x, y):
    C = Symbol('C')
    return simplify( solve(integrate(1/g, y) - integrate(f, x) - C, y)[0] )


t = Symbol('t')
s = Symbol('s')
f = Function('f')
g = Function('g')

f = t**2
g = s

print separable(f, g, t, s)
