import pygame
pygame.init()

# Set up the window
window_size = (400, 400)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Button Click")

# Set up the buttons
button_font = pygame.font.SysFont("arial", 20)
button_padding = 20
button_width = 150
button_height = 50
button1_text = button_font.render("Button 1", True, (255, 255, 255))
button2_text = button_font.render("Button 2", True, (255, 255, 255))
button1_rect = pygame.Rect(
    button_padding, window_size[1] / 2 - button_height / 2, button_width, button_height
)
button2_rect = pygame.Rect(
    window_size[0] - button_padding - button_width,
    window_size[1] / 2 - button_height / 2,
    button_width,
    button_height,
)

# Start the game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if button1_rect.collidepoint(mouse_pos):
                choice = "Button 1"
                button1_rect = pygame.Rect(0, 0, 0, 0)
                button2_rect = pygame.Rect(0, 0, 0, 0)
            elif button2_rect.collidepoint(mouse_pos):
                choice = "Button 2"
                button1_rect = pygame.Rect(0, 0, 0, 0)
                button2_rect = pygame.Rect(0, 0, 0, 0)

    # Draw the buttons
    screen.fill((0, 0, 0))
    screen.blit(
        button1_text, (button1_rect.centerx - button1_text.get_width() / 2, button1_rect.centery - button1_text.get_height() / 2)
    )
    screen.blit(
        button2_text, (button2_rect.centerx - button2_text.get_width() / 2, button2_rect.centery - button2_text.get_height() / 2)
    )

    # Update the display
    pygame.display.update()