import turtle
'''
def line_without_moving():
    turtle.forward(50)
    turtle.backward(50)
'''
def line_without_moving(length):
    turtle.forward(length)
    turtle.backward(length)

def tilted_line_without_moving(length, angle):
    turtle.left(angle)
    turtle.forward(length)
    turtle.backward(length)


line_without_moving(100)
tilted_line_without_moving(100, 90)
