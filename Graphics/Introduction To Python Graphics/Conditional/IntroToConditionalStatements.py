import turtle

#Examples

#Example 1
condition = True

if condition:
    print("condition met")

if not condition:
    print("condition not met")

#Example 2
direction = -30

if direction > 0:
    turtle.forward(direction)

else:
    turtle.left(180)
    turtle.forward(-direction)

# Giving Directions

def move():
    direction = input("Go left or right? ")
    if direction == "left":
        turtle.left(60)
        turtle.forward(50)
    if direction == "right":
        turtle.right(60)
        turtle.forward(50)

# Data Munging
my_variable = "       I Am Capitalised"
print(my_variable)
my_stripped = my_variable.strip()
print(my_stripped)
my_lower = my_variable.lower()
print(my_lower)
