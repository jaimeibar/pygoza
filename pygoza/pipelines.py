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

    def open_spider(self, spider):
        self.file = open('zgzcalendar.ics', 'w')

    def close_spider(self):
        self.file.close()

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            zgzcalendar=crawler.get_calendar()
        )

    def process_item(self, item, spider):
        match = Event()
        for k, v in item.items():
            match.add(k, v)
        self.zgzcalendar.add_component(match)
        self.file.write(self.zgzcalendar.to_ical())
