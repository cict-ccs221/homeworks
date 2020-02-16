from turtle import*
from random import randint

speed(50)
bgcolor('black')

x=2

while x < 500:

    r=randint(10,255)
    g=randint(10,255)
    b=randint(10,255)

    colormode(255)
    pencolor(r,g,b)

    fd(50+x)
    rt(90.911)

    x=x+1

exitonclick()
