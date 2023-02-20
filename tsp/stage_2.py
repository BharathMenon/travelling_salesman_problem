"""
solve the tsp
"""

from itertools import permutations
from math import inf
from numpy import array

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

def tsp_branch_and_bound(cities, distances_original):
    """
    use branch and bound bfs
    """

    path = [0]
    from_index = 0
    
    # make city to itself = infinity
    distances = distances_original.copy()
    for i in range(len(cities)):
        distances[i,i] = inf

    def cost_of_reduction(distances, from_index, to_index):
        """
        calculates cost of reduction of matrix to a given path
        """
        distances = distances.copy()
        distances[from_index] = [inf]*len(distances)
        distances[:, to_index] = [inf]*len(distances)
        cost = distances_original[from_index, to_index]

        # rows
        for i in range(len(distances)):
            m = min(distances[i])
            if m == inf:    continue
            cost += m
            for j in range(len(distances[i])):
                distances[i, j] -= m
        
        # cols
        for i in range(len(distances)):
            m = min(distances[:, i])
            if m == inf:    continue
            cost += m
            for j in range(len(distances[:, i])):
                distances[j, i] -= m
        
        return (cost, distances)
    
    while len(path) < len(cities):
        m = inf
        md = []

        for to_index in range(len(distances)):
            if to_index in path:  continue
            cost, new_distances = cost_of_reduction(distances.copy(), from_index, to_index)
            if cost < m:
                m = cost
                md = new_distances
                mti = to_index

        distances = md
        path.append(mti)
        from_index = mti
        
        for i in path:
            distances[from_index, i] = inf

        print(distances)
    print(path)
    return path