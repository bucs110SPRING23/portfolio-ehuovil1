import pygame
display = pygame.display.set_mode((600, 400))
pygame.draw.circle(display, "white", [300, 100], 40)
pygame.display.update()
pygame.draw.circle(display, "white", [300, 180], 60)
pygame.display.update()
pygame.draw.circle(display, "white", [300, 290], 90)
pygame.display.update()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
