from .settings import *


url = f'https://api.openweathermap.org/data/2.5/forecast?q={app_data['city']}&appid={api}'
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
    lat = data['city']['coord']['lat']
    lon = data['city']['coord']['lon']
    tz = tf.timezone_at(lng = lon, lat = lat)
    tz = pytz.timezone(tz)
    time_week = datetime.now(tz)
    time = str(datetime.now(tz))
    hour = time.split(' ')[1].split(':')[0]
    time = time.split(' ')[0].split('.')[0]
    month = time.split('-')[1]
    day = time.split('-')[2]
    year = time.split('-')[0].split('20')[1]
    dt_txt = 'dt_txt'
    for dt_txt in data['list']:
        app_data['weather_time'].append(int(dt_txt['dt_txt'].split(' ')[1].split(':')[0]))
        app_data['weather_temp'].append(round(dt_txt['main']['temp'] - 273.15, 1))
        app_data['weather_icon'].append(dt_txt['weather'][0]['icon'])
else:
    app_data['country'] = None
    app_data['city'] = None
    app_data['name'] = None
    app_data['surname'] = None
    url = f'https://api.openweathermap.org/data/2.5/forecast?q={app_data['city']}&appid={api}'
    answer = get(url)
    if answer.status_code != 200:
        print('Wrong api')
        app_data['api_check'] = False
    else:
        data = answer.json()
        temp = data['list'][0]['main']['temp'] - 273.15
        temp = round(temp, 1)
        icon = data['list'][0]['weather'][0]['icon']
        feels_like = round(data['list'][0]['main']['feels_like'] - 273.15, 1)
        wind_speed = data['list'][0]['wind']['speed']
        humidity = data['list'][0]['main']['humidity']
        weather_description_main = data['list'][0]['weather'][0]['main'].title()
        weather_desription = data['list'][0]['weather'][0]['description'].title()
        lat = data['city']['coord']['lat']
        lon = data['city']['coord']['lon']
        tz = tf.timezone_at(lng = lon, lat = lat)
        tz = pytz.timezone(tz)
        time_week = datetime.now(tz)
        time = str(datetime.now(tz))
        hour = time.split(' ')[1].split(':')[0]
        time = time.split(' ')[0].split('.')[0]
        month = time.split('-')[1]
        day = time.split('-')[2]
        year = time.split('-')[0].split('20')[1]
        dt_txt = 'dt_txt'
        for dt_txt in data['list']:
            app_data['weather_time'].append(int(dt_txt['dt_txt'].split(' ')[1].split(':')[0]))
            app_data['weather_temp'].append(round(dt_txt['main']['temp'] - 273.15, 1))
            app_data['weather_icon'].append(dt_txt['weather'][0]['icon'])