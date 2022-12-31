import pygame
from pygame.locals import QUIT, MOUSEBUTTONDOWN, KEYDOWN, K_ESCAPE
from advanced_input import get_city_distances, distance_between_cities


def draw_cities(screen, cities, font):
    for index, city in enumerate(cities):
        pygame.draw.circle(screen, (248, 248, 242), city, 5)
        text_surface = font.render(str(index), True, (248, 248, 242))
        screen.blit(text_surface, dest=(city[0] - 3, city[1] - 15))


def handle_input(input, cities):
    if input.type == QUIT:
        return -1
    if input.type == KEYDOWN:
        if input.key == K_ESCAPE:
            return -1
    if input.type == MOUSEBUTTONDOWN:
        new_city = pygame.mouse.get_pos()
        if len(cities) == 0:
            cities.append(new_city)
            return
        if min(map(lambda x: distance_between_cities(x, new_city),
                   cities)) <= 15:
            return
        cities.append(new_city)


def get_cities(screen, cities, font):
    for event in pygame.event.get():
        if handle_input(event, cities) == -1:
            distances, scales = get_city_distances(cities)
            return distances, scales
        else:
            continue
        break
    draw_cities(screen, cities, font)
    return None, None
