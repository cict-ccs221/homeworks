import turtle
import math

billy=turtle.Turtle()
willy=turtle.Turtle()
dilly=turtle.Turtle()

billy.color("red")
willy.color("red")
dilly.color("red")
billy.shape("blank")
willy.shape("blank")
dilly.shape("blank")
billy.speed(20)
willy.speed(15)
dilly.speed(20)
for i in range(25):
	billy.forward(150)
	billy.left(170)
	billy.forward(150)
	billy.left(170)
billy.left(275)
billy.circle(76)
willy.forward(200)
willy.left(85)

willy.circle(125)
willy.left(98)
willy.forward(20)
willy.right(98)
willy.circle(104)
willy.right(90)
willy.forward(10)
willy.left(90)
willy.circle(114.5)
willy.right(45)
def sarkul():
        willy.begin_fill()
        willy.circle(25,105)
        willy.right(80)
        willy.end_fill()
sarkul()
sarkul()
def sarkul2():
        
        willy.right(10)
        willy.circle(25,104)
        willy.right(85)

for i in range(5):
        sarkul2()
        sarkul()
        sarkul()

sarkul2()
sarkul()


turtle.done()
