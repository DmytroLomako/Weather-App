from .settings import *
from .widgets import *
from .weather_get_data import *
        
        
def load_weather():
    global current_temp_text, weather_desription, current_description_text, current_time_func, current_city_select_text, current_description_select_text, current_temp_select_text, max_temp, min_temp, current_city_select_max_temp_text, weather_description_main, list_weather_icon2, current_max_temp, current_weather_description, current_image, data, time_week, hour
    current_position_text = CTkLabel(frame_current_position, text = 'Поточна позиція', font = ('Arial', 35), text_color = 'white')
    current_position_text.grid(row = 0, column = 0, pady = 10)
    weather_data['current_city_text'] = CTkLabel(frame_current_position, text = app_data['city'], font = ('Arial', 22), text_color = 'white')
    weather_data['current_city_text'].grid(row = 1, column = 0, pady = 10)
    current_temp_text = CTkLabel(frame_current_position, text = f'{temp}°', font = ('Arial', 48), text_color = 'white')
    current_temp_text.grid(row = 2, column = 0, pady = 10)
    path_to_image = os.path.abspath(__file__ + f'/../../weather/{icon}.png')
    if not os.path.exists(path_to_image):
        path_to_image = os.path.abspath(__file__ + f'/../../weather/01d.png')
        print('Не знайдено картинку', app_data['weather_icon'][0])
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
    weather_data['range_count'] = [0, 1, 2, 3, 4, 5, 6, 7]

    weekday_text = CTkLabel(frame_weather, text = weekdays[time_week.weekday()], font = ('Arial', 24), text_color = 'white')
    weekday_text.place(x = 700, y = 200)
    weather_data['first_hours_temp'] = []
    weather_data['first_hours_time'] = []
    list_weather_icon2 = []
    for i in range(8):
        first_hours_time = CTkLabel(frame_hourly_weather, text = f'{app_data['weather_time'][i]}:00', font = ('Arial', 18), text_color = 'white')
        first_hours_time.grid(row = 0, column = i, pady = 10, padx = 10)
        weather_data['first_hours_time'].append(first_hours_time)
        path_to_image = os.path.abspath(__file__ + f'/../../weather/{app_data['weather_icon'][i]}.png')
        if not os.path.exists(path_to_image):
            path_to_image = os.path.abspath(__file__ + f'/../../weather/01d.png')
            print('Не знайдено картинку', app_data['weather_icon'][0])
        image = PIL.Image.open(path_to_image)
        image = image.resize([50, 50])
        image = PIL.ImageTk.PhotoImage(image)
        label_image = CTkLabel(frame_hourly_weather, image = image, text = '')
        label_image.grid(row = 1, column = i, pady = 10, padx = 16)
        list_weather_icon2.append(label_image)
        first_hours_temp = CTkLabel(frame_hourly_weather, text = f'{app_data['weather_temp'][i]}°', font = ('Arial', 26), text_color = 'white')
        first_hours_temp.grid(row = 2, column = i, pady = 10, padx = 16)
        weather_data['first_hours_temp'].append(first_hours_temp)
    list_weather_max_min_temp = []
    for i in range(8):
        list_weather_max_min_temp.append(app_data['weather_temp'][i])
    max_temp = str(max(list_weather_max_min_temp)).split('.')[0]
    min_temp = str(min(list_weather_max_min_temp)).split('.')[0]
    path_image_arrow_up = os.path.abspath(__file__ + '/../../weather/arrow_up.png')
    image_arrow_up = PIL.Image.open(path_image_arrow_up)
    image_arrow_up = image_arrow_up.resize([28, 33])
    image_arrow_up = PIL.ImageTk.PhotoImage(image_arrow_up)
    path_image_arrow_down = os.path.abspath(__file__ + '/../../weather/arrow_down.png')
    image_arrow_down = PIL.Image.open(path_image_arrow_down)
    image_arrow_down = image_arrow_down.resize([28, 33])
    image_arrow_down = PIL.ImageTk.PhotoImage(image_arrow_down)
    current_max_temp = CTkLabel(frame_weather, text = f'{min_temp}°          {max_temp}°', font = ('Arial', 30), text_color = 'white')
    current_max_temp.place(x = 370, y = 360)
    arrow_up = CTkLabel(frame_weather, image = image_arrow_up, text = '', font = ('Arial', 30), text_color = 'white')
    arrow_up.place(x = 460, y = 360)
    arrow_down = CTkLabel(frame_weather, image = image_arrow_down, text = '', font = ('Arial', 30), text_color = 'white')
    arrow_down.place(x = 330, y = 360)
    app_data["lat"] = data['city']['coord']['lat']
    app_data["lon"] = data['city']['coord']['lon']
    def current_time_func():
        global data, time
        app.after(1000, current_time_func)
        tz = tf.timezone_at(lng = app_data['lon'], lat = app_data['lat'])
        tz = pytz.timezone(tz)
        time = str(datetime.now(tz))
        time = time.split(' ')[1].split('.')[0]
        current_time_now_text = CTkLabel(frame_weather, text = time, font = ('Arial', 30), text_color = 'white')
        current_time_now_text.place(x = 677, y = 300)
    weather_data['right_arrow'] = CTkLabel(frame_weather, text = '>', font = ('Arial', 50), text_color = 'white')
    weather_data['right_arrow'].place(x = 875, y = 550)
    weather_data['left_arrow'] = CTkLabel(frame_weather, text = '<', font = ('Arial', 50), text_color = '#a0bcbd')
    weather_data['left_arrow'].place(x = 20, y = 550)
    current_time_func()
    frame_current_city = CTkFrame(frame_city_select, 235, 100, fg_color = '#5DA7B1', border_color = '#b5d3d9', border_width = 5, corner_radius = 20)
    frame_current_city.place(x = 20, y = 30)
    current_city_position_text = CTkLabel(frame_current_city, text = 'Поточна позиція', font = ('Arial', 16), text_color = 'white')
    current_city_position_text.place(x = 14, y = 8)
    current_city_select_text = CTkLabel(frame_current_city, text = app_data['city'], font = ('Arial', 12), text_color = 'white')
    current_city_select_text.place(x = 15, y = 30)
    temp_city = str(temp).split('.')[0]
    current_temp_select_text = CTkLabel(frame_current_city, text = f'{temp_city}°', font = ('Arial', 50), text_color = 'white')
    current_temp_select_text.place(x = 150, y = 10)
    current_description_select_text = CTkLabel(frame_current_city, text = weather_desription, font = ('Arial', 13), text_color = 'white')
    current_description_select_text.place(x = 14, y = 55)
    current_city_select_max_temp_text = CTkLabel(frame_current_city, text = f'макс: {max_temp}°, мін: {min_temp}°', font = ('Arial', 12), text_color = 'white')
    current_city_select_max_temp_text.place(x = 120, y = 65)

if app_data['name'] != None:
    load_weather()
    app.after(1000, current_time_func)