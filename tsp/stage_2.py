"""
solve the tsp
"""

from itertools import permutations
# from math import inf

def distance_of_path(path, distances):
    """
    calculates distance of a path
    """
    return sum(distances[path[i]][path[i+1]] for i in range(-1, len(path)-1))

def tsp_brute_force(cities, distances):
    """
    use brute force
    """
    permutations_of_cities = permutations(range(len(cities)))
    order_of_indices = min(permutations_of_cities, key = lambda x: distance_of_path(x, distances))
    return order_of_indices

# def travelling_salesman_problem_branch_and_bound(cities, distances):
#     """
#     use branch and bound bfs
#     """
#     return cities
