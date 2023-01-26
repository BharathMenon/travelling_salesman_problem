import pygame
from pygame.locals import QUIT, KEYDOWN, K_ESCAPE

def draw_cities(screen, cities):
    for index, city in enumerate(cities):
        pygame.draw.circle(screen, (248, 248, 242), city, 5)

def handle_input(input, cities):
    if input.type == QUIT:
        return -1
    if input.type == KEYDOWN:
        if input.key == K_ESCAPE:
            return -1

def draw_path(screen, cities):
    pygame.draw.lines(screen, (189, 147, 249), True, cities, 1)

def draw_animation_background(screen, cities, scale):
    for event in pygame.event.get():
        if handle_input(event, cities) == -1:
            return -1
    draw_cities(screen, cities)
    draw_path(screen, cities)

def draw_salesman(screen, position):
    pygame.draw.rect(screen, (255, 121, 198), pygame.Rect(*map(lambda x: x - 5, position), 10, 10))