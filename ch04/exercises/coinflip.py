import turtle
import random
bob = turtle.Turtle()
bob.shape("turtle")
bob.color("purple")
heads = 0
tails = 1

bob.penup()
bob.goto(0, 0)
#
for i in range (10):
    flip = random.randint(0,1)
    print(flip)
    if flip == 0:
        bob.left(90)
        bob.forward(50)
    elif flip == 1:
        bob.right(90)
        bob.forward(50)


turtle.exitonclick()

