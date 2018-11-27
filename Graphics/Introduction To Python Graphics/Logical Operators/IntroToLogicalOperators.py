import turtle
'''
x = False

if not x:
    print("condition met")

else:
    print("condition not met")

def forward(length):
    if not turtle.isdown():
        turtle.forward(length)

# Exercise 1
turtle.penup()
forward(100)
turtle.pendown()
forward(100)


#Exercise 2

if 1 < 2 and 4 > 2:
    print("condition met")

if 1 > 2 and 4 < 10:
    print("condition not met")

if 4 < 10 or 1 < 2:
    print("condition met")

'''
# Exercise 3

def not_in_box():
    if turtle.xcor() > 100 or turtle.ycor() > 100
    or turtle.xcor() < -100 or turtle.ycor() < -100:
        return True
    return False


def forward(length):
    while length > 0:
        if not_in_box():
            angle = turtle.towards(0, 0)
            turtle.setheading(angle)
        turtle.forward(1)
        length = length - 1


turtle.left(45)
turtle.forward(200)
forward(200)
