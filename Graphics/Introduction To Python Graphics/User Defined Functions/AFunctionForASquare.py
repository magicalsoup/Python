import turtle
turtle.width(5)
def drawSquare():
    for i in range(4):
        turtle.forward(100)
        turtle.right(90)

def goback():
    turtle.left(180)
for i in range (3):
    turtle.right(200)
    drawSquare()
    goback()
    
