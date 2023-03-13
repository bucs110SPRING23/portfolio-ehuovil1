import turtle #1. import modules
import random
import math
import pygame
#Part A
#window = turtle.Screen() # 2.  Create a screen
#window.bgcolor('lightblue')

#michelangelo = turtle.Turtle() # 3.  Create two turtles
#leonardo = turtle.Turtle()
#michelangelo.color('orange')
#leonardo.color('blue')
#michelangelo.shape('turtle')
#leonardo.shape('turtle')

#michelangelo.up() # 4. Pick up the pen so we don’t get lines
#leonardo.up()
#michelangelo.goto(-100,20)
#leonardo.goto(-100,-20)

## 5. Your PART A code goes here
#background
pygame.init()
display = pygame.display.set_mode((500, 500))
pygame.time.wait(200)
display.fill("light blue")
pygame.display.update()
pygame.draw.circle(display, "red", [250, 250], 250)
pygame.draw.line(display, "black", [250, 0], [250, 500])
pygame.draw.line(display, "black", [0, 250], [500, 250])
pygame.display.update()
pygame.time.wait(200)

running = True
#inside
#screen_width=700
#screen_height=400
#screen=pygame.display.set_mode([screen_width, screen_height])

# PART B - complete part B here

for i in range(10):
    xCord = random.randrange(0, 500)
    yCord = random.randrange(0, 500)
    distance_from_center = math.hypot(xCord - 250,yCord - 250)
    if distance_from_center <= 250:
        pygame.draw.circle(display, "green", [xCord, yCord], 5)
        pygame.display.update()
        #pygame.time.wait(200)

    else:
        pygame.draw.circle(display, "black", [xCord, yCord], 5)
        pygame.display.update()
        #pygame.time.wait(200)
    #pygame.display.update()
    #pygame.time.wait(200)

 #the distance formula

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
