from math import *
from turtle import Turtle
alex = Turtle()

#alex.setposition(x,y)

def deg(x):
    return x*180/pi

def rad(x):
    return x*pi/180

def square(s):
    alex.forward(s)
    alex.left(90)
    alex.forward(s)
    alex.left(90)
    alex.forward(s)
    alex.left(90)
    alex.forward(s)

def circle(r):
    alex.circle(r)
    return True

def rect(a,b):
    alex.forward(a)
    alex.left(90)
    alex.forward(b)
    alex.left(90)
    alex.forward(a)
    alex.left(90)
    alex.forward(b)
    return True

def n_gon(s,n):
    if n < 3:
        return False
    ext_angle = 360/float(n)
    for i in range(0,n):
        alex.forward(s)
        alex.left(ext_angle)
    return True

def pentagram(s):
    alex.left(36)
    for i in range(0,5):
        alex.forward(s)
        alex.left(180-36)
    alex.right(36)

def satan(s):
    alex.left(72)
    for i in range(0,5):
        alex.forward(s)
        alex.left(180-36)
    alex.right(72)
    r = s / (2*sin(rad(108)))
    circle(r)


for i in range(3, 12):
    n_gon(60, i)

alex.getscreen()._root.mainloop()
