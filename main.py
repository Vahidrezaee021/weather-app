import tkinter as tk
from tkinter import messagebox
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz


def get_weather():
    pass
    

root = tk.Tk()
root.title("Weather App")
root.geometry("900x500+300+200")
root.resizable(False, False)

search_image = tk.PhotoImage(file="search.png")
search_image_lable = tk.Label(root, image=search_image)
search_image_lable.pack(pady=20, side=tk.TOP)


textfield = tk.Entry(root, justify="center", width=17, font=("poppins", 25, "bold"), bg="#404040", fg="white", border=0)
textfield.place(x=280, y=40)

search_icon = tk.PhotoImage(file="search_icon.png")
search_icon_button = tk.Button(root, image=search_icon, border=0, cursor="hand2", bg="#404040", command=get_weather)
search_icon_button.place(x=590, y=34)


logo_image = tk.PhotoImage(file="logo.png")
logo_label = tk.Label(root, image=logo_image)
logo_label.pack(side=tk.TOP)

frame_image = tk.PhotoImage(file="box.png")
frame_label = tk.Label(root, image=frame_image)
frame_label.pack(pady=10, side=tk.TOP)


city_lable = tk.Label(root, font=("arial", 40, "bold"), fg="#e355cd")
city_lable.place(x=120, y=160)

time_lable = tk.Label(root, font=("arial", 20, "bold"), fg="#4b4bcc")
time_lable.place(x=120, y=230)

clock = tk.Label(root, font=("Helvetica", 20), fg="#4b4bcc")
clock.place(x=120, y=270)

root.mainloop()