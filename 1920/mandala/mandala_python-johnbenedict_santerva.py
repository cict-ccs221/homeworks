import turtle

loadWindow = turtle.Screen()
turtle.colormode(255)

turtle.speed(0)

def shape(size, sides):
    for i in range(sides):
        turtle.forward(size)
        turtle.left(360/sides)


sides=2

for i in range (50):
    for colours in ("yellow", "black", "green", "red", "purple"):
        turtle.color(colours)
        shape(5*i, sides)
        turtle.right(i)

turtle.exitonclick()
