import turtle
turtle.shape("turtle")
turtle.color("purple")
for i in range(4):
    turtle.forward(50)
    turtle.left(90)

turtle.penup()
turtle.goto(100,50)
turtle.color("red")
turtle.pendown()
for i in range(4):
    turtle.forward(50)
    turtle.left(90)
turtle.exitonclick()
