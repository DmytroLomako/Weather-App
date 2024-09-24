import PIL.Image
import PIL.ImageTk
from requests import get
from customtkinter import *
import PIL
import os
import json
from deep_translator import GoogleTranslator
from datetime import datetime

translator = GoogleTranslator(source = 'auto', target = 'uk')
api = 

main_map = True
path_to_json = os.path.abspath(__file__ + '/../save.json')

user_country = None
user_city = None
user_name = None
user_surname = None
def sign_up_save(frame_auth, country_name_entry, city_name_entry, name_entry, surname_entry, label_user_text):
    global main_map, user_country, user_city, user_name, user_surname
    user_country = country_name_entry.get()
    user_city = city_name_entry.get()
    user_name = name_entry.get()
    user_surname = surname_entry.get()
    label_user_text.configure(text = f'{user_name} {user_surname}')
    url = f'https://api.openweathermap.org/data/2.5/weather?q={user_city}&appid={api}'
    answer = get(url)
    if answer.status_code == 200:
        if user_country != '' and user_city != '' and user_name != '' and user_surname != '':
            frame_auth.destroy()
            main_map = True
            load_weather()
            with open(path_to_json, 'w')as file:
                json.dump({'country': user_country, 'city': user_city, 'name': user_name, 'surname': user_surname}, file, indent = 4, ensure_ascii = False)
    else:
        city_name_entry.configure(border_color = 'red')

if os.path.exists(path_to_json):
    with open(path_to_json, 'r') as file:
        data = json.load(file)
        user_country = data['country']
        user_city = data['city']
        user_name = data['name']
        user_surname = data['surname']
def exit_account(label_user_text, frame):
    global user_country, user_name, user_surname, user_city
    user_country = None
    user_city = None
    user_name = None
    user_surname = None
    label_user_text.configure(text = 'Зареєструйтесь')
    frame.destroy()
    os.remove(path_to_json)

list_weather_time = []
list_weather_temp = []
list_weather_icon = []
url = f'https://api.openweathermap.org/data/2.5/forecast?q={user_city}&appid={api}'
answer = get(url)
if answer.status_code == 200:
    data = answer.json()
    temp = data['list'][0]['main']['temp'] - 273.15
    temp = round(temp, 1)
    icon = data['list'][0]['weather'][0]['icon']
    feels_like = round(data['list'][0]['main']['feels_like'] - 273.15, 1)
    wind_speed = data['list'][0]['wind']['speed']
    humidity = data['list'][0]['main']['humidity']
    weather_description_main = data['list'][0]['weather'][0]['main'].title()
    weather_desription = data['list'][0]['weather'][0]['description'].title()
    time = data['list'][0]['dt_txt'].split(' ')[0]
    month = time.split('-')[1]
    day = time.split('-')[2]
    year = time.split('-')[0].split('20')[1]
    dt_txt = 'dt_txt'
    for dt_txt in data['list']:
        list_weather_time.append(dt_txt['dt_txt'].split(' ')[1].split(':')[0])
        list_weather_temp.append(round(dt_txt['main']['temp'] - 273.15, 1))
        list_weather_icon.append(dt_txt['weather'][0]['icon'])
    # date_time = data['list'][]
app = CTk()
app.title('Weather App')
app.geometry('1200x800')
frame_city_select = CTkFrame(app, 275, 800, fg_color = '#096C82')
frame_city_select.place(x = 0, y = 0)
frame_weather = CTkFrame(app, 925, 800, fg_color = '#5DA7B1', border_color = '#096C82', border_width = 5)
frame_weather.place(x = 275, y = 0)
frame_user = CTkFrame(app, fg_color = '#5DA7B1', corner_radius = 0)
path_image = os.path.abspath(__file__ + '/../weather/user.png')
image = PIL.Image.open(path_image)
image = image.resize([64, 50])
image = PIL.ImageTk.PhotoImage(image)
label_user = CTkLabel(frame_user, image = image, text = '')
label_user_text = CTkLabel(frame_user, text = f'{user_name} {user_surname}', font = ('Arial', 20), text_color = 'white')
if user_name == None:
    label_user_text.configure(text = 'Зареєструйтесь')
