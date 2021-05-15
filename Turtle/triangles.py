from math import *
from turtle import Turtle
alex = Turtle()

#alex.setposition(x,y)

def deg(x):
    return x*180/pi

def rad(x):
    return x*pi/180

def isTri(a,b,c):
    T = [a,b,c]
    m = max(T)
    T.remove(m)
    if T[0] + T[1] < m:
        return False
    return True

def equTri(s):
    alex.forward(s)
    alex.left(120)
    alex.forward(s)
    alex.left(120)
    alex.forward(s)
    alex.left(120)
    return True

def isocTri(b,s):
    if not isTri(b,s,s):
        return False
    s = float(s)
    b = float(b)
    alex.forward(b)
    #acos returns in radians
    theta = deg(acos(b/(2*s)))
    alex.left(180 - theta)
    alex.forward(s)
    alex.left(2*theta)
    alex.forward(s)
    alex.left(180-theta)
    return True


def SSS(a,b,c):
    if not isTri(a,b,c):
        return False
    a = float(a)
    b = float(b)
    c = float(c)
    #side a
    alex.forward(a)
    theta = deg(acos( (a*a+b*b-c*c)/(2*a*b) ))
    alex.left(180 - theta)
    #side b
    alex.forward(b)
    phi = deg(acos( (b*b+c*c-a*a)/(2*b*c) ))
    alex.left(180 - phi)
    #side c
    alex.forward(c)
    alex.left(theta+phi)
    return True

def SAS(a,theta,b):
    if theta <= 0 or theta >= 180:
        return False
    a = float(a)
    b = float(b)
    c = (a*a + b*b - 2*a*b*cos(rad(theta)))**(0.5)
    
    #side a
    alex.forward(a)
    alex.left(180-theta)
    #side b
    alex.forward(b)
    phi = 0
    #there's a weird error probably due to binary
    #where if phi is exactly 90 degrees it causes a
    #math error bc the number is actually slightly out of the range
    try:
        phi = deg(asin( (a/c)*sin(rad(theta)) ))
    except:
        if int( (a/c)*sin(rad(theta)) ) == 1:
            phi = 90
        else:
            return False
    #there are technically to solutions to ^
    #this is the second solution situation
    if a > b and a > c:
        phi = 180 - phi
    alex.left(180 - phi)
    #side c
    alex.forward(c)
    alex.left(theta+phi)
    return True

def ASA(theta,a,phi):
    if theta <= 0:
        return False
    if phi <= 0:
        return False
    if theta + phi >= 180:
        return False
    a = float(a)    
    #side a
    alex.forward(a)
    alex.left(180-phi)
    #side b
    b = a * (sin(rad(theta)) / sin(rad(180-theta-phi)))
    alex.forward(b)
    alex.left(theta+phi)
    #side c
    c = (a*a + b*b - 2*a*b*cos(rad(phi)))**(0.5)
    alex.forward(c)
    alex.left(180-theta)
    return True

def AAS(theta,phi,a):
    if theta <= 0:
        return False
    if phi <= 0:
        return False
    if theta+phi >= 180:
        return False
    a = float(a)
    #side a
    alex.forward(a)
    alex.left(theta+phi)
    #side b
    b = a * (sin(rad(theta)) / sin(rad(phi)))
    alex.forward(b)
    alex.left(180-phi)
    #side c
    c = (a*a + b*b - 2*a*b*cos(rad(180-theta-phi)))**(0.5)
    alex.forward(c)
    alex.left(180-theta)
    return True



alex.getscreen()._root.mainloop()
