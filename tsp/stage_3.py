"""
animate solution
"""
import pygame

def draw_cities(screen, cities):
    """
    draws cities
    """
    for city in cities:
        pygame.draw.circle(screen, (248, 248, 242), city, 5)

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
    pygame.draw.lines(screen, (189, 147, 249), True, cities, 1)

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
    pygame.draw.rect(screen, (255, 121, 198), pygame.Rect(*map(lambda x: x - 5, position), 10, 10))
