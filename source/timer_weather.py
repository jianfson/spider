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
print time.localtime(time.time())
weather.weather_func( '2017-05-12 17:00:00' )
#schedule.every().hour.do(fun_timer)
#schedule.every().day.at("17:00").do(fun_timer)
#while True:
#    schedule.run_pending()
#    time.sleep(1)
