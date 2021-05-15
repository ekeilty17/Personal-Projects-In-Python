from sympy import * 
from vector import *

def normal(r, u, v):
    return r.Partial(u).cross(r.Partial(v)) 

def surface_integral(F, x, y, z, r, (u, u_a, u_b), (v, v_a, v_b), invert):
    
    F = F.copy()
    r = r.copy()

    n = normal(r, u, v)    
    if invert:
        n *= -1

    for i in range(len(F.E)):
        F.E[i] = F.E[i].subs(x, n.E[0])
        F.E[i] = F.E[i].subs(y, n.E[1])
        F.E[i] = F.E[i].subs(z, n.E[2])     
    
    return integrate( integrate(F.dot(r), (u, u_a, u_b)), (v, v_a, v_b) )


x = Symbol("x")
y = Symbol("y")
z = Symbol("z")
u = Symbol("u")
v = Symbol("v")
C = Cartesian3D()

F = Vector([x**2, x-y, 2*z], C)
r1 = Vector([u*cos(v), u*sin(v), 1], C)
r2 = Vector([u*cos(v), u*sin(v), u**2], C)

S1 = surface_integral(F, x, y, z, r1, (u, 0, 1), (v, 0, 2*pi), True)
S2 = surface_integral(F, x, y, z, r2, (u, 0, 1), (v, 0, 2*pi), False)

print S1
print S2
print S1 + S2
