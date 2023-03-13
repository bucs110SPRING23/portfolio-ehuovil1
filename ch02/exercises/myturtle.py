import turtle
bob = turtle.Turtle()
bob.shape("turtle")
bob.color("purple")
for i in range(4):
    bob.forward(50)
    bob.left(90)

bob.penup()
bob.goto(100,50)
bob.color("red")
bob.pendown()
for i in range(4):
    bob.forward(50)
    bob.left(90)
turtle.exitonclick()
