# Mandala Homework
import turtle

turtle.bgcolor("black")
turtle.pensize(2)
turtle.speed(0)

for i in range(10):
    for colours in ["orange", "orange", "orange", "orange", "orange", "orange", "orange", "orange", "orange", "orange"]:
        turtle.color(colours)
        turtle.circle(150)
        turtle.circle(110)
        turtle.circle(90)
        turtle.circle(80)
        turtle.circle(50)
        turtle.left(10)

turtle.hideturtle()

# credit to GeekTutorials
