from weather import WeatherMan
from speech import Serj
from task import TaskManager
from datetime import datetime, timedelta


def good_morning():
    wm = WeatherMan('Moscow')
    serj = Serj()
    serj.set_rate(200)
    serj.say_hello('Варвара')
    serj.say_today_date()
    serj.say_time()
    serj.say_weather(wm.curr_temp, wm.wind_speed, wm.wind_dir, wm.weather_desc)


if __name__ == '__main__':
    wm = WeatherMan('Moscow')
    serj = Serj()
    serj.set_rate(200)
    serj.say_hello('Варвара')
    serj.say_today_date()
    serj.say_time()
    serj.say_weather(wm.curr_temp, wm.wind_speed, wm.wind_dir, wm.weather_desc)
    tm = TaskManager()
    tm.create_task('Приготовить бабушке подарок', datetime.strptime("19.10.2019", "%d.%m.%Y").date())
    task_list = tm.get_active_tasks()
    if len(task_list) > 0:
        serj.say('У вас есть активные задачи')
        for t in task_list:
            serj.say_task(t.text, t.datetime)
