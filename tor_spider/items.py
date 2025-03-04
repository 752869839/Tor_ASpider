# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TorWholeNetworkItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    url = scrapy.Field()
    status = scrapy.Field()
    domain = scrapy.Field()
    description = scrapy.Field()
    title = scrapy.Field()
    html = scrapy.Field()
    language = scrapy.Field()
    img_url = scrapy.Field()
    encode = scrapy.Field()
    crawl_time = scrapy.Field()
