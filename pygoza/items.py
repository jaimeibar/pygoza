# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ZaragozaMatchItem(scrapy.Item):
    weekday = scrapy.Field()
    matchday = scrapy.Field()
    matchtime = scrapy.Field()
    localteam = scrapy.Field()
    foreignteam = scrapy.Field()
