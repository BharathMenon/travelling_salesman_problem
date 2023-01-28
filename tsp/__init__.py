"""
Animate the travelling salesman problem
"""
from math import atan, sin, cos, pi
import time
import pygame

from tsp.stage_1 import get_cities
from tsp.advanced_input import distance_between
from tsp.stage_2 import tsp_brute_force
from tsp.stage_3 import draw_animation_background, draw_salesman

# stage -
# 1 -    get cities and distances
# 2 -    solve travelling salesman problem
# 3 -    animate salesman
# 4 -    exit

# initialize pygame

pygame.init()

# pygame variables
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption('Enter Coordinates!')
font = pygame.font.Font(pygame.font.get_default_font(), 10)
CLOCK = pygame.time.Clock()

def sign(number):
    """
    return sign of number
    """
    if number < 0:
        return -1
    return 1

def stage_1(cities):
    """
    stage 1
    """
    distances, scales = get_cities(screen, cities, font)
    if len(distances) != 0:
        return distances, scales
    return None, None

def overshot(from_pos, cur_pos, to_pos):
    """
    if salesman has completed journey
    """
    return distance_between(from_pos,cur_pos) > distance_between(from_pos, to_pos)

def move_salesman(salesman_position, delta_x, angle, scale):
    """
    moves salesman
    """
    salesman_position[0] += 4 * sign(delta_x) * cos(angle) * scale
    salesman_position[1] += 4 * sign(delta_x) * sin(angle) * scale

def run():
    """
    run everything
    """

    cities = []

    stage = 1

    while True:

        screen.fill((40, 42, 54))

        # get distances and scales
        if stage == 1:
            distances, scales = stage_1(cities)
            if distances is not None:
                stage = 2

        # solve tsp and prepare for animation
        elif stage == 2:
            start = time.perf_counter()
            order_of_indices = tsp_brute_force(cities, distances)
            end = time.perf_counter()
            print(end-start)

            # arrange cities by order of indices
            cities = list(map(lambda x: cities[x], order_of_indices))

            # initializesalesman_positions
            salesman_position = list(cities[0])
            from_position, to_position = cities[:2]
            to_index = 1

            # values for velocity
            delta_x = to_position[0] - from_position[0]
            delta_y = (to_position[1] - from_position[1])
            if delta_x == 0:
                angle = sign(delta_y)*pi/2
            else:
                angle = (atan((delta_y) / (delta_x)))

            stage = 3

        elif stage == 3:
            if draw_animation_background(screen, cities) == -1:
                stage = 4

            # update values if salesman completes travel to city
            if overshot(from_position,salesman_position, to_position):
                to_index = (to_index + 1) % len(cities)
                salesman_position = list(to_position)
                from_position, to_position = to_position, cities[to_index]
                delta_x = to_position[0] - from_position[0]
                delta_y = (to_position[1] - from_position[1])
                if delta_x == 0:
                    angle = sign(delta_y)*pi/2
                else:
                    angle = (atan((delta_y) / (delta_x)))

            draw_salesman(screen,salesman_position)
            scale = scales[order_of_indices[to_index-1]][order_of_indices[to_index]]
            move_salesman(salesman_position, delta_x, angle, scale)

        else:
            # for is the last stage, just like cancer
            # after this you quit life
            pygame.quit()
            break
        pygame.display.update()
        CLOCK.tick(30)