frame_user.place(x = 320, y = 30)
label_user.grid(row = 0, column = 0)
label_user_text.grid(row = 0, column = 1, padx = 5)
search_entry = CTkEntry(frame_weather, font = ('Arial', 22), width = 238, height = 46, placeholder_text = 'Пошук', corner_radius = 20, fg_color = '#096C82', border_color = '#b5d3d9', border_width = 3)
search_entry.place(x = 645, y = 45)
path_image3 = os.path.abspath(__file__ + '/../weather/loope.png')
image3 = PIL.Image.open(path_image3)
image3 = image3.resize([42, 33])
image3 = PIL.ImageTk.PhotoImage(image3)
search_loope = CTkLabel(frame_weather, image = image3, text = '', bg_color = '#096C82')
search_loope.place(x = 831, y = 51)
frame_current_position = CTkFrame(frame_weather, 315, 275, fg_color = '#5DA7B1')
frame_current_position.place(x = 300, y = 120)
weekdays = ['Понеділок', 'Вівторок', 'Середа', 'Четвер', "П'ятниця", 'Субота', 'Неділя']
def load_weather():
    global current_city_text, current_temp_text, weather_desription, current_description_text, list_first_hours_temp, list_first_hours_time, current_time_func, current_city_select_text, range_count, right_arrow, current_description_select_text, current_temp_select_text, max_temp, min_temp, current_city_select_max_temp_text, weather_description_main, list_weather_icon2, current_max_temp, current_weather_description, current_image, list_weather_icon, city_name
    current_position_text = CTkLabel(frame_current_position, text = 'Поточна позиція', font = ('Arial', 35), text_color = 'white')
    current_position_text.grid(row = 0, column = 0, pady = 10)
    current_city_text = CTkLabel(frame_current_position, text = user_city, font = ('Arial', 22), text_color = 'white')
    current_city_text.grid(row = 1, column = 0, pady = 10)
    current_temp_text = CTkLabel(frame_current_position, text = f'{temp}°', font = ('Arial', 48), text_color = 'white')
    current_temp_text.grid(row = 2, column = 0, pady = 10)
    path_to_image = os.path.abspath(__file__ + f'/../weather/{icon}.png')
    if not os.path.exists(path_to_image):
        path_to_image = os.path.abspath(__file__ + f'/../weather/01d.png')
        print('Не знайдено картинку', list_weather_icon[0])
    image = PIL.Image.open(path_to_image)
    image = image.resize([180, 180])
    image = PIL.ImageTk.PhotoImage(image)
    current_image = CTkLabel(frame_weather, image = image, text = '')
    current_image.place(x = 75, y = 180)
    weather_desription = translator.translate(weather_desription)
    weather_description_main = translator.translate(weather_description_main).title()
    current_description_text = CTkLabel(frame_current_position, text = weather_description_main, font = ('Arial', 22), text_color = 'white')
    current_description_text.grid(row = 3, column = 0, pady = 10)
    current_time = CTkLabel(frame_weather, text = f'{day}.{month}.{year}', font = ('Arial', 40), text_color = 'white')
    current_time.place(x = 665, y = 240)
    frame_hourly_weather_main = CTkFrame(frame_weather, 785, 250, fg_color = '#5DA7B1', border_color = '#b5d3d9', border_width = 5, corner_radius = 20)
    frame_hourly_weather_main.place(x = 70, y = 430)
    frame_hourly_weather = CTkFrame(frame_hourly_weather_main, 20, 240, fg_color = 'transparent')
    frame_hourly_weather.place(x = 20, y = 70)
    top_line = CTkFrame(frame_hourly_weather_main, 764, 2, fg_color = '#b5d3d9')
    top_line.place(x = 18, y = 50)
    current_weather_description = CTkLabel(frame_hourly_weather_main, text = f'{weather_desription}', font = ('Arial', 20), text_color = 'white')
    current_weather_description.place(x = 30, y = 20)
    range_count = [0, 1, 2, 3, 4, 5, 6, 7]
    def right_arrow_func(event):
        global range_count, list_first_hours_temp, list_first_hours_time, right_arrow, list_weather_temp, list_weather_icon_path
        if range_count[7] == 39:
            return False
        left_arrow.configure(text_color = 'white')
        range_count.append(range_count[7] + 1)
        del range_count[0]
        j = 0
        for i in range_count:
            list_first_hours_time[j].configure(text = f'{list_weather_time[i]}:00')
            list_first_hours_temp[j].configure(text = f'{list_weather_temp[i]}°')
            path_to_image = os.path.abspath(__file__ + f'/../weather/{list_weather_icon[i]}.png')
            try:
                if list_weather_icon_path != None:
                    path_to_image = list_weather_icon_path[i]
            except:
                pass
            if not os.path.exists(path_to_image):
                path_to_image = os.path.abspath(__file__ + f'/../weather/01d.png')
                print('Не знайдено картинку', list_weather_icon[0])
            image = PIL.Image.open(path_to_image)
            image = image.resize([50, 50])
            image = PIL.ImageTk.PhotoImage(image)
            list_weather_icon2[j].configure(image = image)
            j += 1
        if range_count[7] == 39:
            right_arrow.configure(text_color = '#a0bcbd')
    def left_arrow_func(event):
        global range_count, list_first_hours_temp, list_first_hours_time, right_arrow, list_weather_temp, list_weather_icon_path
        if range_count[0] == 0:
            return False
        right_arrow.configure(text_color = 'white')
        range_count.insert(0, range_count[0] - 1)
        del range_count[8]
        j = 0
        for i in range_count:
            list_first_hours_time[j].configure(text = f'{list_weather_time[i]}:00')
            list_first_hours_temp[j].configure(text = f'{list_weather_temp[i]}°')
            path_to_image = os.path.abspath(__file__ + f'/../weather/{list_weather_icon[i]}.png')
            try:
                if list_weather_icon_path != None:
                    path_to_image = list_weather_icon_path[i]
            except:
                pass
            if not os.path.exists(path_to_image):
                path_to_image = os.path.abspath(__file__ + f'/../weather/01d.png')
                print('Не знайдено картинку', list_weather_icon[0])
            image = PIL.Image.open(path_to_image)
            image = image.resize([50, 50])
            image = PIL.ImageTk.PhotoImage(image)
            list_weather_icon2[j].configure(image = image)
            j += 1
        if range_count[0] == 0:
            left_arrow.configure(text_color = '#a0bcbd')
    right_arrow = CTkLabel(frame_weather, text = '>', font = ('Arial', 50), text_color = 'white')
    right_arrow.place(x = 875, y = 550)
    right_arrow.bind('<Button-1>', right_arrow_func)
    left_arrow = CTkLabel(frame_weather, text = '<', font = ('Arial', 50), text_color = '#a0bcbd')
    left_arrow.place(x = 20, y = 550)
    left_arrow.bind('<Button-1>', left_arrow_func)
    weekday_text = CTkLabel(frame_weather, text = weekdays[datetime.now().weekday()], font = ('Arial', 24), text_color = 'white')
    weekday_text.place(x = 700, y = 200)
    list_first_hours_temp = []
    list_first_hours_time = []
    list_weather_icon2 = []
    for i in range(8):
        first_hours_time = CTkLabel(frame_hourly_weather, text = f'{list_weather_time[i]}:00', font = ('Arial', 18), text_color = 'white')
        first_hours_time.grid(row = 0, column = i, pady = 10, padx = 10)
        list_first_hours_time.append(first_hours_time)
        path_to_image = os.path.abspath(__file__ + f'/../weather/{list_weather_icon[i]}.png')
        if not os.path.exists(path_to_image):
            path_to_image = os.path.abspath(__file__ + f'/../weather/01d.png')
            print('Не знайдено картинку', list_weather_icon[0])
        image = PIL.Image.open(path_to_image)
        image = image.resize([50, 50])
        image = PIL.ImageTk.PhotoImage(image)
        label_image = CTkLabel(frame_hourly_weather, image = image, text = '')
        label_image.grid(row = 1, column = i, pady = 10, padx = 16)
        list_weather_icon2.append(label_image)
        first_hours_temp = CTkLabel(frame_hourly_weather, text = f'{list_weather_temp[i]}°', font = ('Arial', 26), text_color = 'white')
        first_hours_temp.grid(row = 2, column = i, pady = 10, padx = 16)
        list_first_hours_temp.append(first_hours_temp)
    list_weather_max_min_temp = []
    for i in range(8):
        list_weather_max_min_temp.append(list_weather_temp[i])
    max_temp = str(max(list_weather_max_min_temp)).split('.')[0]
    min_temp = str(min(list_weather_max_min_temp)).split('.')[0]
    path_image_arrow_up = os.path.abspath(__file__ + '/../weather/arrow_up.png')
    image_arrow_up = PIL.Image.open(path_image_arrow_up)
    image_arrow_up = image_arrow_up.resize([28, 33])
    image_arrow_up = PIL.ImageTk.PhotoImage(image_arrow_up)
    path_image_arrow_down = os.path.abspath(__file__ + '/../weather/arrow_down.png')
    image_arrow_down = PIL.Image.open(path_image_arrow_down)
    image_arrow_down = image_arrow_down.resize([28, 33])
    image_arrow_down = PIL.ImageTk.PhotoImage(image_arrow_down)
    current_max_temp = CTkLabel(frame_weather, text = f'{min_temp}°          {max_temp}°', font = ('Arial', 30), text_color = 'white')
    current_max_temp.place(x = 370, y = 360)
    arrow_up = CTkLabel(frame_weather, image = image_arrow_up, text = '', font = ('Arial', 30), text_color = 'white')
    arrow_up.place(x = 460, y = 360)
    arrow_down = CTkLabel(frame_weather, image = image_arrow_down, text = '', font = ('Arial', 30), text_color = 'white')
    arrow_down.place(x = 330, y = 360)
    def current_time_func():
        app.after(1000, current_time_func)
        current_time_now = str(datetime.now()).split('.')[0].split(' ')[1]
        current_time_now_text = CTkLabel(frame_weather, text = current_time_now.split('.')[0], font = ('Arial', 30), text_color = 'white')
        current_time_now_text.place(x = 677, y = 300)
    current_time_func()
    frame_current_city = CTkFrame(frame_city_select, 235, 100, fg_color = '#5DA7B1', border_color = '#b5d3d9', border_width = 5, corner_radius = 20)
    frame_current_city.place(x = 20, y = 30)
    current_city_position_text = CTkLabel(frame_current_city, text = 'Поточна позиція', font = ('Arial', 16), text_color = 'white')
    current_city_position_text.place(x = 14, y = 8)
    current_city_select_text = CTkLabel(frame_current_city, text = user_city, font = ('Arial', 12), text_color = 'white')
    current_city_select_text.place(x = 15, y = 30)
    current_temp_select_text = CTkLabel(frame_current_city, text = f'{str(temp).split('.')[0]}°', font = ('Arial', 50), text_color = 'white')
    current_temp_select_text.place(x = 150, y = 10)
    current_description_select_text = CTkLabel(frame_current_city, text = weather_desription, font = ('Arial', 13), text_color = 'white')
    current_description_select_text.place(x = 14, y = 55)
    current_city_select_max_temp_text = CTkLabel(frame_current_city, text = f'макс: {max_temp}°, мін: {min_temp}°', font = ('Arial', 12), text_color = 'white')
    current_city_select_max_temp_text.place(x = 120, y = 65)

    class Sidebar_City:
        def __init__(self, name, row):
            self.name = name
            self.row = row
        def sidebar_city_func(self):
            self.frame = CTkFrame(frame_city_select, 235, 100, fg_color = '#096C82', border_color = '#b5d3d9', border_width = 5, corner_radius = 20)
            self.frame.place(x = 20, y = 160 + 130 * (self.row - 1))
            self.city_name = CTkLabel(self.frame, text = self.name, font = ('Arial', 16), text_color = 'white')
            self.city_name.place(x = 14, y = 8)
            url_city = f'https://api.openweathermap.org/data/2.5/forecast?q={self.name}&appid={api}'
            answer_city = get(url_city)
            data_city = answer_city.json()
            temp_city = data_city['list'][0]['main']['temp'] - 273.15
            description_city = data_city['list'][0]['weather'][0]['description']
            description_city = translator.translate(description_city).title()
            self.city_temp_text = CTkLabel(self.frame, text = f'{str(temp_city).split('.')[0]}°', font = ('Arial', 50), text_color = 'white')
            self.city_temp_text.place(x = 150, y = 10)
            self.city_description_text = CTkLabel(self.frame, text = description_city, font = ('Arial', 13), text_color = 'white')
            self.city_description_text.place(x = 14, y = 55)
            list_weather_temp_city = []
            dt_txt = 'dt_txt'
            for dt_txt in data_city['list']:
                list_weather_temp_city.append((round(dt_txt['main']['temp'] - 273.15, 1)))
            list_weather_max_min_temp_city = []
            for i in range(8):
                list_weather_max_min_temp_city.append(list_weather_temp_city[i])
            city_max_temp = str(max(list_weather_max_min_temp_city)).split('.')[0]
            city_min_temp = str(min(list_weather_max_min_temp_city)).split('.')[0]
            self.city_max_min_temp_text = CTkLabel(self.frame, text = f'max: {city_max_temp}°, min: {city_min_temp}°', font = ('Arial', 12), text_color = 'white')
            self.city_max_min_temp_text.place(x = 120, y = 65)
        def click_city(self, event):
            global user_city_search, search_city, user_city, temp, weather_desription, max_temp, min_temp
            self.city_name.configure(text = user_city)
            self.city_temp_text.configure(text = f'{str(temp).split('.')[0]}°')
            self.city_description_text.configure(text = weather_desription)
            self.city_max_min_temp_text.configure(text = f'max: {max_temp}°, min: {min_temp}°')
            user_city_search = self.name
            search_city(None)
    kyiv = Sidebar_City('Kyiv', 1)
    kyiv.sidebar_city_func()
    kyiv.frame.bind('<Button-1>', kyiv.click_city)
    kyiv.city_temp_text.bind('<Button-1>', kyiv.click_city)
    
    rome = Sidebar_City('Rome', 2)
    rome.sidebar_city_func()
    rome.frame.bind('<Button-1>', rome.click_city)
    rome.city_temp_text.bind('<Button-1>', rome.click_city)
    
    paris = Sidebar_City('Paris', 3)
    paris.sidebar_city_func()
    paris.frame.bind('<Button-1>', paris.click_city)
    paris.city_temp_text.bind('<Button-1>', paris.click_city)
    
    london = Sidebar_City('London', 4)
    london.sidebar_city_func()
    london.frame.bind('<Button-1>', london.click_city)
    london.city_temp_text.bind('<Button-1>', london.click_city)
    
    new_york = Sidebar_City('New York', 5)
    new_york.sidebar_city_func()
    new_york.frame.bind('<Button-1>', new_york.click_city)
    new_york.city_temp_text.bind('<Button-1>', new_york.click_city)

