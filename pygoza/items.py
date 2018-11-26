# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import datetime

import scrapy
from scrapy.loader import ItemLoader
from scrapy.loader.processors import Join, Compose, MapCompose, TakeFirst


def format_match_day(day):
    """
    Converts string match day to datetime.date object
    :param day: Unformatted match day
    :return: datetime.date object year-month-day
    """
    day, month, year = map(int, day.split('-'))
    matchday = datetime.date(year, month, day)
    return matchday


class ZaragozaMatchItem(scrapy.Item):
    weekday = scrapy.Field()
    day = scrapy.Field()
    time = scrapy.Field()
    localteam = scrapy.Field()
    foreignteam = scrapy.Field()
    finalscore = scrapy.Field()


class ZaragozaMatchItemLoader(ItemLoader):
    default_item_class = ZaragozaMatchItem
    weekday_in = TakeFirst()
    # day_in = MapCompose(str.strip, format_match_day)
    """
    time_in
    localteam_in
    foreignteam_in
    finalscore_in
    """
