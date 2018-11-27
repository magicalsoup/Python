import turtle

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