if user_name != None:
    load_weather()
    app.after(1000, current_time_func)
user_city_search = ''
def search_city(event):
    global user_city_search, temp, feels_like, wind_speed, humidity, weather_desription, current_city_text, current_temp_text, range_count, max_temp, min_temp, list_weather_temp, list_weather_icon, list_weather_time, list_weather_icon_path, user_city
    if event != None:
        user_city_search = search_entry.get()
    user_city = user_city_search
    url = f'https://api.openweathermap.org/data/2.5/forecast?q={user_city_search}&appid={api}'
    answer = get(url)
    if answer.status_code == 200:
        range_count = [0, 1, 2, 3, 4, 5, 6, 7]
        data = answer.json()
        temp = data['list'][0]['main']['temp'] - 273.15
        temp = round(temp, 1)
        icon = data['list'][0]['weather'][0]['icon']
        feels_like = round(data['list'][0]['main']['feels_like'] - 273.15, 1)
        wind_speed = data['list'][0]['wind']['speed']
        humidity = data['list'][0]['main']['humidity']
        weather_description_main = data['list'][0]['weather'][0]['main'].title()
        weather_desription = data['list'][0]['weather'][0]['description'].title()
        dt_txt = 'dt_txt'
        current_city_text.configure(text = user_city_search)
        current_temp_text.configure(text = f'{temp}°')
        path_to_main_icon = os.path.abspath(__file__ + f'/../weather/{icon}.png')
        if not os.path.exists(path_to_main_icon):
            path_to_main_icon = os.path.abspath(__file__ + f'/../weather/01d.png')
            print('Не знайдено картинку', list_weather_icon[0])
        image_main_icon = PIL.Image.open(path_to_main_icon)
        image_main_icon = image_main_icon.resize([180, 180])
        image_main_icon = PIL.ImageTk.PhotoImage(image_main_icon)
        current_image.configure(image = image_main_icon)
        weather_desription = translator.translate(weather_desription)
        weather_description_main = translator.translate(weather_description_main).title()
        current_description_text.configure(text = weather_description_main)
        current_weather_description.configure(text = weather_desription)
        list_weather_time = []
        list_weather_temp = []
        list_weather_icon = []
        list_weather_icon_path = []
        for dt_txt in data['list']:
            list_weather_time.append(dt_txt['dt_txt'].split(' ')[1].split(':')[0])
            list_weather_temp.append(round(dt_txt['main']['temp'] - 273.15, 1))
            path_to_icon = os.path.abspath(__file__ + f'/../weather/{dt_txt["weather"][0]["icon"]}.png')
            if not os.path.exists(path_to_icon):
                path_to_icon = os.path.abspath(__file__ + f'/../weather/01d.png')
                print('Не знайдено картинку', list_weather_icon[0])
            image_icon = PIL.Image.open(path_to_icon)
            image_icon = image_icon.resize([50, 50])
            image_icon = PIL.ImageTk.PhotoImage(image_icon)
            list_weather_icon.append(image_icon)
            list_weather_icon_path.append(path_to_icon)
        for i in range(8):
            list_first_hours_time[i].configure(text = f'{list_weather_time[i]}:00')
            list_first_hours_temp[i].configure(text = f'{list_weather_temp[i]}°')
            list_weather_icon2[i].configure(image = list_weather_icon[i])
        list_weather_max_min_temp = []
        for i in range(8):
            list_weather_max_min_temp.append(list_weather_temp[i])
        current_description_select_text.configure(text = weather_desription)
        current_city_select_text.configure(text = user_city_search)
        current_temp_select_text.configure(text = f'{str(temp).split('.')[0]}°')
        max_temp = str(max(list_weather_max_min_temp)).split('.')[0]
        min_temp = str(min(list_weather_max_min_temp)).split('.')[0]
        current_city_select_max_temp_text.configure(text = f'mакс: {max_temp}°, мін: {min_temp}°')
        current_max_temp.configure(text = f'{min_temp}°          {max_temp}°')
        # load_weather()
