import turtle

def line_without_moving():
    turtle.forward(50)
    turtle.backward(50)

line_without_moving()
turtle.right(90)
line_without_moving()
turtle.right(90)
line_without_moving()
turtle.right(90)
line_without_moving()

def star_arm():
    line_without_moving()
    turtle.right(360 / 5)

for _ in range(5):
    star_arm()
