import datetime

import scrapy
from scrapy.loader.processors import Join

from pygoza.items import ZaragozaMatchItem, ZaragozaMatchItemLoader

class MatchesSpider(scrapy.Spider):

    name = "matches"
    start_urls = [
            'https://www.laliga.es/en/laliga-123/zaragoza/calendar'
        ]

    def parse(self, response):
        matches = response.xpath('//div[starts-with(@class, "partido")]')
        for match in matches:
            matchloader = ZaragozaMatchItemLoader(ZaragozaMatchItem(), match)
            matchloader.add_css('weekday', 'span.letra::text')
            matchloader.add_css('day', 'span.dia::text')
            matchloader.add_css('time', 'span.hora::text')
            localteamloader = matchloader.nested_xpath('.//span[@class="equipo local"]')
            localteamloader.add_xpath('localteam', './/span[@class="team"]/text()')
            foreignteamloader = matchloader.nested_xpath('.//span[@class="equipo visitante"]')
            foreignteamloader.add_xpath('foreignteam', './/span[@class="team"]/text()')
            matchloader.add_xpath('finalscore', './/strong/text()')
            yield matchloader.load_item()

    def get_final_score(self, match):
        """
        Extracts final score from match details.
        :param match: Full match details.
        :return: String final score.
        """
        fscoreprocessor = Join(' - ')
        fscore = fscoreprocessor(match.xpath('.//strong/text()').extract())
        return fscore

    def get_match_time(self, match):
        """
        Extracts match time from match details.
        :param match: Full match details.
        :return: datetime.time object with hour and minutes.
        """
        hour, minutes = map(int, match.css('span.hora::text').extract_first().strip(' ·').split(':'))
        matchtime = datetime.time(hour, minutes)
        return matchtime
