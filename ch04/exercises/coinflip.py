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
for i in range (0, 10):
    flip = random.randrange(0, 1)
    if flip == 0:
        bob.left(90)
        bob.forward(50)
        turtle.exitonclick()
    if flip == 1:
        bob.right(90)
        bob.forward(50)
        turtle.exitonclick()

