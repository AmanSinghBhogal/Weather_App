from tkinter import *
from PIL import Image,ImageTk
import json
import requests
import bs4      # bs stands for Beautify Soup
from decouple import config

app = Tk()
app.title("Weather")
app.iconbitmap("weather-news.ico")
app.geometry("500x500")

col1=60
col2=220
col3=350

row1 = 10
row2 = 90
row3 = 150
row4=180
row5=350


city = Entry(app,font=('Times',18),borderwidth=15,relief=FLAT)
city.place(x=80,y=row2,width=300,height=50)
city.focus_set()

text1 = StringVar()
text2 = StringVar()
text3 = StringVar()
text4 = StringVar()

text1.set("")
text2.set("")
text3.set("")
text4.set("")

Key = config('API_KEY')

def get_weather():
    cityname = city.get()
    url = 'https://api.openweathermap.org/data/2.5/weather?q='+ cityname +'&appid='+Key
    # Grabs the content from the URL:
    html = requests.get(url)

    # Creates a soup object that contains parsed content
    soup = bs4.BeautifulSoup(html.text, "html.parser")

    # parses the json object and deserializes it into a parsed string
    data = json.loads(soup.text)

    temp = data["main"]["temp"] - 273.15
    humid = data["main"]["humidity"]
    wind = data["wind"]["speed"]
    dis = data["weather"][0]["description"]
    temp = "{:.2f}".format(temp)
    humid = "{:.2f}".format(humid)
    wind = "{:.2f}".format(wind)

    text1.set(temp)
    text2.set(humid)
    text3.set(wind)
    text4.set(str(dis).upper())

weathernews1 = Image.open('weather-news.ico')
weathernews1 = weathernews1.resize((50,50))
weathernews1 = ImageTk.PhotoImage(weathernews1)
weathernews = Label(image=weathernews1, cursor='hand2')
weathernews.place(x=col2,y=row1)


search1 = Image.open('search.png')
search1 = search1.resize((40,40))
search1 = ImageTk.PhotoImage(search1)
search = Button(image=search1, borderwidth=0, cursor='hand2',command=get_weather)
search.place(x=390,y=row2+5)

weatherLabel = Label(app, text='Temperature', font=('Times',15))
weatherLabel.place(x=60,y=row3)
HumidityLabel = Label(app, text='Humidity', font=('Times',15))
HumidityLabel.place(x=220,y=row3)

windLabel = Label(app, text='Wind', font=('Times',15))
windLabel.place(x=350,y=row3)

temperature = Label(app, textvariable=text1, font=('Times',15))
temperature.place(x=90,y=row4)

humidity = Label(app, textvariable=text2, font=('Times',15))
humidity.place(x=230,y=row4)

windspeed = Label(app, textvariable=text3, font=('Times',15))
windspeed.place(x=355,y=row4)

description = Label(app, textvariable=text4, font=('Times',15))
description.place(x=col2-50,y=row5)

app.mainloop()