import turtle as nat

def outerPattern(small,big):
    nat.pensize(10)
    nat.speed(0)
    nat.circle(small, 180)
    nat.right(90)
    nat.circle(big,45)
    nat.right(90)
    nat.circle(small, 180)
    nat.right(90)
    nat.circle(big,45)
    nat.right(90)