import turtle

wn = turtle.Screen()
wn.bgcolor('black')

flow = turtle.Turtle()
flow.speed(100)
flow.color('blue')
for i in range(500):
    flow.forward(i)
    flow.left(100)

ray= turtle.Turtle()
ray.color('red')

ray.speed(100)

for i in range(180):
    ray.forward(60)
    ray.right(30)
    ray.forward(20)
    ray.left(60)
    ray.forward(50)
    ray.right(30)

    ray.penup()
    ray.setposition(0, 0)
    ray.pendown()

    ray.right(2)

Zayn = turtle.Turtle()
Zayn.speed(100)
Zayn.color('lightblue')
rotate=int(360)
def drawCircles(t,size):
    for i in range(10):
        t.circle(size)
        size=size-4
def drawSpecial(t,size,repeat):
  for i in range (repeat):
    drawCircles(t,size)
    t.right(360/repeat)
drawSpecial(Zayn,100,10)

sun= turtle.Turtle()
sun.color('blue')
sun.speed(100)
for i in range(50):
    sun.forward(i)
    sun.left(151)
wn.exitonclick()


#improvised from Trinket & Michael0x2a code
