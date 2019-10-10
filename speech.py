import pyttsx3
from datetime import datetime


# from gtts import gTTS # IF NEED SAVE VOICE TO FILE


class Serj:
    # 'час', 'часа', 'часов' : 'минута', 'минуты', 'минут' : 'секунда', 'секунды', 'секунд'
    # 'часа', 'часов', 'часов' : 'минуты', 'минут', 'минут' : 'секунды', 'секунд', 'секунд'
    ends_dict = {1: 0, 2: 1, 3: 1, 4: 1, 5: 2, 6: 2, 7: 2, 8: 2, 9: 2, 0: 2}
    hour_ends = [' час ', ' часа ', ' часов ']
    minute_ends = [' минута ', ' минуты ', ' минут ']
    second_ends = [' секунда ', ' секунды ', ' секунд ']
    temp_ends = [' градус ', ' градуса ', ' градусов ']
    pres_ends = [' миллиметр ', ' миллиметра ', ' миллиметров ']
    procent_ends = [' процент ', ' процента ', ' процентов ']
    meters_ends = [' метр ', ' метра ', ' метров ']
    week_days = ['понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота', 'воскресенье']

    def __init__(self):
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 180)  # Speed percent (can go over 100)
        self.engine.setProperty('volume', 0.9)  # Volume 0-1

    def say(self, text):
        self.engine.say(text)
        self.engine.runAndWait()

    def set_volume(self, vol):
        if vol in range(0, 100):
            self.engine.setProperty('volume', vol / 100)  # Volume 0-1
        else:
            self.say('Громкость должна быть в пределах от нуля до ста')

    def set_rate(self, rate):
        if rate in range(100, 250):
            self.engine.setProperty('rate', rate)  # Speed percent (can go over 100)
        else:
            self.say('Скорость должна быть в пределах от ста до двухсотпятидесяти')

    def say_hello(self, name):
        hello_text = name + ', '
        hour = datetime.now().time().hour
        if hour in range(10, 17):
            hello_text += 'Добрый день'
        elif hour in range(6, 10):
            hello_text += 'Доброе утро'
        elif hour in range(17, 23):
            hello_text += 'Добрый вечер'
        else:
            hello_text += 'Доброй ночи'
        self.say(hello_text)

    def say_today_date(self):
        date = datetime.today()
        year, month, day = str(date.year), str(date.month), str(date.day)
        day_of_week = Serj.week_days[date.weekday()]
        text = 'Сегодня {}, '.format(day_of_week) + '.'.join([day, month, year]) + ' года'
        self.say(text)

    def say_time(self):
        date = datetime.now()
        hour, minute = date.hour, date.minute
        text = 'Текущее время ' + str(hour) + self.word_ends(hour, Serj.hour_ends) \
               + str(minute) + self.word_ends(minute, Serj.minute_ends)
        self.say(text)

    def say_temp(self, temp):
        temp_end = self.word_ends(temp, Serj.temp_ends)
        text = f'Температура воздуха {temp} {str(temp_end)} по Цельсию'
        self.say(text)

    def say_humidity(self, humidity):
        hum_end = self.word_ends(humidity, Serj.procent_ends)
        text = f'Влажность воздуха {humidity} {str(hum_end)}'
        self.say(text)

    def say_pressure(self, press):
        pres_ends = self.word_ends(press, Serj.pres_ends)
        text = f'Давление {press} {str(pres_ends)} ртутного столба'
        self.say(text)

    def say_weather(self, temp, hum, press, wind_speed, wind_dir, description):
        self.say(f'На улице {description}')
        self.say_temp(temp)
        self.say_humidity(hum)
        self.say_pressure(press)
        wind_text = f'Ветер {wind_dir}, {wind_speed} {self.word_ends(wind_speed, Serj.meters_ends)} в секунду'
        self.say(wind_text)

    def say_task(self, task_text, task_datetime):
        self.say('Задача {} должна быть выполнена до {}.{}.{}'.format(task_text, task_datetime.day, task_datetime.month, task_datetime.year))

    def word_ends(self, n, end_list):
        n = int(n % 100)
        if n in range(5, 20):
            return str(end_list[2])
        else:
            i = n % 10
            #  print('Окончание: {}, число {}'.format(end_list[Serj.ends_dict[int(i)]], n))
            return str(end_list[Serj.ends_dict[int(i)]])
