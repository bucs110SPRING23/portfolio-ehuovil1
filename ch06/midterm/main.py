import pygame
import random
import turtle
def main():
#background
    pygame.init()
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    hugefont = pygame.font.SysFont('arial', 36)
    bigfont = pygame.font.SysFont('arial', 18)
    smallfont = pygame.font.SysFont('arial',12)
    screen = pygame.display.set_mode((600, 500))
    screen.fill(WHITE)
    pygame.display.set_caption("Rock Paper Scissors")

    #blits
    title = bigfont.render('Choose your weapon below', True, "black")
    screen.blit(title, (190, 15))



    rock = pygame.Rect(30, 60, 150, 60)
    paper = pygame.Rect(220, 60, 150, 60)
    scissors = pygame.Rect(420, 60, 150, 60)
    pygame.draw.rect(screen, "yellow", rock)
    pygame.draw.rect(screen, "green", paper)
    pygame.draw.rect(screen, "lightblue", scissors)

    text1 = hugefont.render('Rock' , True , "black")
    screen.blit(text1, (60 , 70))
    text2 = hugefont.render('Paper' , True , "black")
    screen.blit(text2, (245 , 70))
    text3 = hugefont.render('Scissors', True, "black")
    screen.blit(text3, (425, 70))
    pygame.display.update()



    #RPS
    cpuObject = 1
    cpuWins = 0
    userWins = 0
    ties = 0

    userRPS = 0
    go = 0

    for i in range(7):
        cpuObject = random.randint(1,3)
        pygame.event.clear()
        while True:
            event = pygame.event.wait()
            if event.type == pygame.QUIT:
                #go = 'no'
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if rock.collidepoint(mouse_pos):
                    userRPS = 1
                elif paper.collidepoint(mouse_pos):
                    userRPS = 2
                elif scissors.collidepoint(mouse_pos):
                    userRPS = 3

                if cpuObject == userRPS:
                    ties+=1
                    result = hugefont.render("It's a tie! " + str(userWins) + " - " + str(cpuWins), True , "black")
                    blank = pygame.Rect(125, 140, 350, 130)
                    pygame.time.wait(200)
                    pygame.draw.rect(screen, "white", blank)
                    pygame.display.update()
                    screen.blit(result, (195 , 210))
                    pygame.display.update()
                    break
                elif cpuObject == 1:
                    if userRPS == 2:
                        userWins+=1
                        result = hugefont.render('You won! ' + str(userWins) + " - " + str(cpuWins), True , "black")
                        blank = pygame.Rect(125, 140, 350, 130)
                        pygame.time.wait(200)
                        pygame.draw.rect(screen, "white", blank)
                        pygame.display.update()
                        screen.blit(result, (195 , 210))
                        pygame.display.update()
                        break
                    else:
                        cpuWins+=1
                        result = hugefont.render('You lost! ' + str(userWins) + " - " + str(cpuWins), True , "black")
                        blank = pygame.Rect(125, 140, 350, 130)
                        pygame.time.wait(200)
                        pygame.draw.rect(screen, "white", blank)
                        pygame.display.update()
                        screen.blit(result, (195 , 210))
                        pygame.display.update()
                        break
                elif cpuObject == 2:
                    if userRPS == 1:
                        cpuWins+=1
                        result = hugefont.render('You lost! ' + str(userWins) + " - " + str(cpuWins), True , "black")
                        blank = pygame.Rect(125, 140, 350, 130)
                        pygame.time.wait(200)
                        pygame.draw.rect(screen, "white", blank)
                        pygame.display.update()
                        screen.blit(result, (195 , 210))
                        pygame.display.update()
                        break
                    else:
                        userWins+=1
                        result = hugefont.render('You won! ' + str(userWins) + " - " + str(cpuWins), True , "black")
                        blank = pygame.Rect(125, 140, 350, 130)
                        pygame.time.wait(200)
                        pygame.draw.rect(screen, "white", blank)
                        pygame.display.update()
                        screen.blit(result, (195 , 210))
                        pygame.display.update()
                        break
                else:
                    if userRPS == 1:
                        userWins+=1
                        result = hugefont.render('You won! ' + str(userWins) + " - " + str(cpuWins), True , "black")
                        blank = pygame.Rect(125, 140, 350, 130)
                        pygame.time.wait(200)
                        pygame.draw.rect(screen, "white", blank)
                        pygame.display.update()
                        screen.blit(result, (195 , 210))
                        pygame.display.update()
                        break
                    else:
                        cpuWins+=1
                        result = hugefont.render('You lost! ' + str(userWins) + " - " + str(cpuWins), True , "black")
                        blank = pygame.Rect(125, 140, 350, 130)
                        pygame.time.wait(200)
                        pygame.draw.rect(screen, "white", blank)
                        pygame.display.update()
                        screen.blit(result, (195 , 210))
                        pygame.display.update()
                        break


    if cpuWins > userWins:
        winner = "Cpu"
    elif cpuWins < userWins:
        winner = "User"
    else:
        winner = "Tie"

    score1 = hugefont.render("Winner: " + str(winner), True, "black")
    score2 = hugefont.render("Cpu Wins: " + str(cpuWins), True, "black")
    score3 = hugefont.render("User Wins: " + str(userWins), True, "black")
    score4 = hugefont.render("Ties: " + str(ties), True, "black")
    pygame.draw.rect(screen, "white", blank)
    pygame.display.update()
    screen.blit(score1, (155 , 170))
    screen.blit(score2, (155 , 220))
    screen.blit(score3, (155 , 270))
    screen.blit(score4, (155 , 320))
    pygame.display.update()



    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    running = False



def turtle(x, y):
    import turtle
    erik = turtle.Turtle()
    erik.shape("turtle")
    for i in range(x):
        erik.color("purple")
        erik.forward(50)
        erik.left(y)
    turtle.delay(500)


x = int(input("Choose how many hikes u want the turtle to make: "))
y = int(input("What angle do you want the turtle to turn everytime?"))
turtle(x, y)
main()




