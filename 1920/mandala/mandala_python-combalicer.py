import turtle

# initialize
wn = turtle.Screen()
wn.bgcolor("#333333")
draw= turtle.Turtle()
draw.speed(10)
draw.pensize(1.2)

# position
ww = wn.window_width()
wh = wn.window_height()
draw.penup()
draw.setposition((-ww/2.4,-wh/35))



# 5th layer
for i in range(3):
    for rainbow in ("red", "orange", "yellow", "green", "blue", "indigo", "violet"):
        draw.pendown()
        draw.color(rainbow)
        draw.circle(50, 160)
        draw.right(180)
draw.penup()
draw.forward(80)
draw.pendown()

# 4th layer
for i in range(3):
    for rainbow in ("red", "orange", "yellow", "green", "blue", "indigo", "violet"):
        draw.color(rainbow)
        draw.circle(38, 160)
        draw.right(180)
draw.penup()
draw.forward(80)
draw.pendown()

# 3rd layer
for i in range(3):
    for rainbow in ("red", "orange", "yellow", "green", "blue", "indigo", "violet"):
        draw.color(rainbow)
        draw.circle(25, 160)
        draw.right(180)
draw.penup()
draw.forward(80)
draw.pendown()

# 2nd layer
draw.color("white")
draw.right(90)
draw.circle(60)
draw.left(90)
draw.penup()
draw.forward(80)
draw.pendown()

# 1st layer
draw.color("cyan")
draw.begin_fill()
draw.right(270)
draw.circle(20)
draw.end_fill()

# Line 1
draw.left(309.5)
draw.forward(260)
draw.right(180)
draw.forward(270)
# Line 2
draw.left(159.3)
draw.forward(265)
draw.right(180)
draw.forward(270)
for i in range(5):
    draw.left(160)
    draw.forward(275)
    draw.right(180)
    draw.forward(275)
for i in range(3):
    draw.left(161)
    draw.forward(280)
    draw.right(180)
    draw.forward(280)
for i in range(5):
    draw.left(160)
    draw.forward(275)
    draw.right(180)
    draw.forward(275)
for i in range(3):
    draw.left(159)
    draw.forward(275)
    draw.right(180)
    draw.forward(275)

turtle.done()

# own made
