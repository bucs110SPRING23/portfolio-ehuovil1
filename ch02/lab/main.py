import pygame
import math
import random
import turtle
x = random.randrange(1,10)
print(x)
turtle1 = turtle.Turtle()
turtle2 = turtle.Turtle()
turtle1.penup()
turtle2.penup()
turtle1.goto((-100, 20))
turtle2.goto((-100, -20))
turtle1.pendown()
turtle2.pendown()
turtle1.forward(random.randrange(1,100))
turtle2.forward(random.randrange(1,100))
turtle1.penup()
turtle2.penup()
turtle1.goto((-100, 20))
turtle2.goto((-100, -20))
#race2
turtle1.pendown()
turtle2.pendown()
turtle1.speed(1)
turtle2.speed(1)
turtle1.color("blue")
turtle2.color("blue")
for i in range(10):
    
    turtle1.forward(random.randrange(1,100))
    turtle2.forward(random.randrange(1,100))
turtle1.penup()
turtle2.penup()
turtle1.goto((-100, 20))
turtle2.goto((-100, -20))
turtle.exitonclick()
#partB
pygame.init()
window = pygame.display.set_mode()

xpos
ypos
def getpoints(num_sides, side_length):
    points = []
    for i in range(num_sides):
        angle = 360/num_sides
        radians = math.radians(angle * i)
        x = xpos + side_length * math.cos(radians)
        y = ypos + side_length * math.sin(radians)
        points.append([x, y])
        #pygame.display.flip()
    return points
triangle = getpoints(3, 20)
pygame.draw.polygon(window, "blue", triangle)
square = getpoints(4, 20)

hexagon = getpoints(6, 20)

icosagon = getpoints(20, 20)

hectagon = getpoints(100, 20)

circleish = getpoints(360, 20)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()