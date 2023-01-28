"""
change speed for some paths
"""

import tkinter as tk
import tkinter.messagebox as mb
import numpy

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
    window.configure(bg="#282a36")

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
                     bg="#282a36",
                     fg="#f8f8f2")
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
    label = tk.Label(text="SCALE", bg="#282a36", fg="#f8f8f2")
    label.pack()
    input_scale = tk.Entry()
    input_scale.pack()

    # button
    update = tk.Button(window, text="Update Speed", command=update_speed)
    update.pack()
    window.mainloop()
    return new_distances, scales
