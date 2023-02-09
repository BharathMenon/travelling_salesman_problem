"""
input functions
"""
from tsp.advanced_input import distance_between
import pygame

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

def handle_input_city(keypress, cities):
    """
    handle input
    """
    if keypress.type == 1025:
        new_city = pygame.mouse.get_pos()
        if len(cities) == 0:
            cities.append(new_city)
            return None
        if min(map(lambda x: distance_between(x, new_city), cities)) <= 15:
            return None
        cities.append(new_city)
        return None
    return -1
