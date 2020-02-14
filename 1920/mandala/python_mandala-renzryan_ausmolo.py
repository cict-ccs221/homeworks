import turtle
import math
import random
wn = turtle.Screen()

wn.bgcolor('black')
Albert = turtle.Turtle()
Albert.speed(0)
Albert.color('#1b262c')
rotate=int(360)
def drawCircles(t,size):
    for i in range(50):
        t.circle(size)
        size=size-2
def drawSpecial(t,size,repeat):
  for i in range (repeat):
    drawCircles(t,size)
    t.right(360/repeat)
drawSpecial(Albert,100,10)
Steve = turtle.Turtle()
Steve.speed(0)
Steve.color('#0f4c75')
rotate=int(90)
def drawCircles(t,size):
    for i in range(6):
        t.circle(size)
        size=size-5
def drawSpecial(t,size,repeat):
    for i in range (repeat):
        drawCircles(t,size)
        t.right(360/repeat)
drawSpecial(Steve,100,10)
Barry = turtle.Turtle()
Barry.speed(30)
Barry.color('#3282b8')
rotate=int(80)
def drawCircles(t,size):
    for i in range(5):
        t.circle(size)
        size=size-5
def drawSpecial(t,size,repeat):
    for i in range (repeat):
        drawCircles(t,size)
        t.right(360/repeat)
drawSpecial(Barry,100,10)
Terry = turtle.Turtle()
Terry.speed(0)
Terry.color('#bbe1fa')
rotate=int(90)
def drawCircles(t,size):
    for i in range(4):
        t.circle(size)
        size=size-6
def drawSpecial(t,size,repeat):
    for i in range (repeat):
        drawCircles(t,size)
        t.right(360/repeat)
drawSpecial(Terry,100,10)
Will = turtle.Turtle()
Will.speed(0)
Will.color('pink')
rotate=int(90)
def drawCircles(t,size):
    for i in range(3):
        t.circle(size)
        size=size-20
def drawSpecial(t,size,repeat):
    for i in range (repeat):
        drawCircles(t,size)
        t.right(360/repeat)
drawSpecial(Will,100,10)

turtle.done()
