import turtle

turtle.width(3)
def drawHexagon():
    for i in range (6):
        turtle.left(60)
        turtle.forward(50)

for i in range (6):
    drawHexagon()
    turtle.right(60)
    turtle.forward(50)
