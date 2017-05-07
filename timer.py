import threading
import time
from xlwt import *
from datetime import datetime
file = Workbook(encoding = 'utf-8')      #指定file以utf-8的格式打开
table = file.add_sheet('爬虫数据')            #打开文件名称
a,b=eval(input("请输入时间间隔和结束时间："))
def fun_timer():
    w = Workbook()
    ws = w.add_sheet('Hey, Dude')
    fmts = [
    'M/D/YY',
    'D-MMM-YY',
    'D-MMM',
    'MMM-YY',
    'h:mm AM/PM',
    'h:mm:ss AM/PM',
    'h:mm',
    'h:mm:ss',
    'M/D/YY h:mm',
    'mm:ss',
    '[h]:mm:ss',
    'mm:ss.0',
   ]

    i = 0
    for fmt in fmts:
       ws.write(i, 0, fmt)

       style = XFStyle()
       style.num_format_str = fmt

       ws.write(i, 4, datetime.now(), style)

       i += 1

    w.save('dates.xls')
    
    print('Hello Timer!')
    print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
    global timer
    timer = threading.Timer(a, fun_timer)
    timer.start()

timer = threading.Timer(0.02, fun_timer)
timer.start()

time.sleep(b)
timer.cancel()


