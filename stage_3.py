def handle_input(input, cities):
    if input.type == QUIT:
        return -1
    if input.type == MOUSEBUTTONDOWN:
        new_city = pygame.mouse.get_pos()
        if len(cities) == 0:
            cities.append(new_city)
            return
        if min(map(lambda x : distance_between_cities(x, new_city), cities)) <= 15:
            return
        cities.append(new_city)
def animate_salesman(cities, order_of_indices, scale):
    cities = list(map(lambda x: cities[x], order_of_indices))
    for event in pygame.event.get():
        if handle_input(event, cities) == -1:
            return -1
    first_index = 