"""
change speed for some paths
"""

import tkinter as tk
import tkinter.messagebox as mb
import random
import numpy

def random_distance():
    """
    return a random number for scales
    """
    match random.randint(0, 2):
        case 0:
            return 1
        case 1:
            return random.randint(1, 20)
        case 2:
            return 1/random.randint(1, 5)

def random_cities(cities):
    """
    return distances and scales filled with 50 random inputs
    """
    number_of_cities = 50
    for _ in range(number_of_cities):
        cities.append((random.randint(10, 490), random.randint(10, 490)))
    distances = numpy.array([[distance_between(start, end) for start in cities] for end in cities])
    scales = numpy.array([[random_distance() for _ in range(number_of_cities)] for __ in cities])
    return distances, scales

def distance_between(from_city, to_city):
    """
    calculates distance between two cities
    """
    distance = ((from_city[0] - to_city[0])**2 + (from_city[1] - to_city[1])**2)**0.5
    return distance

def get_city_distances(cities):
    """
    return distances and scales
    """
    def update_speed():
        """
        read tkinter input
        """
        input_city_2 = int(city2.get())
        input_city_1 = int(city1.get())
        if input_city_1 == input_city_2:
            return
        scale = float(input_scale.get())
        scales[input_city_1][input_city_2] = scale
        new_distances[input_city_1][input_city_2] = distances[input_city_1][input_city_2] / scale

    # initial distances
    distances = numpy.array([[distance_between(start, end) for start in cities] for end in cities])
    scales = numpy.array([[1] * len(cities)] * len(cities))
    window = tk.Tk()
    window.configure(bg="#313244")

    # exits if user does not want to change speeds
    if mb.askquestion(
            "Advanced Input",
            "Do You Want to Change Speeds For Specific Routes?") != "yes":
        window.destroy()
        return distances, scales
    new_distances = distances.copy()

    # make the window look cool
    window.geometry("500x500")
    title = tk.Label(text="ADVANCED DISTANCE SETTINGS",
                     bg="#313244",
                     fg="#a6adc8")
    title.pack()

    # dropdowns
    city1 = tk.StringVar()
    city1.set(0)
    drop1 = tk.OptionMenu(window, city1, *list(range(len(cities))))
    drop1.pack()

    city2 = tk.StringVar()
    city2.set(0)
    drop2 = tk.OptionMenu(window, city2, *list(range(len(cities))))
    drop2.pack()

    # scale
    label = tk.Label(text="SCALE", bg="#313244", fg="#a6adc8")
    label.pack()
    input_scale = tk.Entry()
    input_scale.pack()

    # button
    update = tk.Button(window, text="Update Speed", command=update_speed)
    update.pack()
    window.mainloop()
    return new_distances, scales
