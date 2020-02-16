## The Yin and Yang code at the CENTER is taken from "I know python's" youtube channel
## The star is a sample code I found online
import turtle as nat
import yinyang as yinyang
import outerPattern as outer
import liness as liness
import writeText as writeText
import starz as starz

bgcolor = "mediumseagreen"
colors = [ "red","purple","blue","green","orange","yellow"]

window = nat.Screen()
window.bgcolor(bgcolor)

#MAIN
#creates star
starz.star(-400, 200, 48)
starz.star(400,200, 36)
starz.star(-300,360, 28)
starz.star(300,360, 28)
starz.star(-200,450, 24)
starz.star(200,450, 24)
starz.star(-100,520, 24)
starz.star(100,520, 24)

#draws the yin and yang pattern
yinyang.pattern("white", "black")
yinyang.pattern("black", "white")

#draws the outerPattern function
nat.penup()
nat.goto(380, -50)
nat.pendown()
for i in range(4):
    outer.outerPattern(50,260)

#draws a circle around the yin and yang
nat.left(90)
nat.penup()
nat.goto(320,0)
nat.pendown()
nat.pensize(10)
nat.circle(320)

#draws the lines over the circle around the yin and yang
nat.penup()
nat.goto(350,0)
nat.pendown()
liness.liness(350,30)

#writes text that appear in the center
writeText.writeText("You are the Yin to my Yang")

nat.done()
