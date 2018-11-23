import datetime

import scrapy
from scrapy.loader import ItemLoader

from pygoza.items import ZaragozaMatchItem

class MatchesSpider(scrapy.Spider):

    name = "matches"
    start_urls = [
            'https://www.laliga.es/en/laliga-123/zaragoza/calendar'
        ]

    def parse(self, response):
        matches = response.xpath('//div[starts-with(@class, "partido")]')
        for match in matches:
            yield {
                'date': self.get_match_day(match),
                'time': self.get_match_time(match),
                'localteam': match.xpath('.//span[@class="equipo local"]').xpath('.//span[@class="team"]/text()').extract_first(),
                'foreignteam': match.xpath('.//span[@class="equipo visitante"]').xpath('.//span[@class="team"]/text()').extract_first(),
                'finalscore': ' - '.join(match.xpath('.//strong/text()').extract())
            }

    def get_match_day(self, match):
        """
        Extracts match day from match details.
        :param match: Full match details.
        :return: datetime.date object with hour and minutes.
        """
        year, month, day = map(int, match.css('span.hora::text').extract_first().strip(' ').split('-'))
        matchday = datetime.date(year, month, day)
        return matchday

    def get_match_time(self, match):
        """
        Extracts match time from match details.
        :param match: Full match details.
        :return: datetime.time object with hour and minutes.
        """
        hour, minutes = map(int, match.css('span.hora::text').extract_first().strip(' ·').split(':'))
        matchtime = datetime.time(hour, minutes)
        return matchtime
