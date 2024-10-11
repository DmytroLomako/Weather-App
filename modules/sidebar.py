from .search import *


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
        temp_city = str(temp_city).split('.')[0]
        self.city_temp_text = CTkLabel(self.frame, text = f'{temp_city}°', font = ('Arial', 50), text_color = 'white')
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
        global search_city, temp, weather_desription, max_temp, min_temp
        self.city_name.configure(text = app_data['city'])
        temp_city = str(temp).split('.')[0]
        self.city_temp_text.configure(text = f'{temp_city}°')
        self.city_description_text.configure(text = weather_desription)
        self.city_max_min_temp_text.configure(text = f'max: {max_temp}°, min: {min_temp}°')
        weather_data['user_city_search'] = self.name
        search_city(None)
def sidebar_city_bind(city_name, city_row):
    city = Sidebar_City(city_name, city_row)
    city.sidebar_city_func()
    city.frame.bind('<Button-1>', city.click_city)
    city.city_temp_text.bind('<Button-1>', city.click_city)
    city.city_name.bind('<Button-1>', city.click_city)
    city.city_description_text.bind('<Button-1>', city.click_city)
if app_data['city'] != None:
    for i in range(len(list_cities)):
        sidebar_city_bind(list_cities[i], i + 1)