search_loope.bind('<Button-1>', search_city)
def open_register(event):
    frame_auth = CTkToplevel(app)
    frame_auth.geometry('460x645')
    frame_auth.title('Register')
    frame_auth_contain = CTkFrame(frame_auth, 460, 645, fg_color = '#5DA7B1', border_color = '#096C82', border_width = 5)
    frame_auth_contain.place(x = 0, y = 0)
    frame_auth_contain2 = CTkFrame(frame_auth_contain, 300, 300, fg_color = '#5DA7B1')
    frame_auth_contain2.place(x = 30, y = 105)
    country_text = CTkLabel(frame_auth_contain2, text = 'Країна:', font = ('Arial', 22), text_color = 'white')
    country_text.grid(row = 0, column = 0, pady = 10, sticky = 'w', padx = 5)
    city_text = CTkLabel(frame_auth_contain2, text = 'Місто:', font = ('Arial', 22), text_color = 'white')
    city_text.grid(row = 2, column = 0, pady = 10, sticky = 'w', padx = 5)
    name_text = CTkLabel(frame_auth_contain2, text = "Ім'я:", font = ('Arial', 22), text_color = 'white')
    name_text.grid(row = 4, column = 0, pady = 10, sticky = 'w', padx = 5)
    surname_text = CTkLabel(frame_auth_contain2, text = 'Прізвище:', font = ('Arial', 22), text_color = 'white')
    surname_text.grid(row = 6, column = 0, pady = 10, sticky = 'w', padx = 5)
    if user_name != None:
        personal_office_text = CTkLabel(frame_auth_contain, text = 'Особистий кабінет', font = ('Arial', 28), text_color = 'white')
        personal_office_text.place(x = 105, y = 40)
        country_name_text = CTkLabel(frame_auth_contain2, text = user_country, font = ('Arial', 28), text_color = 'white')
        country_name_text.grid(row = 1, column = 0, pady = 10, sticky = 'w', padx = 60)
        city_name_text = CTkLabel(frame_auth_contain2, text = user_city, font = ('Arial', 28), text_color = 'white')
        city_name_text.grid(row = 3, column = 0, pady = 10, sticky = 'w', padx = 60)
        name_user_text = CTkLabel(frame_auth_contain2, text = user_name, font = ('Arial', 28), text_color = 'white')
        name_user_text.grid(row = 5, column = 0, pady = 10, sticky = 'w', padx = 60)
        surname_user_text = CTkLabel(frame_auth_contain2, text = user_surname, font = ('Arial', 28), text_color = 'white')
        surname_user_text.grid(row = 7, column = 0, pady = 10, sticky = 'w', padx = 60)
        frame_exit_account = CTkFrame(frame_auth_contain, fg_color = '#5DA7B1')
        frame_exit_account.place(x = 380, y = 20)
        exit_account_text = CTkLabel(frame_exit_account, text = 'Вийти', font = ('Arial', 12), text_color = 'white')
        exit_account_text.grid(row = 0, column = 0, sticky = 'w')
        path_image2 = os.path.abspath(__file__ + '/../weather/exit.png')
        image_exit = PIL.Image.open(path_image2)
        image_exit = image_exit.resize((40, 40))
        exit_account_image = CTkLabel(frame_exit_account, image = PIL.ImageTk.PhotoImage(image_exit), text = '')
        exit_account_image.grid(row = 0, column = 1)
        exit_account_image.bind('<Button-1>', lambda event: exit_account(label_user_text, frame_auth))
    else:
        personal_office_text = CTkLabel(frame_auth_contain, text = 'Реєстрація користувача', font = ('Arial', 28), text_color = 'white')
        personal_office_text.place(x = 70, y = 40)
        country_name_entry = CTkEntry(frame_auth_contain2, font = ('Arial', 22), width = 218, height = 46, corner_radius = 20, fg_color = '#096C82', border_color = '#b5d3d9', border_width = 3)
        country_name_entry.grid(row = 1, column = 0, pady = 5, sticky = 'w')
        city_name_entry = CTkEntry(frame_auth_contain2, font = ('Arial', 22), width = 218, height = 46, corner_radius = 20, fg_color = '#096C82', border_color = '#b5d3d9', border_width = 3)
        city_name_entry.grid(row = 3, column = 0, pady = 5, sticky = 'w')
        name_entry = CTkEntry(frame_auth_contain2, font = ('Arial', 22), width = 295, height = 46, corner_radius = 20, fg_color = '#096C82', border_color = '#b5d3d9', border_width = 3)
        name_entry.grid(row = 5, column = 0, pady = 5)
        surname_entry = CTkEntry(frame_auth_contain2, font = ('Arial', 22), width = 295, height = 46, corner_radius = 20, fg_color = '#096C82', border_color = '#b5d3d9', border_width = 3)
        surname_entry.grid(row = 7, column = 0, pady = 5)
        button_save = CTkButton(frame_auth_contain, width = 218, height = 46, text = 'Зберегти', font = ('Arial', 22), corner_radius = 20, fg_color = '#096C82', hover_color = '#096C82', border_color = '#b5d3d9', border_width = 3, command = lambda: sign_up_save(frame_auth, country_name_entry, city_name_entry, name_entry, surname_entry, label_user_text))
        button_save.place(x = 105, y = 560)
label_user.bind('<Button-1>', open_register)

app.mainloop()