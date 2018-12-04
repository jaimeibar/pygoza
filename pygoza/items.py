# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import datetime
import logging

import scrapy
from scrapy.loader import ItemLoader
from scrapy.loader.processors import Compose, MapCompose, Identity, Join

from icalendar import Calendar

logger = logging.getLogger(__name__)


def format_match_day(day):
    """
    Converts string match day to datetime.date object
    :param day: Unformatted match day
    :return: datetime.date object year-month-day
    """
    day, month, year = map(int, day.split('-'))
    matchday = datetime.date(year, month, day)
    return matchday


def get_match_time(mtime):
    """
    Converts string time into datetime.time object
    :param mtime: Match time details.
    :return: datetime.time object with hour and minutes.
    """
    if not mtime or mtime == ' ':
        return 'N/A'
    mtime = mtime[0]
    hour, minutes = map(int, mtime.strip(' ·').split(':'))
    matchtime = datetime.time(hour, minutes)
    return matchtime


class ZaragozaMatchItem(scrapy.Item):
    weekday = scrapy.Field()
    day = scrapy.Field()
    time = scrapy.Field()
    localteam = scrapy.Field()
    foreignteam = scrapy.Field()
    finalscore = scrapy.Field()


class ZaragozaMatchItemLoader(ItemLoader):
    default_item_class = ZaragozaMatchItem
    weekday_in = Identity()
    day_in = MapCompose(str.strip, format_match_day)
    time_in = Compose(get_match_time)
    localteam_in = Identity()
    foreignteam_in = Identity()
    finalscore_in = Compose(MapCompose(lambda v: v.strip()), Join(' - '))
