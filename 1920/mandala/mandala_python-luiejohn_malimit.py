import turtle as jim

jim.Screen().bgcolor("black")

jim.tracer(20)
jim.speed(10.5)
jim.shape('arrow')

a = 0
color = 0

primColor = ['red', 'orange', 'yellow']
secColor = ['violet', 'indigo', 'blue']


for j in range(300, 0, -60):
    jim.color('','green')
    jim.penup()
    jim.goto(0,-j)
    jim.pendown()
    if a%2 == 0:
        jim.begin_fill()
        jim.circle(j)
        jim.end_fill()
    a+=1
    jim.penup()
    jim.goto(0,0)
    jim.pendown()
    jim.color('','black')
    for i in range(18):
        jim.left(60)
        jim.begin_fill()
        jim.forward(j)
        jim.right(210)
        jim.forward(j)
        jim.end_fill()
        jim.goto(0,0)
    color+=1

jim.done()
