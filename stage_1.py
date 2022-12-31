import pygame
from pygame.locals import QUIT, MOUSEBUTTONDOWN
from advanced_input import get_city_distances, distance_between_cities

def draw_city(screen, position, font, text):
    pygame.draw.circle(screen, (248, 248, 242), position, 5)
    text_surface = font.render(text, True, (248, 248, 242))
    screen.blit(text_surface, dest=(position[0]-3,position[1]-15))
def handle_input(input, cities):
    if input.type == QUIT:
        return -1
    if input.type == MOUSEBUTTONDOWN:
        new_city = pygame.mouse.get_pos()
        if len(cities) == 0:
            cities.append(new_city)
            return
        if min(map(lambda x : distance_between_cities(x, new_city), cities)) <= 15:
            return
        cities.append(new_city)
def get_cities(screen, cities, font):
    screen.fill((40, 42, 54))
    for event in pygame.event.get():
        if handle_input(event, cities) == -1:
            distances, scales = get_city_distances(cities)
            return screen, distances, scales
        else:
            continue
        break
    for index, city in enumerate(cities):
        draw_city(screen, city, font, str(index))
    return screen, None, None