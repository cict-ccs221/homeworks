from turtle import*

shape("turtle")
wheel = 12
bgcolor("green")
pensize(12)
pencolor("yellow")

for i in range(wheel):
	begin_fill();rt(90);fd(200);lt(120);fd(200);lt(120);fd(200);end_fill()
	fd(200)

