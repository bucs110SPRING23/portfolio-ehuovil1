import pygame
from src.ball import Ball

class Controller:
    def __init__(self)
        pygame.init

        self.screen = pygame.display.set.mode()

        self.ball = Ball(self.width / 2, self.height / 2, 100)
        self.sprites = pygame.sprite.Group



def mainloop(self):


    while True:
            if self.state == "GAME"


def endloop():
    font_obj = pygame.font.SysFont(None, 48)
    msg = font_obj.render("You Won!", True, "yellow")

    while self.state == "END":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            self.screen.blit(msg, [50, 50])


def gameloop(self):
        
    while self.state == "GAME"

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.ball.rect.collidepoint(event.pos):
                    pygame.quit()
                    exit()
        
        self.sprites.update()

        if self.ball.rect.x < 0:
            self.ball.direction = "right"
        elif self.ball.rect.x > (self.width - self.ball.rect.width):
            self.ball.direction = "left"


                