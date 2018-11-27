import turtle

def draw_Shape(sides,length):
    for i in range (sides):
        turtle.forward(length)
        turtle.left(360 / sides)


draw_Shape(3, 100)
