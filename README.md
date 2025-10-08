# 🌦️ Weather App (Python + Tkinter)

This is a simple **Weather Application** built using **Python** and **Tkinter** for the graphical user interface.  
The app allows users to search for any city and get real-time weather information using the **OpenWeatherMap API**.  

It displays details such as:
- 🌍 City name and local time (based on timezone)
- 🌡️ Temperature and "feels like" condition
- 💨 Wind speed
- 💧 Humidity level
- ☁️ Weather description
- 🧭 Atmospheric pressure

## 🛠️ Technologies Used
- **Python 3**
- **Tkinter**
- **Geopy**
- **TimezoneFinder**
- **Pytz**
- **Requests**

## ⚙️ How It Works
1. The user enters the name of a city.  
2. The app uses **Geopy** to find the city’s coordinates.  
3. With **TimezoneFinder** and **Pytz**, it calculates the local time.  
4. It then requests weather data from the **OpenWeatherMap API**.  
5. Finally, the results are displayed in a stylish Tkinter interface.

## 🔑 API Requirement
You need an **OpenWeatherMap API key**.  
Replace this line with your own key:
```python
api_key = "YOUR_API_KEY"
