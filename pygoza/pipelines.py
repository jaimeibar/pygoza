# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import logging

from icalendar import Calendar, Event


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

    def __init__(self):
        self.zgzcalendar = self.open_calendar()

    def open_spider(self, spider):
        self.file = open('zgzcalendar.ics', 'wb')

    def close_spider(self, spider):
        self.file.close()

    def open_calendar(self):
        cal = Calendar()
        return cal

    def process_item(self, item, spider):
        match = Event()
        for k, v in item.items():
            match.add(k, v)
        self.zgzcalendar.add_component(match)
        self.file.write(self.zgzcalendar.to_ical())