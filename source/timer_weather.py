#!/usr/bin/env python
# coding=utf-8
import schedule
import time
import sys
import weather
reload(sys);  
sys.setdefaultencoding('utf8');
def fun_timer():
    print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
    weather.weather_func( time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))  )
    #global timer
    #timer = threading.Timer(10, fun_timer)
    #timer.start()

#timer = threading.Timer(0.02, fun_timer)
#timer.start()

#time.sleep(200)
#timer.cancel()
#weather.weather_func('2017-05-11 12:00:00')

schedule.every().hour.do(fun_timer)
while True:
    schedule.run_pending()
    time.sleep(1)
