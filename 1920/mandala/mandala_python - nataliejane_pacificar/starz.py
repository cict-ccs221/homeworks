import turtle as nat

my_pen = nat.Pen()
colors = [ "red","purple","blue","green","orange","yellow"]

def star(a, b, c):
    for x in range(c):
        my_pen.speed(0)
        my_pen.penup()
        my_pen.goto(a, b)
        my_pen.pendown()
        my_pen.pencolor(colors[x % 6])
        my_pen.width(x/60 + 1)
        my_pen.forward(x)
        my_pen.left(59)