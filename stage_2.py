from itertools import permutations

def travelling_salesman_problem(cities, distances):
    # cities is a list
    # eg cities = [(2, 3), (4, 5)]
    # distances is a 2d list that contains distance for every combination of cities
    # eg distances = [
    # [0 1 2],
    # [3 0 3],
    # [2 3 0],
    # ]
    # if salesman travels from 0 to 1 then distance is distances[0][1] and value is 1
    # if salesman travels from 1 to 0 then distance is the key [1][0] and value is 3
    # return a list indices
    # eg - return [0, 1] if shortest route is 0-1-0
    # dont return first index twice ( [ 0, 1 ] not [ 0, 1, 0 ] )
    # 1-0-1 is the same as 0-1-0 because it is a closed loop so [ 1, 0 ] is also valid but 0 is assumed starting point so prefer [ 0, 1 ]. it will be easier to animate

    # random order for testing purposes
    # TODO - solve the problem and find the real order
    order_of_indices = list(range(len(cities)))
    return order_of_indices

def travelling_salesman_problem_brute_force(cities, distances):
    order_of_indices = min(permutations(range(len(cities))), key = lambda x: sum(distances[x[i]][x[i+1]] for i in range(-1, len(cities) - 1)))
    return order_of_indices

from math import inf

def travelling_salesman_problem_branch_and_bound(cities, distances):
    pass