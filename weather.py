from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import messagebox
from datetime import datetime
import requests

root = Tk()
root.title("Weather App")
root.geometry("900x500+300+200")
root.resizable(False, False)

WEATHERAPI_KEY = "3d25d46fe8ea4e2dae2162934240601"

def get_weather():
    try:
        city = textfield.get()

        geolocator = Nominatim(user_agent="geoapiExercises")
        location = geolocator.geocode(city)

        if location is None:
            raise ValueError("Location not found")

        home = datetime.now()
        current_time = home.strftime("%I:%M %p")
        clock.config(text=current_time)
        name.config(text=f"Weather in {city}")

        # Use WeatherAPI for current weather
        current_api = f"http://api.weatherapi.com/v1/current.json?key={WEATHERAPI_KEY}&q={city}"
        current_json_data = requests.get(current_api).json()

        # Extract relevant data from WeatherAPI response for current weather
        temp = current_json_data.get('current', {}).get('temp_c')
        wind_speed = current_json_data.get('current', {}).get('wind_kph')
        humidity = current_json_data.get('current', {}).get('humidity')
        pressure = current_json_data.get('current', {}).get('pressure_mb')
        description = current_json_data.get('current', {}).get('condition', {}).get('text')

        # Update the labels with current weather information
        t.config(text=f"{temp}°C")
        w.config(text=wind_speed)
        h.config(text=humidity)
        d.config(text=description)
        p.config(text=pressure)

        # Use WeatherAPI for future forecast (next 3 days)
        forecast_api = f"http://api.weatherapi.com/v1/forecast.json?key={WEATHERAPI_KEY}&q={city}&days=3"
        forecast_json_data = requests.get(forecast_api).json()

        # Extract relevant data from WeatherAPI response for forecast
        forecast_data = forecast_json_data.get('forecast', {}).get('forecastday', [])

        # Display the forecast for the next 3 days
        forecast_text = "\n".join([f"{day['date']}: {day['day']['avgtemp_c']}°C, {day['day']['condition']['text']}" for day in forecast_data])
        future_weather.config(text=forecast_text)

    except Exception as e:
        print(f"Error: {str(e)}")
        messagebox.showerror("Weather App", f"Error: {str(e)}")

       
Search_image = PhotoImage(file="search.png")
myimage = Label(image=Search_image)
myimage.place(x=20, y=20)
 
textfield = tk.Entry(root, justify="center", width=17, font=("poppins", 25, "bold"), bg="#404040", border=0, fg="white")
textfield.place(x=50, y=40)
textfield.focus()

Search_icon = PhotoImage(file="search_icon.png")
myimage_icon = Button(image=Search_icon, borderwidth=0, cursor="hand2", bg="#404040", command=get_weather)
myimage_icon.place(x=400, y=34)

# logo
Logo_image = PhotoImage(file="logo.png")
logo = Label(image=Logo_image)
logo.place(x=150, y=100)

# Bottom box
Frame_image = PhotoImage(file="box.png")
frame_myimage = Label(image=Frame_image)
frame_myimage.pack(padx=5, pady=5, side=BOTTOM)

# time
name = Label(root, font=("arial", 15, "bold"))
name.place(x=30, y=100)
clock = Label(root, font=("Helvetica", 20))
clock.place(x=30, y=130)

# Label
label1 = Label(root, text="WIND", font=("Helvetica", 15, 'bold'), fg="white", bg="#1ab5ef")
label1.place(x=120, y=400)

label2 = Label(root, text="HUMIDITY", font=("Helvetica", 15, 'bold'), fg="white", bg="#1ab5ef")
label2.place(x=250, y=400)

label3 = Label(root, text="DESCRIPTION", font=("Helvetica", 15, 'bold'), fg="white", bg="#1ab5ef")
label3.place(x=430, y=400)

label4 = Label(root, text="PRESSURE", font=("Helvetica", 15, 'bold'), fg="white", bg="#1ab5ef")
label4.place(x=650, y=400)

t = Label(font=("arial", 70, "bold"), fg="#ee666d")
t.place(x=400, y=150)
c = Label(font=("arial", 15, 'bold'))
c.place(x=400, y=250)

w = Label(text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
w.place(x=120, y=430)
h = Label(text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
h.place(x=280, y=430)
d = Label(text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
d.place(x=450, y=430)
p = Label(text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
p.place(x=670, y=430)

future_weather = Label(root, text="", font=("Arial", 12))
future_weather.place(x=550, y=250)

root.mainloop()