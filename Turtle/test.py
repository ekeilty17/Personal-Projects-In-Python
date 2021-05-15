from turtle import Turtle
alex = Turtle()
alex.position()
alex.forward(100)
alex.left(90)
alex.forward(100)

for i in range(0,10,0.1):
    print i

alex.getscreen()._root.mainloop()
