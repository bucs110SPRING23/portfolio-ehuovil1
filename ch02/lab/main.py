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
turtle1.speed(0)
turtle2.speed(0)
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

#triangle (3 sides)
#square (4 sides)
#hexagon (6 sides)
#icosagon (20 sides)
#Hectagon (100 sides)
#circle -ish (360 sides)


#points = []
#tnum_sides = 3
#tside_length = 18
#xpos = 30
#ypos = 40
#tangle = 360 / tnum_sides
#radians = math.radians(tangle * i)
#x = xpos + tside_length * math.cos(radians)
#y = ypos + tside_length * math.sin(radians)
#points.append([x,y])
#x2 = xpos + tside_length * math.cos(radians)
#y2 = ypos + tside_length * math.sin(radians)
#points.append([x,y])
#x3 = xpos + tside_length * math.cos(radians)
#y3 = ypos + tside_length * math.sin(radians)
#points.append(x,y)
##pygame.draw.polygon(points)
#p#ygame.display.flip()
#p#oints.clear
#window.fill("blue")
#pygame.display.flip()
#pygame.time.delay()
#print(points)
#while running:
#    for event in pygame.event.get():
#        if event.type == pygame.QUIT:
#            running = False#

#pygame.quit()


xpos = 200
ypos = 200
def getpoints(num_sides, side_length):
    points = []
    for i in range(num_sides):
        angle = 360/num_sides
        radians = math.radians(angle * i)
        x = xpos + side_length * math.cos(radians)
        y = ypos + side_length * math.sin(radians)
        points.append([x, y])
        pygame.display.flip()
    return points

triangle = getpoints(3, 20)
window.fill("white")
pygame.draw.polygon(window, "blue", triangle)
pygame.time.wait(2000)


square = getpoints(4, 20)
window.fill("blue")
pygame.draw.polygon(window, "green", square)
pygame.time.wait(2000)


hexagon = getpoints(6, 20)
window.fill("white")
pygame.draw.polygon(window, "red", hexagon)
pygame.time.wait(2000)


icosagon = getpoints(20, 20)
window.fill("yellow")
pygame.draw.polygon(window, "purple", icosagon)
pygame.time.wait(2000)


hectagon = getpoints(100, 20)
window.fill("red")
pygame.draw.polygon(window, "blue", hectagon)
pygame.time.wait(2000)

circleish = getpoints(360, 20)
window.fill("yellow")
pygame.draw.polygon(window, "black", circleish)
pygame.time.wait(2000)


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()