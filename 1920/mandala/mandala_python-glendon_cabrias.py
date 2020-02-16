import turtle as diamond
import random

diamond.pensize(3)
diamond.speed(0)
diamond.Screen() .bgcolor("black")
colours = ["pink","red"]

diamond.tracer(2)
diamond.shape('blank')

for i in range(20):
	for i in range(2):
		diamond.color(colours[i%2])
		diamond.forward(200)
		diamond.right(60)
		diamond.forward(200)
		diamond.right(120)
		diamond.forward(200)
		diamond.right(60)
		diamond.forward(200)
	diamond.right(30)
	diamond.forward(30)
	
	diamond.penup()
	diamond.goto(0,50)
	diamond.pendown()
	
	diamond.circle(150)

diamond.done()
