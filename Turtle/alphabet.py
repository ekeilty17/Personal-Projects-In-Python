from turtle import Turtle
alex = Turtle()

# The heights of the letters need to be the same, 
#   otherwise it would be really hard to use and it would look bad

def A(l):
    # necessary dimensions
    curr = alex.position()
    x = curr[0]
    y = curr[1]
    a = l/4.0
    b = l/3.0
    
    # drawing outside of A
    alex.setposition(x+a, y+3*b)
    alex.forward(2*a)
    alex.setposition(x+4*a,y)
    alex.backward(a)
    alex.setposition(x+2*b, y+b)
    alex.setposition(x+b, y+b)
    alex.setposition(x+a, y)
    alex.backward(a)

    # drawing inside of a
    alex.penup()
    alex.setposition(x+(23.0/60.0)*l, y+(8.0/15.0)*l)
    alex.pendown()
    alex.setposition(x+(37.0/60.0)*l, y+(8.0/15.0)*l)
    alex.setposition(x+(34.0/60.0)*l, y+(4.0/5.0)*l)    
    alex.setposition(x+(26.0/60.0)*l, y+(4.0/5.0)*l)    
    alex.setposition(x+(23.0/60.0)*l, y+(8.0/15.0)*l)

    # setting pen to end of A
    alex.penup()
    alex.setposition(x+4*a, y)
    alex.pendown()


def B(l):

    # necessary dimensions
    curr = alex.position()
    x = curr[0]
    y = curr[1]
    
    # Outside of the B
    alex.setposition(x, y+l)
    alex.forward(l/4.0)
    alex.circle(-l/5.0,180)
    alex.right(180)
    alex.circle(-(3.0/10.0)*l,180)
    alex.right(180)
    alex.backward(l/4.0)
    
    # Inside of the B
    alex.penup()
    alex.setposition(x+l/6.0, y+l/6.0)
    alex.pendown()
    alex.setposition(x+l/6.0, y+(13.0/30.0)*l)
    alex.circle(-(2.0/15.0)*l,180)
    alex.right(180)

    alex.penup()
    alex.setposition(x+(1.0/6.0)*l, y+(9.0/10.0)*l)
    alex.pendown()
    alex.circle(-(1.0/10.0)*l,180)
    alex.right(180)
    alex.setposition(x+(1.0/6.0)*l, y+(9.0/10.0)*l)

    # setting pen positoion at the end of B
    alex.penup()
    alex.setposition(x + (11.0/20.0)*l, y)
    alex.pendown()


def C(l):
    return None

for i in range(100, 0, -10):
    B(i)

alex.getscreen()._root.mainloop()
