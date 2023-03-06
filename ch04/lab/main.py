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


#inside
#screen_width=700
#screen_height=400
#screen=pygame.display.set_mode([screen_width, screen_height])
green = 0
white = 0




# PART B - complete part B here
#distance_from_center = math.hypot(xCord - 250,yCord - 250)
#if distance_from_center <= 250:
    
for i in range(10):
    xCord = random.randrange(0, 500)
    yCord = random.randrange(0, 500)
    distance_from_center = math.hypot(xCord - 250,yCord - 250)
    if distance_from_center <= 250:
        pygame.draw.circle(display, "green", [xCord, yCord], 5)
        pygame.display.update()
        green +=1

    else:
        pygame.draw.circle(display, "black", [xCord, yCord], 5)
        pygame.display.update()   

for i in range(10):
    xCord = random.randrange(0, 500)
    yCord = random.randrange(0, 500)
    distance_from_center = math.hypot(xCord - 250,yCord - 250)
    if distance_from_center <= 250:
        pygame.draw.circle(display, "white", [xCord, yCord], 5)
        pygame.display.update()
        white +=1
    else:
        pygame.draw.circle(display, "black", [xCord, yCord], 5)
        pygame.display.update()   

if green > white:
    winner = "Green Wins!"
elif green < white:
    winner = "White Wins!"
else:
    winner = "It's a Tie!"


#part B
#Player Green Will Win!
color_dark = (100,100,100)
pygame.draw.rect(display, "green", [90, 120, 120, 60])
smallfont = pygame.font.SysFont('Corbel',16) 
text1 = smallfont.render('Player Green Will Win!' , True , "black")
display.blit(text1 , (90 , 120))
pygame.display.update()
#Player White Will Win!
color_dark = (100,100,100)
pygame.draw.rect(display, "white", [280, 120, 120, 60])
smallfont = pygame.font.SysFont('Corbel',16) 
text2 = smallfont.render('Player White Will Win!' , True , "black")
display.blit(text2, (280 , 120))
pygame.display.update()

for event in pygame.event.get():    
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN :
            print("yo")










                    





font = pygame.font.Font(None, 48)
text = font.render(winner, True, "Black")
display.blit(text, (150, 40)) # where <x> and<y> are coordinates on screen
pygame.display.update()
 #the distance formula
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()



