import turtle

#Exercise 1
'''
for i in range (10):
    turtle.forward(10)
    turtle.penup()
    turtle.forward(10)
    turtle.pendown()
'''
#Bonus
for i in range(10):
    turtle.forward(10 + i)
    turtle.penup()
    turtle.forward(10 + i)
    turtle.pendown()
