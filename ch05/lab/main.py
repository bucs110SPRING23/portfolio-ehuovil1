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
    for n in range(2, upperlimit + 1):
        threenplus1_iters_dict[n] = threenp1(n) 
    return threenplus1_iters_dict

# Create a Pygame window
pygame.init()
screen = pygame.display.set_mode((500, 500))
pygame.display.update()

# Draw a line graph using the iterations from threenp1range()
graph_data = threenp1range(100)
max_iterations = max(graph_data.values())
max_key = max(graph_data, key=graph_data.get)

for key, value in graph_data.items():
    pygame.draw.line(screen, "white", (key, 500), (key, 500 - value), 1)

# Display the value with the maximum iterations on the graph
font = pygame.font.Font(None, 30)
text = font.render(f"Max Iterations: {max_iterations} (n = {max_key})", True, "white")
screen.blit(text, (10, 10))

# Update the display
pygame.display.update()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()