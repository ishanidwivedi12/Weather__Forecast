from tkinter import *
import requests
import json
from tkinter.messagebox import showinfo

def get_weather_info():
    api_key = "1a684ff733b6f5c3ecb2a60271f6795e"
    city = city_entry.get()
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    res = requests.get(url)
    json_data = json.loads(res.text)

    weather = json_data["weather"][0]["description"]
    temperature = json_data["main"]["temp"]
    humidity = json_data["main"]["humidity"]
    wind_speed = json_data["wind"]["speed"]
    city_name = json_data["name"]
    country_name = json_data["sys"]["country"]

    showinfo(f'{city.title()} Weather', f'City Name: {city_name} \nCountry: {country_name} \nWeather: {weather} \nTemperature: {temperature}°C \nHumidity: {humidity}% \nWind speed: {wind_speed} m/s')

root = Tk()
root.title("Weather App")

app_label= Label(root, text="Weather App", font=("Times", 20, "bold"))
app_label.grid(row=0, column=0, columnspan=2)

city_label = Label(root, text="Enter city name:")
city_label.grid(row=1, column=0, columnspan=2)

city_entry = Entry(root, width=30)
city_entry.grid(row=1, column=2, pady=10)

btn = Button(root, text="Get Weather Info",  bd=1, command=get_weather_info)
btn.grid(row=2, column=0, columnspan=2, pady=10)

root.mainloop()
