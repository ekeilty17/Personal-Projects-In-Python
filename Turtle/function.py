from math import *
import numpy as np
from turtle import Turtle
alex = Turtle()

#function prototype
f = lambda x: x**2+10
#domain and range of the function
[a,b] = [-10,10]
a = float(a)
b = float(b)
fa = f(a)
fb = f(b)

#window parameters
def h_dotted(L):
    dash = 10
    for i in range(dash,L,2*dash):
        alex.forward(dash)
        alex.penup()
        alex.forward(dash)
        alex.pendown()
    alex.forward(dash)
    return True

def v_dotted(L):
    dash = 10
    for i in range(0,L,2*dash):
        alex.forward(dash)
        alex.penup()
        alex.forward(dash)
        alex.pendown()
    alex.forward(dash)
    return True

#scaling the coordinate system
w_length = 200
w_height = 200
wx_min = a/(b-a) * w_length
wx_max = b/(b-a) * w_length

#I need to find the max and min of f(x)
n = 100         #number of sub intervals
dx = (b-a)/n    #sub interval lengths
F = map(f,np.arange(a,b,dx))
F_min = min(F)
F_max = max(F)

wy_min = F_min/(F_max-F_min) * w_height
wy_max = F_max/(F_max-F_min) * w_height

#drawing the window
alex.penup()
alex.setposition(wx_min,0)
alex.pendown()
h_dotted(w_length)
#alex.forward(w_length)
alex.penup()
alex.setposition(0,wy_min)
alex.pendown()
alex.left(90)
v_dotted(w_height)
#alex.forward(w_height)
alex.right(90)

#scaling the function to fit the window
k = w_length/(b-a)
h = w_height/(F_max-F_min)


#putting the cursor in the right spot
alex.penup()
alex.setposition(k*a, h*f(a))
alex.pendown()

for i in np.arange(a,b+dx,dx):
    print i, f(i)
    alex.setposition(k*i,h*f(i))

alex.getscreen()._root.mainloop()
