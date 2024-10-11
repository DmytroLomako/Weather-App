from .weather import *
from .sidebar import sidebar_city_bind


def exit_account(label_user_text, frame):
    app_data['country'] = None
    app_data['city'] = None
    app_data['name'] = None
    app_data['surname'] = None
    label_user_text.configure(text = 'Зареєструйтесь')
    frame.destroy()
    os.remove(path_to_json)
    
def sign_up_save(frame_auth, country_name_entry, city_name_entry, name_entry, surname_entry, label_user_text, personal_office_text):
    app_data['country'] = country_name_entry.get()
    app_data['city'] = city_name_entry.get()
    app_data['name'] = name_entry.get()
    app_data['surname'] = surname_entry.get()
    label_user_text.configure(text = f'{app_data['name']} {app_data['surname']}')
    url = f'https://api.openweathermap.org/data/2.5/weather?q={app_data['city']}&appid={api}'
    answer = get(url)
    if answer.status_code == 200:
        if app_data['country'] != '' and app_data['city'] != '' and app_data['name'] != '' and app_data['surname'] != '':
            frame_auth.destroy()
            for i in range(len(list_cities)):
                sidebar_city_bind(list_cities[i], i + 1)
            main_map = True
            load_weather()
            with open(path_to_json, 'w')as file:
                json.dump({'country': app_data['country'], 'city': app_data['city'], 'name': app_data['name'], 'surname': app_data['surname']}, file, indent = 4, ensure_ascii = False)
    else:
        if app_data['country'] != '' and app_data['city'] != '' and app_data['name'] != '' and app_data['surname'] != '':
            if app_data['api_check'] == False:
                personal_office_text.configure(text = 'Невірний api, або місто')
                personal_office_text.configure(text_color = 'red')
            else:
                city_name_entry.configure(border_color = 'red')
                personal_office_text.configure(text = 'Неправильно введено місто')
        else:
            personal_office_text.configure(text = 'Заповніть всі поля')
    
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
    if app_data['name'] != None:
        personal_office_text = CTkLabel(frame_auth_contain, text = 'Особистий кабінет', font = ('Arial', 28), text_color = 'white')
        personal_office_text.place(x = 105, y = 40)
        country_name_text = CTkLabel(frame_auth_contain2, text = app_data['country'], font = ('Arial', 28), text_color = 'white')
        country_name_text.grid(row = 1, column = 0, pady = 10, sticky = 'w', padx = 60)
        city_name_text = CTkLabel(frame_auth_contain2, text = app_data['city'], font = ('Arial', 28), text_color = 'white')
        city_name_text.grid(row = 3, column = 0, pady = 10, sticky = 'w', padx = 60)
        name_user_text = CTkLabel(frame_auth_contain2, text = app_data['name'], font = ('Arial', 28), text_color = 'white')
        name_user_text.grid(row = 5, column = 0, pady = 10, sticky = 'w', padx = 60)
        surname_user_text = CTkLabel(frame_auth_contain2, text = app_data['surname'], font = ('Arial', 28), text_color = 'white')
        surname_user_text.grid(row = 7, column = 0, pady = 10, sticky = 'w', padx = 60)
        frame_exit_account = CTkFrame(frame_auth_contain, fg_color = '#5DA7B1')
        frame_exit_account.place(x = 380, y = 20)
        exit_account_text = CTkLabel(frame_exit_account, text = 'Вийти', font = ('Arial', 12), text_color = 'white')
        exit_account_text.grid(row = 0, column = 0, sticky = 'w')
        path_image2 = os.path.abspath(__file__ + '/../../weather/exit.png')
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
        button_save = CTkButton(frame_auth_contain, width = 218, height = 46, text = 'Зберегти', font = ('Arial', 22), corner_radius = 20, fg_color = '#096C82', hover_color = '#096C82', border_color = '#b5d3d9', border_width = 3, command = lambda: sign_up_save(frame_auth, country_name_entry, city_name_entry, name_entry, surname_entry, label_user_text, personal_office_text))
        button_save.place(x = 105, y = 560)
label_user.bind('<Button-1>', open_register)
if app_data['city'] == None:
    open_register(None)