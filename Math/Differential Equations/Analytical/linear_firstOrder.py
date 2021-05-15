from sympy import *

# y' + p(x)y = g(x)
# u = exp(integral(p(x))
# y = ( integral(g(x)*u(x)) + C ) / u(x)
def linear_firstOrder(p, g, x):
    u = Function('u')
    C = Symbol('C')
    u = exp(integrate(p, x))
    return simplify( (integrate(g * u, x) + C) / u )

t = Symbol('t')
p = Function('p')
g = Function('g')

p = t
g = t

print linear_firstOrder(p, g, t)
