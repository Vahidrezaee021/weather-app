import tkinter as tk
from tkinter import messagebox
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz



root = tk.Tk()
root.title("Weather App")
root.geometry("900x500+300+200")
root.resizable(False, False)

search_image = tk.PhotoImage(file="search.png")
search_image_lable = tk.Label(root, image=search_image)
search_image_lable.pack(pady=20, side=tk.TOP)

root.mainloop()