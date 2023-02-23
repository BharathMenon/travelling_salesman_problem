"""
get input
"""
import pygame
import numpy
from tsp.advanced_input import get_city_distances, distance_between

def draw_cities(screen, cities, font):
    """
    draw cities
    """
    for index, city in enumerate(cities):
        pygame.draw.circle(screen, pygame.Color("#eba0ac"), city, 5)
        text_surface = font.render(str(index), True, pygame.Color("#cdd6f4"))
        screen.blit(text_surface, dest=(city[0] - 3, city[1] - 15))

def handle_input(keypress, cities):
    """
    handle input
    """
    if keypress.type == 256:
        return -1
    if keypress.type == 768:
        if keypress.key == 27:
            return -1
    if keypress.type == 1025:
        new_city = pygame.mouse.get_pos()
        if len(cities) == 0:
            cities.append(new_city)
            return None
        if min(map(lambda x: distance_between(x, new_city),
                   cities)) <= 15:
            return None
        cities.append(new_city)
    return None

def get_cities(screen, cities, font):
    """
    get cities
    """
    for event in pygame.event.get():
        if handle_input(event, cities) == -1:
            distances, scales = get_city_distances(cities)
            return distances, scales
    draw_cities(screen, cities, font)
    return numpy.array([]), None
