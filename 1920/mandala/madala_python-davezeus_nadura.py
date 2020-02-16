import turtle
window = turtle.Screen()
window.bgcolor("black")


junjun = turtle.Turtle()
junjun.color("#e3cf57")
junjun.speed(-25)


turtle = turtle.Turtle()
turtle.speed(0)
turtle.color("#ffec8b")


x = 0
turtle.setposition(20,65)
turtle.up()

turtle.right(40)
turtle.forward(50)
turtle.right(135)

turtle.down()
for i in range(70):
    turtle.forward(100)
    turtle.left(130)
x = 0
junjun.up()

junjun.right(55)
junjun.forward(70)
junjun.right(135)

junjun.down()

for i in range(120):
    junjun.forward(200)
    junjun.right(61)
    junjun.forward(200)
    junjun.right(61)
    junjun.forward(200)
    junjun.right(61)
    junjun.forward(200)
    junjun.right(61)
    junjun.forward(200)
    junjun.right(61)
    junjun.forward(200)
    junjun.right(61)

    junjun.right(11.1111)
    junjun.hideturtle()
    x = x + 1
input()


turtle.exitonclick()
