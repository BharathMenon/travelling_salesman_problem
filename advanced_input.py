import tkinter as tk
import tkinter.messagebox as mb

def distance_between_cities(a, b):
    distance = ((a[0] - b[0])**2 + (a[1] - b[1])**2)**0.5
    return distance

def get_city_distances(cities):
    def update_speed():
        c1 = cities[eval(city1.get())]
        c2 = cities[eval(city2.get())]
        if c1 == c2:    return
        scale = float(input_scale.get())
        scales[(c1, c2)] = scale
        new_distances[(c1, c2)] = distances[(c1, c2)] * scale
    
    # initial distances
    distances = {(a,b): distance_between_cities(a,b) for a in cities for b in cities if a != b}
    scales = {(a,b): 1 for a in cities for b in cities if a != b}
    
    window = tk.Tk()
    window.configure(bg="#282a36")

    # exits if user does not want to change speeds
    if mb.askquestion("Advanced Input", "Do You Want to Change Speeds For Specific Routes?") != "yes":
        window.destroy()
        return distances, scales

    new_distances = distances.copy()
    
    # make the window look cool
    window.geometry("500x500")
    title = tk.Label(text="ADVANCED DISTANCE SETTINGS", bg="#282a36", fg="#f8f8f2")
    title.pack()

    # dropdowns
    city1 = tk.StringVar()
    city1.set(cities[0])
    drop1 = tk.OptionMenu(window, city1, *list(range(len(cities))))
    drop1.pack()

    city2 = tk.StringVar()
    city2.set(cities[0])
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