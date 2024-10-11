import json, pytz
from requests import get
from customtkinter import *
from deep_translator import GoogleTranslator
from datetime import datetime
from timezonefinder import TimezoneFinder


api = ''
tf = TimezoneFinder()
translator = GoogleTranslator(source = 'auto', target = 'uk')
path_to_json = os.path.abspath(__file__ + '/../../save.json')
app_data = {
    'country': None,
    'city': None,
    'name': None,
    'surname': None,
    'api_check': True,
    'weather_time': [],
    'weather_temp': [],
    'weather_icon': []
}
weather_data = {}

if os.path.exists(path_to_json):
    with open(path_to_json, 'r') as file:
        data = json.load(file)
        app_data['country'] = data['country']
        app_data['city'] = data['city']
        app_data['name'] = data['name']
        app_data['surname'] = data['surname']
        
weekdays = ['Понеділок', 'Вівторок', 'Середа', 'Четвер', "П'ятниця", 'Субота', 'Неділя']
list_cities = ['Kyiv', 'Tokyo', 'Paris', 'London', 'New York']