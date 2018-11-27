import turtle

def draw_Hexagon(length):
    for i in range(6):
        turtle.forward(length)
        turtle.left(60)


draw_Hexagon(100)
