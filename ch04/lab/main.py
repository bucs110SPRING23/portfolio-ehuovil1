import random
import math
import pygame


## 5. Your PART A code goes here
#background
pygame.init()

screen_width=500
screen_height=500
screen=pygame.display.set_mode([screen_width, screen_height])
display = pygame.display.set_mode((500, 500))
pygame.time.wait(200)
display.fill("light blue")
pygame.display.update()
pygame.draw.circle(display, "red", [250, 250], 250)
pygame.draw.line(display, "black", [250, 0], [250, 500])
pygame.draw.line(display, "black", [0, 250], [500, 250])
pygame.display.update()
pygame.time.wait(200)



rect_1 = pygame.Rect(90, 120, 120, 60)
rect_2 = pygame.Rect(280, 120, 120, 60)
pygame.display.update()

#Player Green Will Win!
color_dark = (100,100,100)

go = 'yes'

while True :
    #Player Green Will Win!
    pygame.draw.rect(display, "green", rect_1)
    smallfont = pygame.font.SysFont("arial",10) 
    text1 = smallfont.render('Player Green Will Win!' , True , "black")
    display.blit(text1, (90 , 120))
    pygame.display.update()

    #Player White Will Win!
    pygame.draw.rect(display, "white", rect_2)
    smallfont = pygame.font.SysFont("arial",10) 
    text2 = smallfont.render('Player White Will Win!' , True , "black")
    display.blit(text2, (280 , 120))
    pygame.display.update()

    button1_rect = pygame.Rect(90, 120, 120, 60)
    button2_rect = pygame.Rect(280, 120, 120, 60)


    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if button1_rect.collidepoint(mouse_pos):
                    choice = "Green Wins"
                    go = 'no'
                elif button2_rect.collidepoint(mouse_pos):
                    choice = "White Wins"
                    go = 'no'
    if go == 'no':
        break

display.fill("light blue")
pygame.display.update()
pygame.draw.circle(display, "red", [250, 250], 250)
pygame.draw.line(display, "black", [250, 0], [250, 500])
pygame.draw.line(display, "black", [0, 250], [500, 250])
pygame.display.update()

#inside

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
        pygame.draw.circle(screen, "green", [xCord, yCord], 5)
        pygame.display.update()
        green +=1
    else:
        pygame.draw.circle(screen, "black", [xCord, yCord], 5)
        pygame.display.update()   

for i in range(10):
    xCord = random.randrange(0, 500)
    yCord = random.randrange(0, 500)
    distance_from_center = math.hypot(xCord - 250,yCord - 250)
    if distance_from_center <= 250:
        pygame.draw.circle(screen, "white", [xCord, yCord], 5)
        pygame.display.update()
        white +=1
    else:
        pygame.draw.circle(screen, "black", [xCord, yCord], 5)
        pygame.display.update()   
print(green)
print(white)
if green > white:
    winner = "Green Wins!"
    print
elif green < white:
    winner = "White Wins!"
else:
    winner = "It's a Tie!"

font = pygame.font.SysFont("arial", 40)
text = font.render(winner, True, "Black")
display.blit(text, (140, 40)) # where <x> and<y> are coordinates on screen
pygame.display.update()

if choice == "Green Wins" and green > white:
    result = smallfont.render('You guessed correctly!' , True , "black")
    display.blit(result, (180 , 120))
    pygame.display.update()
elif choice == "Green Wins" and green == white:
    result = smallfont.render('You guessed incorrectly!' , True , "black")
    display.blit(result, (180 , 120))
    pygame.display.update()
elif choice == "Green Wins" and green < white:
    result = smallfont.render('You guessed incorrectly!' , True , "black")
    display.blit(result, (180 , 120))
    pygame.display.update()
elif choice == "White Wins" and green > white:
    result = smallfont.render('You guessed incorrectly!' , True , "black")
    display.blit(result, (180 , 120))
    pygame.display.update()
elif choice == "White Wins" and green < white:
    result = smallfont.render('You guessed correctly!' , True , "black")
    display.blit(result, (180 , 120))
    pygame.display.update()
elif choice == "White Wins" and green == white:
    result = smallfont.render('You guessed incorrectly!' , True , "black")
    display.blit(result, (180 , 120))
    pygame.display.update()

    pygame.display.update()
running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()



