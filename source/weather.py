#!/usr/bin/env python
# coding=utf-8
# agri.gov.cn_amf_client.py
# http://jgsb.agri.gov.cn/flexapps/hqApp.swf数据抓取

import urllib2
import uuid
import pyamf
import json
from pyamf import remoting
from pyamf.flex import messaging


# 构造flex.messaging.messages.RemotingMessage消息
msg = messaging.RemotingMessage(messageId=str(uuid.uuid1()).upper(),
                                clientId=str(uuid.uuid1()).upper(),
                                operation='queryAutoStationByTime',
                                destination='RealtimeDataQuery',
                                timeToLive=0,
                                timestamp=0)
# 第一个是查询参数，第二个是页数，第三个是控制每页显示的数量（默认每页只显示15条）
msg.body = ['2017-05-11 12:00:00','null', None]
msg.headers['DSEndpoint'] = None
msg.headers['DSId'] = str(uuid.uuid1()).upper()
# 按AMF协议编码数据
req = remoting.Request('null', body=(msg,))
env = remoting.Envelope(amfVersion=pyamf.AMF3)
env.bodies = [('/1', req)]
data = bytes(remoting.encode(env).read())

# 提交请求
url = 'http://resource.cdtq.gov.cn:8080/CDPubServiceWebSite/messagebroker/amf'
req = urllib2.Request(url, data, headers={'Content-Type': 'application/x-amf'})
print req
# 解析返回数据
opener = urllib2.build_opener()
print opener

# 解码AMF协议返回的数据
resp = remoting.decode(opener.open(req).read())
excel = resp.bodies[0][1].body.body
#print excel
jo=json.loads(excel)
#print jo['weather']
excel_data = jo['weather']
#print excel_data[0]['stationname']
i=0
while i<len(excel_data):
    print i, excel_data[i]['stationname'], '\n'
    i=i+1

#for stationname in excel_data:
#    print excel_data['stationname']
#          record['marketName'], \
#          record['maxPrice'], \
#          record['minPrice'], \
#          record['averagePrice'], \
#          record['producAdd'] and record['producAdd'], \
#          record['reportMan']<br>
