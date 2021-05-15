from sympy import *

def f(t, y):
    return y**2

y = Symbol('y')
t = Symbol('t')

t0 = 0
y0 = 1

yn = y0
print yn
for i in range(3):
    yn = y0 + integrate(f(t, yn), (t, 0, t))
    print yn
