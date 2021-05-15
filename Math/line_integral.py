from sympy import *
from vector import *

def line_integral_param(F, x, y, z, r, (t, t_a, t_b)):
    
    F = F.copy()

    for i in range(len(F.E)):
        F.E[i] = F.E[i].subs(x, r.E[0])
        F.E[i] = F.E[i].subs(y, r.E[1])
        F.E[i] = F.E[i].subs(z, r.E[2])
    
    dr = r.copy()
    for i in range(len(dr.E)):
        dr.E[i] = diff(r.E[i], t)
    
    return integrate(F.dot(dr), (t, t_a, t_b))

def line_integral_coord(F, x, y, z, C_a, C_b):
    
    F = F.copy()

    t = Symbol("t")
    r = Vector([C_a[0] + (C_b[0] - C_a[0])*t, C_a[1] + (C_b[1] - C_a[1])*t, C_a[2] + (C_b[2] - C_a[2])*t], F.V)
    
    for i in range(len(F.E)):
        F.E[i] = F.E[i].subs(x, r.E[0])
        F.E[i] = F.E[i].subs(y, r.E[1])
        F.E[i] = F.E[i].subs(z, r.E[2])

    dr = r.copy()
    for i in range(len(dr.E)):
        dr.E[i] = diff(r.E[i], t)

    return integrate(F.dot(dr), (t, 0, 1))

def line_integral_coordList(F, x, y, z, L, closed=True):
    
    accum = 0
    for i in range(len(L)-1):
        accum += line_integral_coord(F, x, y, z, L[i], L[i+1])
    
    if closed:
        accum += line_integral_coord(F, x, y, z, L[-1], L[0])

    return accum

x = Symbol("x")
y = Symbol("y")
z = Symbol("z")
t = Symbol("t")
C = Cartesian3D()

F = Vector([3*z+2*y, 2*x+z, 3*x+y], C)
r = Vector([3, 1-2*t, 2+t], C)

C1 = line_integral_param(F, x, y, z, r, (t, 0, 1))
print C1
print
C2 = line_integral_coord(F, x, y, z, (3, 1, 2), (3, -1, 3))
print C2
print
C3 = line_integral_coordList(F, x, y, z, [(3, 1, 2), (3, -1, 3)], False)
print C3
