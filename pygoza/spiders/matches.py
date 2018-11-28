import scrapy

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
            matchloader.add_xpath('time', './/span[@class="fecha"]/span[@class="hora"]/text()')
            localteamloader = matchloader.nested_xpath('.//span[@class="equipo local"]')
            localteamloader.add_xpath('localteam', './/span[@class="team"]/text()')
            foreignteamloader = matchloader.nested_xpath('.//span[@class="equipo visitante"]')
            foreignteamloader.add_xpath('foreignteam', './/span[@class="team"]/text()')
            matchloader.add_xpath('finalscore', './/strong/text()')
            yield matchloader.load_item()
