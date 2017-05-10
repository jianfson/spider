import threading
import time
import sys
import os
reload(sys);  
sys.setdefaultencoding('utf8');
def fun_timer():
    print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
    os.system("scrapy crawl NgaSpider")
    global timer
    timer = threading.Timer(10, fun_timer)
    timer.start()

timer = threading.Timer(0.02, fun_timer)
timer.start()

time.sleep(200)
timer.cancel()


