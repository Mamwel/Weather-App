import tkinter as tk
import requests
from PIL import Image, ImageTk

HEIGHT = 500
WIDTH = 600

def format_response(weather):
    try:
        name = weather['name'] 
        desc = weather['weather'][0]['description']
        temp = weather['main']['temp']

        final_str = f'City: {name}\nConditions: {desc}\nTemperature: {temp}°'
    except:
        final_str = 'Please enter a valid\nCity Name'
    return final_str
 

def get_weather(city):
    key = '81edd21f93728e05866a6ac5b96c0e90'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': key, 'q': city, 'units': 'metric'}
    response = requests.get(url, params=params)
    weather = response.json()
    
    label['text'] = format_response(weather)

    
   
root = tk.Tk()

root.title('Weather App')

root.resizable(False, False)

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

bg_image = tk.PhotoImage(file='bg.png')
bg_label = tk.Label(root, image=bg_image)
bg_label.place(relwidth=1, relheight=1)


frame = tk.Frame(root, bg='#b3daff', bd=5)
frame.place(relx=.5, rely=.1, relwidth=.75, relheight=.1, anchor='n')

entry = tk.Entry(frame, font=18)
entry.place(relwidth=.65, relheight=1)

button = tk.Button(frame, text='How\'s the weather?', command=lambda: get_weather(entry.get()))
button.place(relx=.7, relheight=1, relwidth=.3)

lower_frame = tk.Frame(root, bg='#b3daff', bd=10)
lower_frame.place(relx=.5, rely=.25, relwidth=.75, relheight=.6, anchor='n')


label = tk.Label(lower_frame, text='label', font=('Verdana', 18))
label.place(relwidth=1, relheight=1)

root.mainloop()
 
