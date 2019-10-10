from weather import WeatherMan
from speech import Serj
from task import TaskManager
from datetime import datetime, timedelta


if __name__ == '__main__':
    wm = WeatherMan('Moscow')
    serj = Serj()
    serj.set_rate(200)
<<<<<<< HEAD
    serj.say_humidity(wm.curr_hum)
    serj.say_pressure(wm.curr_pres)
    '''
    serj.say_hello('Варвара')
=======
    serj.say_hello('Александр')
>>>>>>> f581ba988765635bc481a2343e7c622120fa2cc6
    serj.say_today_date()
    serj.say_time()
    serj.say_weather(wm.curr_temp, wm.curr_hum, wm.curr_pres, wm.wind_speed, wm.wind_dir, wm.weather_desc)
    tm = TaskManager()
    tm.create_task('Приготовить бабушке подарок', datetime.strptime("19.10.2019", "%d.%m.%Y").date())
    if tm.check_active_tasks():
        task_list = tm.get_active_tasks()
        serj.say('У вас есть активные задачи')
        for t in task_list:
            serj.say_task(t.text, t.datetime)
    '''
