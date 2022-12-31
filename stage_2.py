from itertools import permutations

def travelling_salesman_problem(cities, distances):
    # cities is a list
    # eg cities = [(2, 3), (4, 5)]
    # distances is a dictionary that contains distance for every combination of cities except city to itself
    # eg distances = {
    # ((2, 3), (4, 5)) : 10,
    # ((4, 5), (2, 3)) : 15
    # }
    # it doesnt contain ((2, 3), (2, 3))
    # key is a tuple of coordinates of both cites
    # if salesman travels from (2,3) to (4, 5) then distance is the key ((2, 3), (4, 5)) and value is 10
    # if salesman travels from (4, 5) to (2,3) then distance is the key ((4, 5), (2, 3)) and value is 15
    # value is distance
    # return a list indices
    # eg - return [0, 1] if shortest route is 0-1-0
    # dont return first index twice ( [ 0, 1 ] not [ 0, 1, 0 ] )
    # 1-0-1 is the same as 0-1-0 because it is a closed loop so [ 1, 0 ] is also valid but 0 is assumed starting point so prefer [ 0, 1 ]. it will be easier to animate

    # random order for testing purposes
    # TODO - solve the problem and find the real order
    order_of_indices = list(range(len(cities)))
    return order_of_indices

def travelling_salesman_problem_brute_force(cities, distances):
    order_of_indices = min(permutations(range(len(cities))), key = lambda x: sum(distances[(cities[x[i]], cities[x[i+1]])] for i in range(-1, len(cities) - 1)))
    return order_of_indices

from math import inf

def travelling_salesman_problem_branch_and_bound(cities, distances):
    num_cities = len(cities)
    
    # base case: if there is only one city, the shortest loop is just to stay there
    if num_cities == 1:
        return [0]
    
    # initialize the minimum distance to infinity
    min_distance = inf
    
    # initialize the list of cities to visit in the shortest loop to an empty list
    shortest_loop = []
    
    # iterate over all starting cities
    for start in range(num_cities):
        # initialize the current distance to the distance from the starting city to the first city in the loop
        curr_distance = distances[(cities[start], cities[(start + 1) % num_cities])]
        # initialize the list of cities visited in the current loop to the starting city and the first city
        curr_loop = [start, (start + 1) % num_cities]
        # initialize the set of remaining cities to all cities except the starting city and the first city
        remaining_cities = set(range(num_cities)) - {start, (start + 1) % num_cities}
        
        # recursive function to find the shortest loop starting from the current city
        def dfs(curr_distance, curr_loop, remaining_cities):
            nonlocal min_distance, shortest_loop
            
            # base case: if there are no more remaining cities, the current loop is complete
            # so we update the minimum distance and the shortest loop if necessary
            if not remaining_cities:
                if curr_distance < min_distance:
                    min_distance = curr_distance
                    shortest_loop = curr_loop[:]
                return
            
            # iterate over the remaining cities
            for next_city in remaining_cities:
                # calculate the distance from the current city to the next city
                next_distance = distances[(cities[curr_loop[-1]], cities[next_city])]
                # if the current distance + the distance to the next city is greater than the minimum distance,
                # we can skip the rest of the recursive calls because they will not result in a shorter loop
                if curr_distance + next_distance > min_distance:
                    continue
                # otherwise, we add the next city to the current loop and remove it from the remaining cities set
                curr_loop.append(next_city)
                remaining_cities.remove(next_city)
                # recursively call the function with the updated current distance and current loop
                dfs(curr_distance + next_distance, curr_loop, remaining_cities)
                # backtrack by adding the next city back to the remaining cities set and removing it from the current loop
                remaining_cities.add(next_city)
                curr_loop.pop()
        
        # call the recursive function to find the shortest loop starting from the current city
        dfs(curr_distance, curr_loop, remaining_cities)
    
    # return the shortest loop
    return shortest_loop
