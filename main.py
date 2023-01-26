from stage_1 import get_cities
from advanced_input import distance_between_cities
from stage_2 import travelling_salesman_problem, travelling_salesman_problem_brute_force, travelling_salesman_problem_branch_and_bound
from stage_3 import draw_animation_background, draw_salesman
import pygame
import time
from math import atan, sin, cos, pi

"""
stage -
1 -    get cities and distances
2 -    solve travelling salesman problem
3 -    animate salesman
4 -    exit
"""

def sign(n):
    if n < 0:
        return -1
    return 1

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
        if len(distances) != 0:
            stage = 2

    # solve tsp and prepare for animation
    elif stage == 2:
        start = time.perf_counter()
        order_of_indices = travelling_salesman_problem_brute_force(cities, distances)
        end = time.perf_counter()
        print(end-start)
        stage = 3

        # arrange cities by order of indices
        cities = list(map(lambda x: cities[x], order_of_indices))
        
        # initialize positions
        position = list(cities[0])
        from_position, to_position = cities[:2]
        to_index = 1

        # values for velocity
        delta_x = to_position[0] - from_position[0]
        delta_y = (to_position[1] - from_position[1])
        if delta_x == 0:
            angle = sign(delta_y)*pi/2
        else:
            angle = (atan((delta_y) / (delta_x)))

    elif stage == 3:
        if draw_animation_background(screen, cities, scales) == -1:
            stage = 4

        # update values if salesman completes travel to city
        if distance_between_cities(from_position, position) > distance_between_cities(from_position, to_position):
            to_index = (to_index + 1) % len(cities)
            position = list(to_position)
            from_position, to_position = to_position, cities[to_index]
            delta_x = to_position[0] - from_position[0]
            delta_y = (to_position[1] - from_position[1])
            if delta_x == 0:
                angle = sign(delta_y)*pi/2
            else:
                angle = (atan((delta_y) / (delta_x)))

        draw_salesman(screen, position)

        position[0] += 4 * sign(delta_x) * cos(angle) * scales[to_index-1][to_index]
        position[1] += 4 * sign(delta_x) * sin(angle) * scales[to_index-1][to_index]

    else:
        # for is the last stage, just like cancer
        # after this you quit life
        pygame.quit()
        break
    pygame.display.update()
    clock.tick(30)
