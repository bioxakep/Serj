from config import WEATHER_API
appid = WEATHER_API  # полученный при регистрации на OpenWeatherMap.org. Что-то вроде такого набора букв и цифр: "6d8e495ca73d5bbc1d6bf8ebd52c4123"

import requests


class WeatherMan:
    def __init__(self, city_name):
        self.weather_desc = ''
        self.wind_speed = 0
        self.wind_dir = ''
        self.wind_deg = 0
        self.curr_temp = 0
        try:
            self.city_id = self.get_city_id(city_name)
            self.request_current_weather(self.city_id)
        except Exception as e:
            print(e)

    @staticmethod
    def get_wind_direction(deg):
        l = [' Северный', ' Северо-восточный', ' Восточный', 'Юго-востояный', ' Южный', ' Юго-западный', ' Западный',
             'Северо-западный']
        for i in range(0, 8):
            step = 45.
            min = i * step - 45 / 2.
            max = i * step + 45 / 2.
            if i == 0 and deg > 360 - 45 / 2.:
                deg = deg - 360
            if deg in range(int(min), int(max)+1):
                return l[i]
        return 'Н/У'

    # Проверка наличия в базе информации о нужном населенном пункте
    @staticmethod
    def get_city_id(city_name):
        city_id = None
        try:
            res = requests.get("http://api.openweathermap.org/data/2.5/find",
                               params={'q': city_name, 'type': 'like', 'units': 'metric', 'lang': 'ru', 'APPID': appid})
            data = res.json()
            cities = ["{} ({})".format(d['name'], d['sys']['country'])
                      for d in data['list']]
            print("city:", cities)
            city_id = data['list'][0]['id']
            print('city_id=', city_id)
        except Exception as e:
            print("Exception (find):", e)
            pass
        assert isinstance(city_id, int)
        return city_id

    # Запрос текущей погоды
    def request_current_weather(self, city_id):
        try:
            res = requests.get("http://api.openweathermap.org/data/2.5/weather",
                               params={'id': city_id, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
            data = res.json()
            print("conditions:", data['weather'][0]['description'])
            self.weather_desc = data['weather'][0]['description']
            print("temp:", data['main']['temp'])
            self.curr_temp = round(data['main']['temp'])
            # print("temp_min:", data['main']['temp_min'])
            # print("temp_max:", data['main']['temp_max'])
            self.wind_speed = data['wind']['speed']
            self.wind_deg = data['wind']['deg']
            self.wind_dir = self.get_wind_direction(self.wind_deg)
            print("data:", data)
            # data:
            # {'coord': {'lon': 37.62, 'lat': 55.75},
            #           'weather': [{'id': 803, 'main': 'Clouds', 'description': 'пасмурно', 'icon': '04d'}],
            #           'base': 'stations',
            #           'main': {'temp': 11.6, 'pressure': 1009, 'humidity': 54, 'temp_min': 11, 'temp_max': 12},
            #           'visibility': 10000, 'wind': {'speed': 7, 'deg': 280}, 'clouds': {'all': 75},
            #           'dt': 1568900463, 'sys':
            #               {'type': 1, 'id': 9029, 'message': 0.0064, 'country': 'RU',
            #               'sunrise': 1568862483, 'sunset': 1568907545},
            #           'timezone': 10800, 'id': 524901, 'name': 'Moscow', 'cod': 200
            #           }
        except Exception as e:
            print("Exception (weather):", e)
            pass

    # Прогноз
    def request_forecast(self, city_id):
        try:
            res = requests.get("http://api.openweathermap.org/data/2.5/forecast",
                               params={'id': city_id, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
            data = res.json()
            print('city:', data['city']['name'], data['city']['country'])
            for i in data['list']:
                print((i['dt_txt'])[:16], '{0:+3.0f}'.format(i['main']['temp']),
                      '{0:2.0f}'.format(i['wind']['speed']) + " м/с",
                      self.get_wind_direction(i['wind']['deg']),
                      i['weather'][0]['description'])
        except Exception as e:
            print("Exception (forecast):", e)
            pass
