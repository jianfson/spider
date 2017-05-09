#!/usr/bin/env python
# coding=utf-8

from pyquery import PyQuery as pq  
import  pandas  as pd    
from  datetime import  datetime  
#import  MySQLdb  
  
shars_tabls=pd.DataFrame();  
code=[]  
name=[]  
indname=[]  
for i in range(1, 10):  
    urlxx = "http://yunvs.com/list/mai_" + str(i) + ".html"  
    v_source = pq(url=urlxx)    
    for data in v_source('tr'):  
            v_code = pq(data).find('td').eq(0).text()  
            v_name = pq(data).find('td').eq(1).text()  
            v_ind = pq(data).find('td').eq(5)  
            xx=[]  
            x=""  
            for i in range(len(pq(v_ind).find('a'))):  
                v_indname = pq(v_ind).find('a').eq(i).text()  
                xx.append(v_indname)  
                x=','.join(xx)  
            code.append(v_code)  
            name.append(v_name)  
            indname.append(x)  
data = {'v_code':code,'v_name':name,'v_ind':indname}  
frame =pd.DataFrame(data)  
frame1=frame[frame.v_name!=""]  
frame1.to_excel("shearstable.xls",encoding="utf-8",index=False)  
print("success")
