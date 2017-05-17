#coding=utf-8
import sys
import ttk
import time 
import threading
import Tkinter as Tk
import Tkinter as tk

reload(sys);
sys.setdefaultencoding('utf8');

isOpened = threading.Event()

RBuf = ''

root = Tk.Tk()
ComS = Tk.StringVar(root,'00:00')
ComX = Tk.StringVar(root,'1')
# Baud = Tk.StringVar(root,"9600")
# Dbit = Tk.StringVar(root,'8')
# Sbit = Tk.StringVar(root,'1')
# Chck = Tk.StringVar(root,'None')
# HexD = Tk.BooleanVar(root,False)
# HexO = Tk.BooleanVar(root,False)
Open = Tk.StringVar(root,u'打开定时器')



def main():
	root.title("网页爬虫")

	#global txt1
	
	txt1 = Tk.Text(root,width=81,border=5)
	txt1.pack(side='top',padx=3,pady=1,anchor='c')
	
	cnv1 = tk.Canvas(root,height=26,width=580)
	cnv1.pack(side='top',padx=0,pady=0,anchor='c')
	cnv1.create_window(120,15,window=ttk.Label(root,text=u'起始时间(时:分)：'))
	cnv1.create_window(220,15,window=ttk.Combobox(root,textvariable=ComS,values=['00:00', '01:00', '02:00','03:00'],width=12))
	cnv1.create_window(337,15,window=ttk.Button(root,text=u'手动抓取',width=12))
	cnv1.create_window(422,15,window=ttk.Button(root,text=u'清除日志',width=9))
	# cnv1.create_window(547,15,window=ttk.Checkbutton(root,text=u'HEX显示',variable=HexD,onvalue=True,offvalue=False))
	
	cnv2 = tk.Canvas(root,height=26,width=580)
	cnv2.pack(side='top',padx=0,pady=0,anchor='c')
	cnv2.create_window(120,15,window=ttk.Label(root,text=u'间隔时间(小时)：'))
	cnv2.create_window(220,15,window=ttk.Combobox(root,textvariable=ComX,values=['1', '2', '3','4'],width=12))
	# cnv2.create_window(202,15,window=ttk.Label(root,text=u'间隔时间(小时)：'))
	# cnv2.create_window(277,15,window=ttk.Combobox(root,textvariable=Baud,values=['4800','9600','19200'],width=12))
	cnv2.create_window(348,15,window=ttk.Button(root,textvariable=Open,width=16,command=lambda:COMOpen(cnv2)))
	cnv2.create_oval(420,7,436,23,fill='black',tag='led')
	# cnv2.create_window(547,15,window=ttk.Checkbutton(root,text=u'HEX发送',variable=HexO,onvalue=True,offvalue=False))
	
	# cnv3 = tk.Canvas(root,height=26,width=580)
	# cnv3.pack(side='top',padx=0,pady=0,anchor='c')
	# cnv3.create_window( 30,15,window=ttk.Label(root,text=u'数据位：'))
	# cnv3.create_window(105,15,window=ttk.Combobox(root,textvariable=Dbit,values=['9','8','7','6','5'],width=12))
	# cnv3.create_window(202,15,window=ttk.Label(root,text=u'停止位：'))
	# cnv3.create_window(277,15,window=ttk.Combobox(root,textvariable=Sbit,values=['1','2'],width=12))
	# cnv3.create_window(370,15,window=ttk.Label(root,text=u'校验位：'))
	# cnv3.create_window(445,15,window=ttk.Combobox(root,textvariable=Chck,values=['None','Odd','Even','Mark','Space'],width=12))
	# cnv3.create_window(547,15,window=ttk.Button(root,text=u'扩展',width=9))

	global args
	args = int(ComX.get())

	com_thread = threading.Thread(target=COMTrce)
	com_thread.setDaemon(True)
	com_thread.start()

	#RBuf = 'test他'
	#txt1.insert("insert",RBuf)

	root.bind("<<COMRxRdy>>",lambda e: txt1.insert("insert",RBuf))

	  
	root.mainloop()

#COM = serial.Serial()
def COMOpen(cnv2):
	#print "COM Open Error!"
	#pass
	if not isOpened.isSet():
		#RBuf = '操作：打开定时器\n'
		#txt1.insert('操作：打开定时器\n')
		# try:
		# 	com_thread.start()
		# 	# COM.timeout = 1
		# 	# COM.xonxoff = 0	
		# 	# COM.port = ComX.get()
		# 	# COM.parity = Chck.get()[0]
		# 	# COM.baudrate = int(Baud.get())
		# 	# COM.bytesize = int(Dbit.get())
		# 	# COM.stopbits = int(Sbit.get())
		# 	# COM.open()
		# except Exception:
		# 	print "COM Open Error!"
		# 	print Exception
		# else:
		#print ComX.get()
		#args = int(ComX.get())
		isOpened.set()
		Open.set(u'关闭定时器')
		#ComX.configure(state='disabled')
		cnv2.itemconfig('led',fill='green')
	else:
		#RBuf = RBuf + '操作：关闭定时器\n'
		isOpened.clear()
		Open.set(u'打开定时器')
		cnv2.itemconfig('led',fill='black')

def COMTrce():
	while True:
		if isOpened.isSet():
			time.sleep(args)
			RBuf = 'test...\n'
			root.event_generate("<<COMRxRdy>>")
			print "test...."
		else:
			args = int(ComX.get())
		time.sleep(0.05)


if __name__=='__main__':
	isOpened.clear()
	main()