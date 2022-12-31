import pygame
from pygame.locals import QUIT, KEYDOWN, K_ESCAPE
from stage_1 import draw_cities
def handle_input(input, cities):
    if input.type == QUIT:
        return -1
    if input.type == KEYDOWN:
        if input.key == K_ESCAPE:
            return -1
def draw_path(screen, cities):
    pygame.draw.lines(screen, (255, 121, 198), True, cities, 1)
def animate_salesman(screen, cities, scale, font):
    for event in pygame.event.get():
        if handle_input(event, cities) == -1:
            return -1
    draw_cities(screen, cities, font)
    draw_path(screen, cities)
