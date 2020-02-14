#Rose
import turtle

window = turtle.Screen()
window.bgcolor("Green")
t = turtle.Turtle()

t.speed (15)
colors = ['red', 'pink', 'red']

for x in range(180):
    t.pencolor (colors[x % 3])
    t.width (x / 50 + 1)
    t.forward (x)
    t.left (60)
    t.right (10)

turtle.exitonclick()

#Credits to (https://github.com/asweigart/simple-turtle-tutorial-for-python/blob/master/simple_turtle_tutorial.md)
#Elaisha D. Diana BSCS 1-B

