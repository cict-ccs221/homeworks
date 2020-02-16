import turtle as nat

def writeText(text):
    nat.penup()
    nat.goto(0, 0)
    nat.pendown()
    nat.color('olive')
    style = ('Courier', 24, 'bold')
    nat.write(text, font=style, align='center')
    nat.hideturtle()