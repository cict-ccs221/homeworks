import turtle as nat

bgcolor = "mediumseagreen"

def liness(length, angle):
    nat.speed(0)
    for i in range(8):
        nat.circle(length,angle)
        nat.pencolor(bgcolor)
        nat.circle(length, angle)
        nat.pencolor("black")