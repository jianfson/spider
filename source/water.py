#!/usr/bin/env python
# coding=utf-8
# agri.gov.cn_amf_client.py
# http://jgsb.agri.gov.cn/flexapps/hqApp.swf数据抓取

import urllib
import urllib2
import os, re
from BeautifulSoup import BeautifulSoup
import requests
import json

url = 'http://221.237.179.75:9090/scszjcsj/szjc_sj/DataPublish/preview.xhtml'
body = {"id": "j_id_3", "name": "j_id_3"}
headers = {'Accept': "application/xml, text/xml, */*; q=0.01",
           'Accept-Encoding': "gzip, deflate",
           'Accept-Language': "en-US,en;q=0.5",
           'Cache-Control': "max-age=0",
           'Connection': "keep-alive",
           'Content-Length': "232",
           'Content-Type': "application/x-www-form-urlencoded; charset=UTF-8",
           'Cookie': "JSESSIONID=404E8DE3C526DADF993C16C42DAB38AB; oam.Flash.RENDERMAP.TOKEN=17nl37pn48",
           'Faces-Request': "partial/ajax",
           'Host': "221.237.179.75:9090",
           'Referer': "http://221.237.179.75:9090/scszjcsj/szjc_sj/DataPublish/preview.xhtml",
           'User-Agent': "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:59.0) Gecko/20100101 Firefox/59.0",
           'X-Requested-With': "XMLHttpRequest"}
 
#print type(body)
#print type(json.dumps(body))
# 这里有个细节，如果body需要json形式的话，需要做处理
# 可以是data = json.dumps(body)
response = requests.post(url, data = body, headers = headers)
# 也可以直接将data字段换成json字段，2.4.3版本之后支持
# response  = requests.post(url, json = body, headers = headers)
 
# 返回信息
print response.text
# 返回响应头
print response.status_code
