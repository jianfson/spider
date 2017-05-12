#!/usr/bin/env python
# coding=utf-8
import schedule
import time
import datetime
import sys
import weather
reload(sys);  
sys.setdefaultencoding('utf8');
def fun_timer():
    now = datetime.datetime.now()
    oneHourAgo = (now - datetime.timedelta(hours = 1) - datetime.timedelta(minutes = now.minute) - datetime.timedelta(seconds = now.second))
    print oneHourAgo.strftime('%Y-%m-%d %H:%M:%S')
    weather.weather_func( oneHourAgo.strftime('%Y-%m-%d %H:%M:%S') )
now = datetime.datetime.now()
schedule.every().hour.do(fun_timer)
oneHourAgo = (now - datetime.timedelta(hours = 1) - datetime.timedelta(minutes = now.minute) - datetime.timedelta(seconds = now.second))
print oneHourAgo.strftime('%Y-%m-%d %H:%M:%S')
weather.weather_func( oneHourAgo.strftime('%Y-%m-%d %H:%M:%S') )
while True:
    schedule.run_pending()
    time.sleep(1)
