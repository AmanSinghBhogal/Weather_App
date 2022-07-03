from tkinter import *
from PIL import Image,ImageTk
import json
import requests
import bs4      # bs stands for Beautify Soup

# key = e0cd284b1483a3eeb7e9bab60c55917f

app = Tk()
app.title("Weather")
app.iconbitmap("weather-news.ico")
app.geometry("500x500")

city = Entry(app,font=('Times',18),borderwidth=15,relief=FLAT)
city.place(x=80,y=30,width=300,height=50)
city.focus_set()

text1 = StringVar()
text2 = StringVar()
text3 = StringVar()
text4 = StringVar()

text1.set("")
text2.set("")
text3.set("")
text4.set("")

def get_weather():
    cityname = city.get()
    url = 'https://api.openweathermap.org/data/2.5/weather?q='+ cityname +'&appid=e0cd284b1483a3eeb7e9bab60c55917f'
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
    text4.set(str(dis))




search1 = Image.open('search.png')
search1 = search1.resize((30,30))
search1 = ImageTk.PhotoImage(search1)
search = Button(image=search1, borderwidth=0, cursor='hand2',command=get_weather)
search.place(x=390,y=40)

weatherLabel = Label(app, text='Temperature', font=('Times',15))
weatherLabel.place(x=60,y=100)
HumidityLabel = Label(app, text='Humidity', font=('Times',15))
HumidityLabel.place(x=220,y=100)

windLabel = Label(app, text='Wind', font=('Times',15))
windLabel.place(x=350,y=100)

temperature = Label(app, textvariable=text1, font=('Times',15))
temperature.place(x=90,y=130)

humidity = Label(app, textvariable=text2, font=('Times',15))
humidity.place(x=230,y=130)

windspeed = Label(app, textvariable=text3, font=('Times',15))
windspeed.place(x=355,y=130)

description = Label(app, textvariable=text4, font=('Times',15))
description.place(x=230,y=300)

app.mainloop()