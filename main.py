from stage_1 import get_cities
# from stage_2 import travelling_salesman_problem
# stage 2 is not ready so temporary function
def travelling_salesman_problem(cities, distances):
    order_of_indices = [0] + list(range(len(cities)))[1::2] + list(range(len(cities)))[2::2]
    return order_of_indices

from stage_3 import animate_salesman
import pygame

"""
stage -
1 -    get cities and distances
2 -    solve travelling salesman problem
3 -    animate salesman
4 -    exit
"""
pygame.init()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption('Enter Coordinates!')
cities = []
font = pygame.font.Font(pygame.font.get_default_font(), 10)
stage = 1
while True:
    if stage == 1:
        distances, scales = get_cities(screen, cities, font)
        if distances != None:
            stage = 2
            print(len(distances), len(cities), sep="\n")
            print(scales)
    elif stage == 2:
        order_of_indices = travelling_salesman_problem(cities, distances)
        stage = 3
        cities = list(map(lambda x: cities[x], order_of_indices))
        
    elif stage == 3:
        if animate_salesman(screen, cities, scales, font) == -1:
            stage = 4
    else:
        pygame.quit()
        break
    pygame.display.flip()