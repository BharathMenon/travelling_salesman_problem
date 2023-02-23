"""
animate solution
"""
import pygame

def draw_cities(screen, cities):
    """
    draws cities
    """
    for city in cities:
        pygame.draw.circle(screen, pygame.Color("#eba0ac"), city, 5)

def handle_input(keypress):
    """
    handles input
    """
    if keypress.type == 256:
        return -1
    if keypress.type == 768:
        if keypress.key == 27:
            return -1
    return None

def draw_path(screen, cities):
    """
    draws path
    """
    pygame.draw.lines(screen, pygame.Color("#f5e0dc"), True, cities, 1)

def draw_animation_background(screen, cities):
    """
    draws background
    """
    for event in pygame.event.get():
        if handle_input(event) == -1:
            return -1
    draw_cities(screen, cities)
    draw_path(screen, cities)
    return None

def draw_salesman(screen, position):
    """
    draws salesman
    """
    pygame.draw.rect(screen, pygame.Color("#cba6f7"), pygame.Rect(*map(lambda x: x - 7, position), 15, 15))
