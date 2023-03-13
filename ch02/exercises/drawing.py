import turtle
Sides = int(input("Enter number of sides:"))
Length = int(input("Enter length of sides:"))
angle = 360 / Sides
print(angle)

turtle.shape("turtle")
turtle.color("blue")
turtle.pencolor("green")
for i in range(Sides):
    turtle.forward(Length)
    turtle.left(angle)

turtle.exitonclick()