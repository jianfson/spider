# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class SourcePipeline(object):
    def process_item(self, item, spider):
        if isinstance(item, SourceItem):
            ## 在此可进行文件写入、数据库写入等操作
            pass
        return item
