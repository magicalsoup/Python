import turtle
import math
turtle.color('blue')

turtle.width(5)

a = 50
b = 50
c = math.sqrt(a**2 + b**2)
tilt1 = 90
tilt2 = 135
a2 = math.sqrt(c**2) / 2

turtle.forward(a)
turtle.left(tilt2)
turtle.forward(c)
turtle.left(tilt2)
turtle.forward(a)
turtle.left(tilt2)
turtle.forward(c)
turtle.left(tilt2)
turtle.forward(a)
turtle.right(tilt2)
turtle.forward(a2)
turtle.right(tilt1)
turtle.forward(a2)
turtle.right(45)
turtle.forward(a)
