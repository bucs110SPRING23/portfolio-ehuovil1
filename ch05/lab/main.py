import pygame


def threenp1(n):
    count = 0
    while n > 1.0:
       count += 1
       if n % 2 == 0:
        n = int(n / 2)
       else:
        n = int(3 * n + 1)
    return count

def threenp1range(upperlimit):
    threenplus1_iters_dict = {}

    for n in range(2,upperlimit + 1):
        threenplus1_iters_dict[n] = threenp1(n) 
    return threenplus1_iters_dict

threenp1(100)
print(threenp1range(100).items())
print(threenp1(100))

screen = pygame.display.set_mode((500, 500))
pygame.display.update()
pygame.draw.lines(screen, "white", False, list(threenp1range(100).items()))
pygame.display.update()

new_display = pygame.transform.flip(display, False, True)
width, height = new_display.get_size()
new_display = pygame.transform.scale(new_display, (width * <factor>, height * <factor>))
display.blit(new_display, (0, 0))





running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()









