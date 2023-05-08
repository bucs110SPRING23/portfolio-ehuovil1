import random
import pygame

pygame.init()
screen = pygame.display.set_mode()

width,height = pygame.display.get_window_size()

hit_box_width = width / 2 #half the screen
hit_box_height = height / 2
#2 halves make quarter

hitboxes = {
    "red": pygame.Rect(0, 0, hit_box_width, hit_box_height),
    "green" : pygame.Rect(0, 0, hit_box_width, hit_box_height),
    "blue" : pygame.Rect(0, 0, hit_box_width, hit_box_height),
    "purple" : pygame.Rect(0, 0, hit_box_width, hit_box_height),
}

#position hitboxes
hitboxes["blue"].topleft = hitboxes["red"].topright
hitboxes["green"].topright = hitboxes["red"].bottomright
hitboxes["purple"].topleft = hitboxes["red"].bottomright
hitboxes["purple"].width = 1000000


main_colors = {
    "red": (255, 0, 0),
    "green": (0, 200, 0),
    "blue": (0, 0, 200),
    "purple" : (200, 0, 200),
}

