import tkinter as tk
from tkinter import messagebox
import requests
import time


def weatherFromOpenWeather(output):
    cityinput=cityname.get()
    apiweather= "http://api.openweathermap.org/data/2.5/weather?q="+ cityinput +"&appid=7797679fcd7f009c4fcebd04cbee6e09"
    jsondata=requests.get(apiweather).json()
    overallweather=jsondata['weather'][0]['main']
    get_temp=int(jsondata['main']['temp']-273.15)

    show=overallweather+"\n"+str(get_temp)+" °C"
    label.config(text=show)



output = tk.Tk()
output.geometry("300x300")
output.title("WeatherAPI")
output.configure(bg="grey")
t = ("calibri", 30, "bold")

cityname =tk.Entry(output, justify='center', font = t)
cityname.pack(pady = 40)
cityname.bind('<Return>', weatherFromOpenWeather)

label =tk.Label(output, font=t)
label.pack()
output.mainloop()