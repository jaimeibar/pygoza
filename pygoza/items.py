# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import datetime
import logging
import pytz

import scrapy
from scrapy.loader import ItemLoader
from scrapy.loader.processors import Compose, MapCompose, Join, TakeFirst

logger = logging.getLogger(__name__)


def get_match_day(day):
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
        return None
    mtime = mtime[0]
    hour, minutes = map(int, mtime.strip(' ·').split(':'))
    matchtime = datetime.time(hour, minutes, tzinfo=pytz.UTC)
    return matchtime


def filter_match_result(result):
    """
    Filter match result in case of unexpected values like
    ['R. Zaragoza', '2', '1'] due to an extra strong tag
    in some matches details.
    :param result: Match result.
    :return: Match result of the form ['2', '1']
    """
    return None if not result.isdigit() else result.strip()


class ZaragozaMatchItem(scrapy.Item):
    day = scrapy.Field()
    time = scrapy.Field()
    localteam = scrapy.Field()
    foreignteam = scrapy.Field()
    finalscore = scrapy.Field()
    tv = scrapy.Field()


class ZaragozaMatchItemLoader(ItemLoader):
    default_item_class = ZaragozaMatchItem
    day_in = MapCompose(str.strip, get_match_day)
    time_in = Compose(get_match_time)
    localteam_out = TakeFirst()
    foreignteam_out = TakeFirst()
    finalscore_in = MapCompose(filter_match_result)
    finalscore_out = Join(' - ')
    tv_in = Compose(lambda t: t[0].strip() if t else None)
    tv_out = TakeFirst()
