#coding=utf-8
import sys
import os
import ttk
import time 
import threading
import Tkinter as Tk
import Tkinter as tk

reload(sys);
sys.setdefaultencoding('utf8');

isOpened = threading.Event()

RBuf = ''
StartTime = ''
start_manually = False

root = Tk.Tk()
ComS = Tk.StringVar(root,'00:00')
ComX = Tk.StringVar(root,'1')
ComL = Tk.StringVar(root,'http://118.122.118.75:8383/websr/browser/webwater.jsp')
Open = Tk.StringVar(root,u'打开定时器')



def main():
	root.title("水质检测数据")

	txt1 = Tk.Text(root,width=81,border=5)
	txt1.pack(side='top',padx=3,pady=1,anchor='c')
	
	cnv1 = tk.Canvas(root,height=26,width=580)
	cnv1.pack(side='top',padx=0,pady=0,anchor='c')
	cnv1.create_window(120,15,window=ttk.Label(root,text=u'起始时间(时:分)：'))
	cnv1.create_window(220,15,window=ttk.Combobox(root,textvariable=ComS,values=['00:00', '01:00', '02:00','03:00','04:00', '05:00', '06:00','07:00','08:00', '09:00', '10:00','11:00','12:00', '13:00', '14:00','15:00','16:00', '17:00', '18:00','19:00','20:00', '21:00', '22:00','23:00'],width=12))
        cnv1.create_window(337,15,window=ttk.Button(root,text=u'手动抓取',width=12,command=lambda:Start(cnv1)))
        cnv1.create_window(430,15,window=ttk.Button(root,text=u'清除日志',width=9,command=lambda:Clear(cnv1)))
	
	cnv2 = tk.Canvas(root,height=26,width=580)
	cnv2.pack(side='top',padx=0,pady=0,anchor='c')
	cnv2.create_window(120,15,window=ttk.Label(root,text=u'间隔时间(小时)：'))
	cnv2.create_window(220,15,window=ttk.Combobox(root,textvariable=ComX,values=['1', '2', '3','4'],width=12))
	cnv2.create_window(337,15,window=ttk.Button(root,textvariable=Open,width=12,command=lambda:COMOpen(cnv2)))
	cnv2.create_oval(420,7,436,23,fill='black',tag='led')
	
	cnv0 = tk.Canvas(root,height=26,width=580)
	cnv0.pack(side='top',padx=0,pady=0,anchor='c')
	cnv0.create_window(100,15,window=ttk.Label(root,text=u'抓取地址：'))
	# Adding a Textbox Entry widget
	cnv0.create_window(370,15,window=ttk.Entry(root,width=80,textvariable=ComL))

	global args
	args = int(ComX.get())
        
        StartTime = time.strftime('%Y-%m-%d ',time.localtime(time.time())) + ComS.get() + ':00' 
	com_thread = threading.Thread(target=COMTrce)
	com_thread.setDaemon(True)
	com_thread.start()


	root.bind("<<COMRxRdy>>",lambda e: txt1.insert("insert",RBuf))
        root.bind("<<DELETE>>",lambda e: txt1.delete(0.0,Tk.END))

	  
	root.mainloop()

def COMOpen(cnv2):
    global RBuf
    global StartTime
    if not isOpened.isSet():
        root.event_generate("<<DELETE>>")
	RBuf = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())) + ' 操作：打开定时器\n'
        StartTime = time.strftime('%Y-%m-%d ',time.localtime(time.time())) + ComS.get() + ':00'
        RBuf = RBuf + 'start time : ' + StartTime + '\n'
        now = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
        if now > StartTime:
            RBuf = RBuf + 'error : StartTime cannot be the time that has passed!!!'
        else:
            isOpened.set()
            Open.set(u'关闭定时器')
	    cnv2.itemconfig('led',fill='green')
        root.event_generate("<<COMRxRdy>>")
    else:
	RBuf = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())) + ' 操作：关闭定时器\n'
        root.event_generate("<<COMRxRdy>>")
	isOpened.clear()
	Open.set(u'打开定时器')
	cnv2.itemconfig('led',fill='black')

def COMTrce():
    global RBuf
    global start_manually
    global StartTime
    while True:
    	if start_manually == True:
	    start_manually = False
	    os.system("scrapy crawl NgaSpider")
	    time.sleep(0.05)
	if isOpened.isSet():
            now = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
            if now > StartTime:
	        RBuf = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())) + ' auto run spider begin...\n'
	        root.event_generate("<<COMRxRdy>>")
                os.system("scrapy crawl NgaSpider")
                RBuf = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())) + ' auto run spider end.\n'
	        root.event_generate("<<COMRxRdy>>")
                time.sleep(args*60*60)
	else:
	    args = int(ComX.get())
	    time.sleep(0.05)
def Start(cnv1):
    global RBuf
    global start_manually
    RBuf = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())) + ' run spider manually\n'
    root.event_generate("<<COMRxRdy>>")
    start_manually = True
    #os.system("scrapy crawl NgaSpider")

def Clear(cnv1):
    root.event_generate("<<DELETE>>")

if __name__=='__main__':
	isOpened.clear()
	main()
