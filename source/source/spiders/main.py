#!/usr/bin/env python
# coding=utf-8

import sys
import scrapy
from scrapy import Selector
from scrapy import Request
from source.items import SourceItem

reload(sys);  
sys.setdefaultencoding('utf8');

class NgaSpider(scrapy.Spider):
    name = "NgaSpider"
    host = "http://bbs.ngacn.cc/"
    # 这个例子中只指定了一个页面作为爬取的起始url
    # 当然从数据库或者文件或者什么其他地方读取起始url也是可以的
    start_urls = [
        "http://www.scemc.cn:8383/websr/browser/webwater.jsp"
    ]

    # 爬虫的入口，可以在此进行一些初始化工作，比如从某个文件或者数据库读入起始url
    def start_requests(self):
        for url in self.start_urls:
            # 此处将起始url加入scrapy的待爬取队列，并指定解析函数
            # scrapy会自行调度，并访问该url然后把内容拿回来
            yield Request(url=url, callback=self.parse)

    # 版面解析函数，解析一个版面上的帖子的标题和地址
    def parse(self, response):
        excel_list=[]
        selector = Selector(response)
        tr_list = selector.xpath('.//tr')
        for tr in tr_list:
            temp_list=[]
            td_list = tr.xpath('.//td')
            len = 0
            for td in td_list:
                len=len+1
            if len==17:
                for td in td_list:
                    #print td.extract()
                    data_list = td.xpath('string(.)').extract()
                    for data in data_list:
                        #print data
                        temp_list.append(data)
            elif len==16:
                i=0
                for td in td_list:
                    if i==1:
                        temp_list.append("")
                    data_list = td.xpath('string(.)').extract()
                    for data in data_list:
                        #print data
                        temp_list.append(data)
                    i=i+1
            if temp_list != []:
                excel_list.append(temp_list)
        item = SourceItem()
        item["data"] = excel_list
        yield item
