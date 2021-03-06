from tkinter import *
from PIL import Image,ImageTk
import json
import requests
import bs4      # bs stands for Beautify Soup
from decouple import config

app = Tk()
app.title("Weather")
app.iconbitmap("./images/weather-news.ico")
app.geometry("500x500")
app.resizable(False,False)

col1=60
col2=220
col3=350

row1 = 10
row2 = 90
row3 = 170
row4=200
row5= 280
row6=350


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
    humid = "{:.1f}".format(humid)
    wind = "{:.2f}".format(wind)

    text1.set(temp+" °C")
    text2.set(humid + " %")
    text3.set(wind + " km/h")
    upper_desc = dis.upper()
    center = upper_desc.center(35," ")
    text4.set(center)

    global weatherDes

    if(dis == "clear sky" or dis == "few clouds"):
        weatherDes = Image.open(r'./images/clear-sky.png')
    elif dis == "overcast clouds" or dis == "scattered clouds":
        weatherDes = Image.open(r'./images/cloudy.png')
    elif dis == "broken clouds":
        weatherDes = Image.open(r'./images/broken clouds.png')
    elif dis == "shower rain" or dis == "rain":
        weatherDes = Image.open(r'./images/rain.png')
    elif dis == "thunderstorm":
        weatherDes = Image.open(r'./images/storm.png')
    elif dis == "snow":
        weatherDes = Image.open(r'./images/snow.png')
    elif dis == "mist" or dis == "haze":
        weatherDes = Image.open(r'./images/mist.png')
    else:    
        weatherDes = Image.open(r'./images/oops.png')

    weatherDes = weatherDes.resize((70,70))
    weatherDes = ImageTk.PhotoImage(weatherDes)
    global DesImg 
    DesImg= Label(image=weatherDes)
    DesImg.place(x=col2,y=row5)

def detectKey(e):
    if(e.keycode == 13):
        get_weather()

app.bind("<KeyPress>", detectKey)

weathernews1 = Image.open('./images/weather-news.ico')
weathernews1 = weathernews1.resize((50,50))
weathernews1 = ImageTk.PhotoImage(weathernews1)
weathernews = Label(image=weathernews1, cursor='hand2')
weathernews.place(x=col2,y=row1)


search1 = Image.open('./images/search.png')
search1 = search1.resize((40,40))
search1 = ImageTk.PhotoImage(search1)
search = Button(image=search1, borderwidth=0, cursor='hand2',command=get_weather)
search.pack()
search.place(x=390,y=row2+5)

temper1 = Image.open('./images/hot.png')
temper1 = temper1.resize((30,30))
temper1 = ImageTk.PhotoImage(temper1)
temper = Label(image=temper1, cursor='hand2')
temper.place(x=30,y=row3)
weatherLabel = Label(app, text='Temperature', font=('Times',18))
weatherLabel.place(x=60,y=row3)

humi1 = Image.open('./images/humidity.png')
humi1 = humi1.resize((30,30))
humi1 = ImageTk.PhotoImage(humi1)
humi = Label(image=humi1, cursor='hand2')
humi.place(x=198,y=row3)
HumidityLabel = Label(app, text='Humidity', font=('Times',18))
HumidityLabel.place(x=235,y=row3)

windi1 = Image.open('./images/wind.png')
windi1 = windi1.resize((30,30))
windi1 = ImageTk.PhotoImage(windi1)
windi = Label(image=windi1, cursor='hand2')
windi.place(x=340,y=row3)
windLabel = Label(app, text='Wind', font=('Times',18))
windLabel.place(x=370,y=row3)

temperature = Label(app, textvariable=text1, font=('Times',18))
temperature.place(x=70,y=row4)

humidity = Label(app, textvariable=text2, font=('Times',18))
humidity.place(x=240,y=row4)

windspeed = Label(app, textvariable=text3, font=('Times',18))
windspeed.place(x=355,y=row4)

description = Label(app, textvariable=text4, font=('Times',18))
description.place(x=col1+45,y=row6)

app.mainloop()