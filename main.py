from stage_1 import get_cities
from advanced_input import distance_between_cities
from stage_2 import travelling_salesman_problem

from stage_3 import draw_animation_background, draw_salesman
import pygame
from math import atan, sin, cos


def sign(n):
    if n < 0:
        return -1
    return 1


"""
stage -
1 -    get cities and distances
2 -    solve travelling salesman problem
3 -    animate salesman
4 -    exit
"""

# initialize pygame
pygame.init()

# pygame variables
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption('Enter Coordinates!')
font = pygame.font.Font(pygame.font.get_default_font(), 10)
clock = pygame.time.Clock()

cities = []
stage = 1

while True:

    screen.fill((40, 42, 54))

    # get distances and scales
    if stage == 1:
        distances, scales = get_cities(screen, cities, font)
        if distances != None:
            stage = 2

    # solve tsp and prepare for animation
    elif stage == 2:
        order_of_indices = travelling_salesman_problem(cities, distances)
        stage = 3

        # arrange cities by order of indices
        cities = list(map(lambda x: cities[x], order_of_indices))

        # initialize positions
        position = list(cities[0])
        from_position, to_position = cities[:2]
        to_index = 1

        # values for velocity
        delta_x = to_position[0] - from_position[0]
        delta_y = to_position[1] - from_position[1]
        angle = -(atan((delta_x) / (delta_y)))

    elif stage == 3:
        if draw_animation_background(screen, cities, scales) == -1:
            stage = 4

        # update values if salesman completes travel to city
        if distance_between_cities(from_position,
                                   position) > distance_between_cities(
                                       from_position, to_position):
            to_index = (to_index + 1) % len(cities)
            position = list(to_position)
            from_position, to_position = to_position, cities[to_index]
            delta_x = to_position[0] - from_position[0]
            delta_y = to_position[1] - from_position[1]
            angle = -(atan((delta_x) / (delta_y)))
            print(angle)

        draw_salesman(screen, position)

        position[0] -= sign(delta_y) * 4 * sin(angle) * scales[(from_position,
                                                                to_position)]
        position[1] += sign(delta_y) * 4 * cos(angle) * scales[(from_position,
                                                                to_position)]

    else:
        # for is the last stage, just like cancer
        pygame.quit()
        break
    pygame.display.update()
    clock.tick(30)
