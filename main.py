import PIL.Image
import PIL.ImageTk
import requests
from customtkinter import *
import PIL
import os
import json


# city = input("Enter a city: ")
# url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api}'
# answer = requests.get(url)
# if answer.status_code == 200:
#     data = answer.json()
#     print(data)
#     temp = data['main']['temp'] - 273.15
#     temp = round(temp, 2)
#     feels_like = round(data['main']['feels_like'] - 273.15, 2)
#     wind_speed = data['wind']['speed']
#     humidity = data['main']['humidity']
#     weather_desription = data['weather'][0]['description']
#     print(temp, feels_like, wind_speed, humidity, weather_desription)

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
    answer = requests.get(url)
    if answer.status_code == 200:
        if user_country != '' and user_city != '' and user_name != '' and user_surname != '':
            frame_auth.destroy()
            main_map = True
            load_weather()
            with open(path_to_json, 'w')as file:
                json.dump({'country': user_country, 'city': user_city, 'name': user_name, 'surname': user_surname}, file, indent = 4, ensure_ascii = False)
    else:
        city_name_entry.configure(border_color = 'red')
# frame_sign_up = CTk()
# frame_sign_up.geometry('460x645')
# frame_sign_up.title('Register')
# frame_sign_up_contain = CTkFrame(frame_sign_up, 460, 645, fg_color = '#5DA7B1', border_color = '#096C82', border_width = 5)
# frame_sign_up_contain.place(x = 0, y = 0)
# sign_up_text = CTkLabel(frame_sign_up_contain, text = 'Реєстрація користувача', font = ('Arial', 28), text_color = 'white')
# sign_up_text.place(x = 70, y = 40)
# frame_sign_up_contain2 = CTkFrame(frame_sign_up_contain, 300, 300, fg_color = '#5DA7B1')
# frame_sign_up_contain2.place(x = 30, y = 105)
# country_name_text = CTkLabel(frame_sign_up_contain2, text = 'Країна:', font = ('Arial', 22), text_color = 'white')
# country_name_text.grid(row = 0, column = 0, pady = 10, sticky = 'w', padx = 5)
# city_name_text = CTkLabel(frame_sign_up_contain2, text = 'Місто:', font = ('Arial', 22), text_color = 'white')
# city_name_text.grid(row = 2, column = 0, pady = 10, sticky = 'w', padx = 5)
# name_text = CTkLabel(frame_sign_up_contain2, text = "Ім'я:", font = ('Arial', 22), text_color = 'white')
# name_text.grid(row = 4, column = 0, pady = 10, sticky = 'w', padx = 5)
# surname_text = CTkLabel(frame_sign_up_contain2, text = "Прізвище:", font = ('Arial', 22), text_color = 'white')
# surname_text.grid(row = 6, column = 0, pady = 10, sticky = 'w', padx = 5)
# country_name_entry = CTkEntry(frame_sign_up_contain2, font = ('Arial', 22), width = 218, placeholder_text = 'Введіть країну', corner_radius = 20, fg_color = '#096C82', border_color = '#b5d3d9', border_width = 3)
# country_name_entry.grid(row = 1, column = 0, pady = 10, sticky = 'w')
# city_name_entry = CTkEntry(frame_sign_up_contain2, font = ('Arial', 22), width = 218, placeholder_text = 'Введіть місто', corner_radius = 20, fg_color = '#096C82', border_color = '#b5d3d9', border_width = 3)
# city_name_entry.grid(row = 3, column = 0, pady = 10, sticky = 'w')
# name_entry = CTkEntry(frame_sign_up_contain2, font = ('Arial', 22), width = 295, placeholder_text = "Введіть ваше ім'я", corner_radius = 20, fg_color = '#096C82', border_color = '#b5d3d9', border_width = 3)
# name_entry.grid(row = 5, column = 0, pady = 10)
# surname_entry = CTkEntry(frame_sign_up_contain2, font = ('Arial', 22), width = 295, placeholder_text = "Введіть ваше прізвище", corner_radius = 20, fg_color = '#096C82', border_color = '#b5d3d9', border_width = 3)
# surname_entry.grid(row = 7, column = 0, pady = 10)
# button_save = CTkButton(frame_sign_up_contain, text = 'Зберегти', font = ('Arial', 22), corner_radius = 20, fg_color = '#096C82', hover_color = '#096C82', border_color = '#b5d3d9', border_width = 3, command = sign_up_save)
# button_save.place(x = 155, y = 560)
# frame_sign_up.mainloop()
print(os.path.exists(path_to_json))
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
if main_map:
    url = f'https://api.openweathermap.org/data/2.5/weather?q={user_city}&appid={api}'
    answer = requests.get(url)
    if answer.status_code == 200:
        data = answer.json()
        temp = data['main']['temp'] - 273.15
        temp = round(temp, 1)
        feels_like = round(data['main']['feels_like'] - 273.15, 1)
        wind_speed = data['wind']['speed']
        humidity = data['main']['humidity']
        weather_desription = data['weather'][0]['main']
        # date_time = data['list'][]
    app = CTk()
    app.title('Weather App')
    app.geometry('1200x800')
    frame_city_select = CTkFrame(app, 275, 800, fg_color = '#096C82')
    frame_city_select.place(x = 0, y = 0)
    frame_weather = CTkFrame(app, 925, 800, fg_color = '#5DA7B1', border_color = '#096C82', border_width = 5)
    frame_weather.place(x = 275, y = 0)
    frame_user = CTkFrame(app, fg_color = '#5DA7B1', corner_radius = 0)
    path_image = os.path.abspath(__file__ + '/../user.png')
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
    search_entry = CTkEntry(frame_weather, font = ('Arial', 22), width = 218, height = 46, placeholder_text = 'Пошук', corner_radius = 20, fg_color = '#096C82', border_color = '#b5d3d9', border_width = 3)
    search_entry.place(x = 645, y = 45)
    path_image3 = os.path.abspath(__file__ + '/../loope.png')
    image3 = PIL.Image.open(path_image3)
    image3 = image3.resize([42, 33])
    image3 = PIL.ImageTk.PhotoImage(image3)
    search_loope = CTkLabel(frame_weather, image = image3, text = '')
    search_loope.place(x = 595, y = 53)
    frame_current_position = CTkFrame(frame_weather, 315, 275, fg_color = '#5DA7B1')
    frame_current_position.place(x = 300, y = 120)
    def load_weather():
        current_position_text = CTkLabel(frame_current_position, text = 'Поточна позиція', font = ('Arial', 35), text_color = 'white')
        current_position_text.grid(row = 0, column = 0, pady = 10)
        current_city_text = CTkLabel(frame_current_position, text = user_city, font = ('Arial', 22), text_color = 'white')
        current_city_text.grid(row = 1, column = 0, pady = 10)
        current_temp_text = CTkLabel(frame_current_position, text = f'{temp}°', font = ('Arial', 48), text_color = 'white')
        current_temp_text.grid(row = 2, column = 0, pady = 10)
        current_description_text = CTkLabel(frame_current_position, text = weather_desription, font = ('Arial', 22), text_color = 'white')
        current_description_text.grid(row = 3, column = 0, pady = 10)
        # date_time = CTkLabel(frame_current_position, text = , font = ('Arial', 22), text_color = 'white')
    if user_name != None:
        load_weather()
    user_city_search = ''
    def search_city():
        global user_city_search, temp, feels_like, wind_speed, humidity, weather_desription, current_city_text, current_temp_text
        user_city_search = search_entry.get()
        app.after(1000, search_city)
        if user_city_search != '':
            url = f'https://api.openweathermap.org/data/2.5/weather?q={user_city_search}&appid={api}'
            answer = requests.get(url)
            if answer.status_code == 200:
                data = answer.json()
                temp = data['main']['temp'] - 273.15
                temp = round(temp, 1)
                feels_like = round(data['main']['feels_like'] - 273.15, 1)
                wind_speed = data['wind']['speed']
                humidity = data['main']['humidity']
                weather_desription = data['weather'][0]['main']
                current_city_text.configure(text = user_city_search)
                current_temp_text.configure(text = f'{temp}°C')
    app.after(1000, search_city)
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
            path_image2 = os.path.abspath(__file__ + '/../exit.png')
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