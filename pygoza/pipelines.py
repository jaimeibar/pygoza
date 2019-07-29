# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from datetime import datetime, time, timedelta
import logging
import os.path
import uuid
import os

from scrapy.exceptions import DropItem
from icalendar import Event
import pytz


"""
BEGIN:VCALENDAR
VERSION:2.0
PRODID:-//My calendar//EN//
BEGIN:VEVENT
SUMMARY:
UUID:
DTSTART:
DTEND:
DTSTAMP:
DESCRIPTION:
END:VEVENT
END:VCALENDAR
"""


logger = logging.getLogger(__name__)

# Match time duration.
MATCHTIME = timedelta(hours=2)


class PygozaPipeline(object):

    def __init__(self, zgzcalendar):
        self.zgzcalendar = zgzcalendar
        self.zgzcalendarfname = getattr(self, 'pygozaoutputfile')
        self.zgzcalendarfpath = getattr(self, 'pygozaoutputfilepath')

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            zgzcalendar=getattr(crawler.spider, 'calendar')
        )

    def close_spider(self, spider):
        # TODO Rewrite with try - except instead and pathlib.Path library.
        if os.access(self.zgzcalendarfpath, os.W_OK):
            # with open(os.path.join(self.zgzcalendarfpath, self.zgzcalendarfname), 'wb') as cfile:
            # cfile.write(self.zgzcalendar.to_ical())
            self.zgzcalendarfname.write(self.zgzcalendar.to_ical())
        else:
            logger.error('Folder {0} not writable'.format(self.zgzcalendarfpath))

    def process_item(self, item, spider):
        if item.keys():
            summary = '{0} - {1}'.format(item.get('localteam'), item.get('foreignteam'))
            mday = item.get('day')[0]
            mtime = item.get('time', 'N/A')[0]
            if isinstance(mtime, time):
                dtstart = datetime.combine(mday, mtime, tzinfo=pytz.UTC)
                dtend = dtstart + MATCHTIME
            else:
                dtstart = datetime(mday.year, mday.month, mday.day, tzinfo=pytz.UTC)
                dtend = dtstart
            finalscore = 'Final score: {0}'.format(item.get('finalscore', 'Not played yet'))
            tv = 'TV: {0}'.format(item.get('tv', 'Not available yet'))
            description = '{0}\n{1}'.format(finalscore, tv)
            match = Event()
            match.add('summary', summary)
            match.add('uid', uuid.uuid4())
            match.add('dtstart', dtstart)
            match.add('dtend', dtend)
            match.add('dtstamp', datetime.now(tz=pytz.UTC))
            match.add('description', description)
            self.zgzcalendar.add_component(match)
        else:
            raise DropItem('No match event details found')
