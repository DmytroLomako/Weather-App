from customtkinter import *
import PIL.Image
from .settings import app_data


app = CTk()
app.title('Weather App')
app.geometry('1200x800')
frame_city_select = CTkFrame(app, 275, 800, fg_color = '#096C82')
frame_city_select.place(x = 0, y = 0)
frame_weather = CTkFrame(app, 925, 800, fg_color = '#5DA7B1', border_color = '#096C82', border_width = 5)
frame_weather.place(x = 275, y = 0)
frame_user = CTkFrame(app, fg_color = '#5DA7B1', corner_radius = 0)
path_image = os.path.abspath(__file__ + '/../../weather/user.png')
image = PIL.Image.open(path_image)
image = image.resize([64, 50])
image = PIL.ImageTk.PhotoImage(image)
label_user = CTkLabel(frame_user, image = image, text = '')
label_user_text = CTkLabel(frame_user, text = f'{app_data['name']} {app_data['surname']}', font = ('Arial', 20), text_color = 'white')
if app_data['name'] == None:
    label_user_text.configure(text = 'Зареєструйтесь')
frame_user.place(x = 320, y = 30)
label_user.grid(row = 0, column = 0)
label_user_text.grid(row = 0, column = 1, padx = 5)
search_entry = CTkEntry(frame_weather, font = ('Arial', 22), width = 238, height = 46, placeholder_text = 'Пошук', corner_radius = 20, fg_color = '#096C82', border_color = '#b5d3d9', border_width = 3)
search_entry.place(x = 645, y = 45)
path_image3 = os.path.abspath(__file__ + '/../../weather/loope.png')
image3 = PIL.Image.open(path_image3)
image3 = image3.resize([42, 33])
image3 = PIL.ImageTk.PhotoImage(image3)
search_loope = CTkLabel(frame_weather, image = image3, text = '', bg_color = '#096C82')
search_loope.place(x = 831, y = 51)
frame_current_position = CTkFrame(frame_weather, 315, 275, fg_color = '#5DA7B1')
frame_current_position.place(x = 300, y = 120)