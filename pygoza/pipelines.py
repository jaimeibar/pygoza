# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import logging

from icalendar import Event


"""
BEGIN:VCALENDAR
VERSION:2.0
PRODID:<ENTER INFORMATION HERE>
BEGIN:VEVENT
END:VEVENT
END:VCALENDAR
"""


logger = logging.getLogger(__name__)


class PygozaPipeline(object):

    def __init__(self, zgzcalendar):
        self.zgzcalendar = zgzcalendar

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            zgzcalendar=getattr(crawler.spider, 'calendar')
        )

    def open_spider(self, spider):
        self.calendarfile = open('zgzcalendar.ics', 'wb')

    def close_spider(self, spider):
        self.calendarfile.close()

    def process_item(self, item, spider):
        match = Event()
        for k, v in item.items():
            match.add(k, v)
        self.zgzcalendar.add_component(match)
        self.calendarfile.write(self.zgzcalendar.to_ical())
