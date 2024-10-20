from customtkinter import *
import datetime
from tkinter import messagebox
from PIL import Image, ImageTk
import os
import requests

def GUI():
    # Defining the Dimention of Window
    set_appearance_mode('light')
    app = CTk()
    app.geometry("500x700")
    app.title("weatherOcast")

    def get_weather(*args):
        city_name_ = city_name.get()
        api_key = "4c109b5b48df125851afa36b5b671fa5"
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name_}&appid={api_key}&units=metric"
        response = requests.get(url)
        weather_data = response.json()
        
        if weather_data["cod"] == 200:
            location = weather_data["name"]
            description = weather_data["weather"][0]["main"]
            temp = weather_data["main"]["temp"]
            fell_like = weather_data["main"]["feels_like"]
            pressure = weather_data["main"]["pressure"]
            humidity = weather_data["main"]["humidity"]
            wind_speed = weather_data["wind"]["speed"]
            country = weather_data["sys"]["country"]
            sunrise = weather_data["sys"]["sunrise"]
            sunrise_cf = datetime.datetime.fromtimestamp(sunrise)
            sunrise_time = sunrise_cf.strftime("%H:%M:%S")
            sunset = weather_data["sys"]["sunset"]
            sunset_cf = datetime.datetime.fromtimestamp(sunset)
            sunset_time = sunset_cf.strftime("%H:%M:%S")

            # configuring all the labels to show data on the GUI
            place_name.configure(text=location)
            temp_label.configure(text=f"Temperature:     {temp}°C")
            fell_like_temp_label.configure(text=f" Fells Like: {fell_like}°C")
            pressure_label.configure(text=f"Pressure: {pressure} mbar")
            humidity_label.configure(text=f"Humidity: {humidity} %")
            wind_speed_label.configure(text=f"Wind SP: {wind_speed} KMPH")
            sunrise_label.configure(text=f"Sunrise: {sunrise_time}")
            sunset_label.configure(text=f"Sunset:  {sunset_time}")
            country_label.configure(text=f"Country: {country}")

            if description == "Clouds":
                description_label.configure(image=cloudy_img)
                desc_info_label.configure(text="Clouds")
            elif description == "Mist":
                description_label.configure(image=mist_img)
                desc_info_label.configure(text="Mist")
            elif description == "Clear":
                description_label.configure(image=clear_img)
                desc_info_label.configure(text="Clear")
            elif description == "Thunderstorm":
                description_label.configure(image=thunderstorm_img)
                desc_info_label.configure(text="Thunderstorm")
            elif description == "Haze":
                description_label.configure(image=haze_img)
                desc_info_label.configure(text="Haze")
            elif description == "Rain":
                description_label.configure(image=rain_img)
                desc_info_label.configure(text="Rain")
            elif description == "Drizzle":
                description_label.configure(image=drizzle_img)
                desc_info_label.configure(text="Drizzle")
            elif description == "Overcast":
                description_label.configure(image=overcast_img)
                desc_info_label.configure(text="Overcast")
            elif description == "Snow":
                description_label.configure(image=snow_img)
                desc_info_label.configure(text="Snow")
            elif description == "Fog":
                description_label.configure(image=fog_img)
                desc_info_label.configure(text="Fog")
            elif description == "Dust":
                description_label.configure(image=dust_img)
                desc_info_label.configure(text="Dust")
               
        else:
            temp_label.destroy()
            app.after(100, lambda: fell_like_temp_label.destroy())
            app.after(200, lambda: pressure_label.destroy())
            app.after(300, lambda: humidity_label.destroy())
            app.after(400, lambda: wind_speed_label.destroy())
            app.after(500, lambda: sunrise_label.destroy())
            app.after(600, lambda: sunset_label.destroy())
            app.after(700, lambda: country_label.destroy())
            app.after(800, lambda: desc_info_label.destroy())
            app.after(900, lambda: description_label.destroy())
            Error_label = CTkLabel(master=app,
                                   text=f"Oops {city_name_} is not a city",
                                   text_color="black",
                                   font=("Roboto Bold", 30, "italic"))
            Error_label.place(relx=0.5, rely=0.5, anchor='center')

            messagebox.showerror("City Error", f"{city_name_} is not a city")
            app.destroy()
            GUI()

    # File/Image to be used in the project
    file_path = os.path.dirname(os.path.realpath(__file__))
    snow_img = CTkImage(Image.open(r"C:\Users\Dhruv Gupta\Desktop\APP\Python\weather\snow.png"), size=(48, 48))
    search_img = CTkImage(Image.open(r"C:\Users\Dhruv Gupta\Desktop\APP\Python\weather\Search.png"))
    location_img = CTkImage(Image.open(r"C:\Users\Dhruv Gupta\Desktop\APP\Python\weather\location.png"), size=(40, 40))
    world_img = CTkImage(Image.open(r"C:\Users\Dhruv Gupta\Desktop\APP\Python\weather\world.png"))
    temp_img = CTkImage(Image.open(r"C:\Users\Dhruv Gupta\Desktop\APP\Python\weather\temperature.png"), size=(48, 48))
    fell_like_img = CTkImage(Image.open(r"C:\Users\Dhruv Gupta\Desktop\APP\Python\weather\fell_like1.png"), size=(40, 40))
    pressure_img = CTkImage(Image.open(r"C:\Users\Dhruv Gupta\Desktop\APP\Python\weather\atmosphere_Pressure.png"), size=(40, 40))
    humidity_img = CTkImage(Image.open(r"C:\Users\Dhruv Gupta\Desktop\APP\Python\weather\humidity.png"), size=(40, 40))
    wind_speed_img = CTkImage(Image.open(r"C:\Users\Dhruv Gupta\Desktop\APP\Python\weather\wind_speed.png"), size=(40, 40))
    sunrise_img = CTkImage(Image.open(r"C:\Users\Dhruv Gupta\Desktop\APP\Python\weather\sunrise.png"), size=(40, 40))
    sunset_img = CTkImage(Image.open(r"C:\Users\Dhruv Gupta\Desktop\APP\Python\weather\sunset.png"), size=(40, 40))
    country_img = CTkImage(Image.open(r"C:\Users\Dhruv Gupta\Desktop\APP\Python\weather\world.png"), size=(40, 40))
    weather_img = CTkImage(Image.open(r"C:\Users\Dhruv Gupta\Desktop\APP\Python\weather\weather.png"), size=(50, 50))
    clear_img = CTkImage(Image.open(r"C:\Users\Dhruv Gupta\Desktop\APP\Python\weather\clear.png"), size=(100, 100))
    partly_cloud_img = CTkImage(Image.open(r"C:\Users\Dhruv Gupta\Desktop\APP\Python\weather\partly_clouds.png"), size=(100, 100))
    cloudy_img = CTkImage(Image.open(r"C:\Users\Dhruv Gupta\Desktop\APP\Python\weather\clouds.png"), size=(100, 100))
    overcast_img = CTkImage(Image.open(r"C:\Users\Dhruv Gupta\Desktop\APP\Python\weather\overcast.png"), size=(100, 100))
    rain_img = CTkImage(Image.open(r"C:\Users\Dhruv Gupta\Desktop\APP\Python\weather\rain.png"), size=(100, 100))
    drizzle_img = CTkImage(Image.open(r"C:\Users\Dhruv Gupta\Desktop\APP\Python\weather\drizzle.png"), size=(100, 100))
    thunderstorm_img = CTkImage(Image.open(r"C:\Users\Dhruv Gupta\Desktop\APP\Python\weather\thunderstorm.png"), size=(100, 100))
    snow_img = CTkImage(Image.open(r"C:\Users\Dhruv Gupta\Desktop\APP\Python\weather\snow.png"), size=(100, 100))
    fog_img = CTkImage(Image.open(r"C:\Users\Dhruv Gupta\Desktop\APP\Python\weather\fog.png"), size=(100, 100))
    mist_img = CTkImage(Image.open(r"C:\Users\Dhruv Gupta\Desktop\APP\Python\weather\mist.png"), size=(100, 100))
    dust_img = CTkImage(Image.open(r"C:\Users\Dhruv Gupta\Desktop\APP\Python\weather\dust.png"), size=(100, 100))
    haze_img = CTkImage(Image.open(r"C:\Users\Dhruv Gupta\Desktop\APP\Python\weather\haze.png"), size=(100, 100))

    app_logo_label = CTkLabel(master=app,
                              text="",
                              image=weather_img,
                              compound="left")
    app_logo_label.place(relx=0.02, rely=0.01)
    date = datetime.datetime.now()
    today_date = date.strftime("%d-%m-%Y")
    date_label = CTkLabel(master=app,
                          text=today_date,
                          font=("Georgia", 17, "bold"),
                          compound="center")
    date_label.place(relx=0.75, rely=0.02)

    weekname_label = CTkLabel(master=app,
                              text=date.strftime("%A"),
                              font=("AHINOS", 17, "bold"))
    weekname_label.place(relx=0.8, rely=0.06)

    city_name = CTkEntry(master=app,
                         height=40,
                         width=450,
                         corner_radius=12,
                         border_color="green",
                         border_width=2,
                         fg_color="transparent",
                         placeholder_text="Enter your City",
                         placeholder_text_color="green",
                         font=("Roboto", 18, "bold"),
                         text_color="green")
    city_name.place(relx=0.5, rely=0.8, anchor=CENTER)
    city_name.bind('<Return>', get_weather)

    button = CTkButton(master=app,
                       height=40,
                       width=300,
                       fg_color="#2FA4B5",
                       corner_radius=9,
                       font=("Roboto", 18, "bold"),
                       text="Search",
                       image=search_img,
                       compound="right",
                       command=get_weather
                       )
    button.place(relx=0.5, rely=0.9, anchor=CENTER)
    place_name = CTkLabel(master=app,
                          height=75,
                          width=200,
                          text="",
                          corner_radius=9,
                          text_color="black",
                          font=("Roboto Bold", 25, "bold"),
                          image=location_img,
                          compound="left")
    place_name.place(relx=0.5, rely=0.05, anchor=CENTER)

    temp_label = CTkLabel(master=app,
                          height=30,
                          width=75,
                          text="Temp:",
                          image=temp_img,
                          compound="left",
                          text_color="black",
                          font=("Roboto Bold", 22, "bold"))
    temp_label.place(relx=0.02, rely=0.15)
    fell_like_temp_label = CTkLabel(master=app,
                                    height=30,
                                    width=75,
                                    text="Fells Like:",
                                    text_color="black",
                                    image=fell_like_img,
                                    compound="left",
                                    font=("Roboto Bold", 22, "bold"))
    fell_like_temp_label.place(relx=0.02, rely=0.25)

    pressure_label = CTkLabel(master=app,
                              text="Pressure:",
                              text_color="black",
                              font=("Roboto Bolld", 22, "bold"),
                              image=pressure_img,
                              compound="left",
                              height=30,
                              width=70)
    pressure_label.place(relx=0.02, rely=0.32)

    humidity_label = CTkLabel(master=app,
                              height=30,
                              width=70,
                              text="Humidity:",
                              text_color="black",
                              font=("Roboto Bold", 22, "bold"),
                              image=humidity_img,
                              compound="left")
    humidity_label.place(relx=0.02, rely=0.4)

    wind_speed_label = CTkLabel(master=app,
                                height=30,
                                width=70,
                                text="Wind Sp:",
                                text_color="black",
                                font=("Roboto Bold", 22, "bold"),
                                compound="left",
                                image=wind_speed_img)
    wind_speed_label.place(relx=0.02, rely=0.48)

    sunrise_label = CTkLabel(master=app,
                             height=30,
                             width=70,
                             text="Sunrise:",
                             text_color="black",
                             font=("Roboto Bold", 22, "bold"),
                             image=sunrise_img,
                             compound="left")
    sunrise_label.place(relx=0.02, rely=0.56)

    sunset_label = CTkLabel(master=app,
                            height=30,
                            width=70,
                            text="Sunset:",
                            text_color="black",
                            font=("Roboto Bold", 22, "bold"),
                            image=sunset_img,
                            compound="left")
    sunset_label.place(relx=0.02, rely=0.64)

    country_label = CTkLabel(master=app,
                             text="Country:",
                             text_color="black",
                             font=("Roboto", 22, "bold"),
                             image=country_img,
                             compound="left")
    country_label.place(relx=0.02, rely=0.70)

    description_label = CTkLabel(master=app,
                                 text="",
                                 image=None,
                                 compound="center")
    description_label.place(relx=0.65, rely=0.2)

    desc_info_label = CTkLabel(master=app,
                               text="",
                               text_color="#4AAEBC",
                               font=("Georgia", 25, "bold"),
                               corner_radius=9)
    desc_info_label.place(relx=0.65, rely=0.4)

    app.mainloop()


if __name__ == "__main__":
    GUI()
