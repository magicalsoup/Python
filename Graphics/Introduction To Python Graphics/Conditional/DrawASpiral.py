import turtle
def draw_Spiral(radius):
    originalx_cor = turtle.xcor()
    originaly_cor = turtle.ycor()
    speed = 1
    while True:
        turtle.forward(speed)
        turtle.left(10)
        speed += 0.1
        if turtle.distance(originalx_cor, originaly_cor) > radius:
            break;

draw_Spiral(100)


