import time
import sys
import os
import schedule
reload(sys);  
sys.setdefaultencoding('utf8');
def fun_timer():
    print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
    os.system("scrapy crawl NgaSpider")

#timer = threading.Timer(0.02, fun_timer)
#timer.start()

#time.sleep(200)
#timer.cancel()
#weather.weather_func('2017-05-11 12:00:00')
schedule.every().day.at("00:00").do(fun_timer)
schedule.every().day.at("04:00").do(fun_timer)
schedule.every().day.at("08:00").do(fun_timer)
schedule.every().day.at("12:00").do(fun_timer)
schedule.every().day.at("16:00").do(fun_timer)
schedule.every().day.at("20:00").do(fun_timer)
while True:
    schedule.run_pending()
    time.sleep(1)

