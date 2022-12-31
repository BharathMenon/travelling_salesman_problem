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
    order_of_indices = [0] + list(range(len(cities)))[1::2] + list(
        range(len(cities)))[2::2]

    return order_of_indices
