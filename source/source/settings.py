# -*- coding: utf-8 -*-

# Scrapy settings for source project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'source'

SPIDER_MODULES = ['source.spiders']
NEWSPIDER_MODULE = 'source.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'source (+http://www.yourdomain.com)'

ITEM_PIPELINES = {
            'source.pipelines.SourcePipeline': 400,
        }
