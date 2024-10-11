from .weather import *


def right_arrow_func(event):
    if weather_data['range_count'][7] == 39:
        return False
    weather_data['left_arrow'].configure(text_color = 'white')
    weather_data['range_count'].append(weather_data['range_count'][7] + 1)
    del weather_data['range_count'][0]
    j = 0
    for i in weather_data['range_count']:
        weather_data['first_hours_time'][j].configure(text = f'{app_data['weather_time'][i]}:00')
        weather_data['first_hours_temp'][j].configure(text = f'{app_data['weather_temp'][i]}°')
        weather_icon = app_data['weather_icon'][i]
        path_to_image = os.path.abspath(__file__ + f'/../../weather/{weather_icon}.png')
        try:
            if app_data['icon_path'] != None:
                path_to_image = app_data['icon_path'][i]
        except:
            pass
        if not os.path.exists(path_to_image):
            path_to_image = os.path.abspath(__file__ + f'/../../weather/01d.png')
            print('Не знайдено картинку', app_data['weather_icon'][0])
        image = PIL.Image.open(path_to_image)
        image = image.resize([50, 50])
        image = PIL.ImageTk.PhotoImage(image)
        list_weather_icon2[j].configure(image = image)
        j += 1
    if weather_data['range_count'][7] == 39:
        weather_data['right_arrow'].configure(text_color = '#a0bcbd')
def left_arrow_func(event):
    if weather_data['range_count'][0] == 0:
        return False
    weather_data['right_arrow'].configure(text_color = 'white')
    weather_data['range_count'].insert(0, weather_data['range_count'][0] - 1)
    del weather_data['range_count'][8]
    j = 0
    for i in weather_data['range_count']:
        weather_data['first_hours_time'][j].configure(text = f'{app_data['weather_time'][i]}:00')
        weather_data['first_hours_temp'][j].configure(text = f'{app_data['weather_temp'][i]}°')
        path_to_image = os.path.abspath(__file__ + f'/../../weather/{app_data['weather_icon'][i]}.png')
        try:
            if app_data['icon_path'] != None:
                path_to_image = app_data['icon_path'][i]
        except:
            pass
        if not os.path.exists(path_to_image):
            path_to_image = os.path.abspath(__file__ + f'/../../weather/01d.png')
            print('Не знайдено картинку', app_data['weather_icon'][0])
        image = PIL.Image.open(path_to_image)
        image = image.resize([50, 50])
        image = PIL.ImageTk.PhotoImage(image)
        list_weather_icon2[j].configure(image = image)
        j += 1
    if weather_data['range_count'][0] == 0:
        weather_data['left_arrow'].configure(text_color = '#a0bcbd')

weather_data['right_arrow'].bind('<Button-1>', right_arrow_func)
weather_data['left_arrow'].bind('<Button-1>', left_arrow_func)