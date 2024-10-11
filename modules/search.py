from .weather import *


weather_data['user_city_search'] = ''
def search_city(event):
    global temp, feels_like, wind_speed, humidity, weather_desription, current_temp_text, max_temp, min_temp, data, hour
    if event != None:
        weather_data['user_city_search'] = search_entry.get()
    app_data['city'] = weather_data['user_city_search']
    url = f'https://api.openweathermap.org/data/2.5/forecast?q={weather_data['user_city_search']}&appid={api}'
    answer = get(url)
    if answer.status_code == 200:
        weather_data['range_count'] = [0, 1, 2, 3, 4, 5, 6, 7]
        weather_data['left_arrow'].configure(text_color = '#a0bcbd')
        weather_data['right_arrow'].configure(text_color = 'white')
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
        weather_data['current_city_text'].configure(text = weather_data['user_city_search'])
        current_temp_text.configure(text = f'{temp}°')
        path_to_main_icon = os.path.abspath(__file__ + f'/../../weather/{icon}.png')
        if not os.path.exists(path_to_main_icon):
            path_to_main_icon = os.path.abspath(__file__ + f'/../../weather/01d.png')
            print('Не знайдено картинку', app_data['weather_icon'][0])
        image_main_icon = PIL.Image.open(path_to_main_icon)
        image_main_icon = image_main_icon.resize([180, 180])
        image_main_icon = PIL.ImageTk.PhotoImage(image_main_icon)
        current_image.configure(image = image_main_icon)
        weather_desription = translator.translate(weather_desription)
        weather_description_main = translator.translate(weather_description_main).title()
        current_description_text.configure(text = weather_description_main)
        current_weather_description.configure(text = weather_desription)
        app_data['weather_time'] = []
        app_data['weather_temp'] = []
        app_data['weather_icon'] = []
        app_data['icon_path'] = []
        for dt_txt in data['list']:
            app_data['weather_time'].append(int(dt_txt['dt_txt'].split(' ')[1].split(':')[0]))
            app_data['weather_temp'].append(round(dt_txt['main']['temp'] - 273.15, 1))
            weather_icon = dt_txt["weather"][0]["icon"]
            path_to_icon = os.path.abspath(__file__ + f'/../../weather/{weather_icon}.png')
            if not os.path.exists(path_to_icon):
                path_to_icon = os.path.abspath(__file__ + f'/../../weather/01d.png')
                print('Не знайдено картинку', app_data['weather_icon'][0])
            image_icon = PIL.Image.open(path_to_icon)
            image_icon = image_icon.resize([50, 50])
            image_icon = PIL.ImageTk.PhotoImage(image_icon)
            app_data['weather_icon'].append(image_icon)
            app_data['icon_path'].append(path_to_icon)
        app_data['lat'] = data['city']['coord']['lat']
        app_data['lon'] = data['city']['coord']['lon']
        tz = tf.timezone_at(lng = lon, lat = lat)
        tz = pytz.timezone(tz)
        time = str(datetime.now(tz))
        hour = time.split(' ')[1].split(':')[0]
        first_hour = int(app_data['weather_time'][0])
        hour = int(hour)
        count = -1
        for i in range(len(app_data['weather_time'])):
            count += 1
            hour = hour // 3 * 3
            # if first_hour != hour:
            app_data['weather_time'][i] = hour + 3 * count
            if app_data['weather_time'][i] >= 24:
                app_data['weather_time'][i] -= 24
                hour = 0
                count = 0
        for i in range(8):
            weather_data['first_hours_time'][i].configure(text = f'{app_data['weather_time'][i]}:00')
            weather_data['first_hours_temp'][i].configure(text = f'{app_data['weather_temp'][i]}°')
            list_weather_icon2[i].configure(image = app_data['weather_icon'][i])
        list_weather_max_min_temp = []
        for i in range(8):
            list_weather_max_min_temp.append(app_data['weather_temp'][i])
        current_description_select_text.configure(text = weather_desription)
        current_city_select_text.configure(text = weather_data['user_city_search'])
        temp_city = str(temp).split('.')[0]
        current_temp_select_text.configure(text = f'{temp_city}°')
        max_temp = str(max(list_weather_max_min_temp)).split('.')[0]
        min_temp = str(min(list_weather_max_min_temp)).split('.')[0]
        current_city_select_max_temp_text.configure(text = f'mакс: {max_temp}°, мін: {min_temp}°')
        current_max_temp.configure(text = f'{min_temp}°          {max_temp}°')
        # load_weather()
search_loope.bind('<Button-1>', search_city)
search_entry.bind('<Return>', search_city)
