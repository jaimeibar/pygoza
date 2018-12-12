import scrapy

from icalendar import Calendar

from pygoza.items import ZaragozaMatchItem, ZaragozaMatchItemLoader


class MatchesSpider(scrapy.Spider):

    name = "matches"
    start_urls = [
            'https://www.laliga.es/en/laliga-123/zaragoza/calendar'
        ]

    def __init__(self, *args, **kwargs):
        self._calendar = Calendar()
        super(MatchesSpider, self).__init__(*args, **kwargs)

    @property
    def calendar(self):
        return self._calendar

    def parse(self, response):
        matches = response.xpath('//div[starts-with(@class, "partido")]')
        for match in matches:
            matchloader = ZaragozaMatchItemLoader(ZaragozaMatchItem(), selector=match)
            matchloader.add_css('day', 'span.dia::text')
            matchloader.add_xpath('time', './/span[@class="fecha"]/span[@class="hora"]/text()')
            localteamloader = matchloader.nested_xpath('.//span[@class="equipo local"]')
            localteamloader.add_xpath('localteam', './/span[@class="team"]/text()')
            foreignteamloader = matchloader.nested_xpath('.//span[@class="equipo visitante"]')
            foreignteamloader.add_xpath('foreignteam', './/span[@class="team"]/text()')
            matchloader.add_xpath('finalscore', './/strong/text()')
            yield matchloader.load_item()
        self.write_calendar_to_file()

    def write_calendar_to_file(self):
        self.calendar.add('prodid', '-//My calendar//EN//')
        self.calendar.add('version', '2.0')
        cfile = open('zgzcalendar.ics', 'wb')
        cfile.write(self.calendar.to_ical())
        cfile.close()
