# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from datetime import datetime, time
import logging
import pytz

from scrapy.exceptions import DropItem
from icalendar import Event


"""
BEGIN:VCALENDAR
VERSION:2.0
PRODID:-//My calendar//EN//
BEGIN:VEVENT
SUMMARY:
DTSTAMP:
DESCRIPTION:
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

    def process_item(self, item, spider):
        if item.keys():
            summary = '{0} - {1}'.format(item.get('localteam'), item.get('foreignteam'))
            mday = item.get('day')[0]
            mtime = item.get('time', 'N/A')[0]
            if isinstance(mtime, time):
                dtstart = datetime.combine(mday, mtime, tzinfo=pytz.UTC)
            else:
                dtstart = datetime(mday.year, mday.month, mday.day, tzinfo=pytz.UTC)
            description = item.get('finalscore')
            match = Event()
            match.add('summary', summary)
            match.add('dtstart', dtstart)
            match.add('dtstamp', datetime.now(tz=pytz.UTC))
            match.add('description', description)
            self.zgzcalendar.add_component(match)
        else:
            raise DropItem('No match event details')
