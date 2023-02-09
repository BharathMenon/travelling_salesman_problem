"""
get input
"""
import pygame
import numpy
from tsp.advanced_input import get_city_distances, distance_between
from tsp.input_functions import handle_input_city, handle_input

def draw_cities(screen, cities, font):
    """
    draw cities
    """
    for index, city in enumerate(cities):
        pygame.draw.circle(screen, (248, 248, 242), city, 5)
        text_surface = font.render(str(index), True, (248, 248, 242))
        screen.blit(text_surface, dest=(city[0] - 3, city[1] - 15))

def get_cities(screen, cities, font):
    """
    get cities
    """
    for event in pygame.event.get():
        if handle_input(event) == -1:
            distances, scales = get_city_distances(cities)
            return distances, scales
        handle_input_city(event, cities)
    draw_cities(screen, cities, font)
    return numpy.array([]), None
