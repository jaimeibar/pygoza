# -*- coding: utf-8 -*-

import argparse
import os
import logging

from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings

from pygoza import __version__
from pygoza.spiders.matches import MatchesSpider
from pygoza.pipelines import PygozaPipeline
from pygoza import settings as pygozasettings


logger = logging.getLogger(__name__)


def _parse_arguments():
    parser = argparse.ArgumentParser(description='Get ics file from match events')

    parser.add_argument('-v', '-version', action='version', version=__version__, help='Display the version')
    parser.add_argument('-o', '--output', action='store', dest='output',
                        default='zgzcalendar.ics', help='Output file name. Default zgzcalendar.ics')
    parser.add_argument('-p', '--path', action='store', dest='path',
                        default=os.getcwd(),
                        help='Path where the output file will be stored. Default current path. {0}'.format(os.getcwd()))
    parser.add_argument('-d', '--debug', action='store_true', help='Enable debug')

    return parser


def main():
    """
    Main function
    :return:
    """
    parser = _parse_arguments()
    arguments = parser.parse_args()
    foutput = arguments.output
    fpath = arguments.path
    # debugmode = arguments.debug
    setattr(PygozaPipeline, 'pygozaoutputfile', foutput)
    pygoza_crawler_settings = Settings()
    pygoza_crawler_settings.setmodule(pygozasettings)
    process = CrawlerProcess(settings=pygoza_crawler_settings)
    process.crawl(MatchesSpider)
    process.start()


if __name__ == '__main__':
    main()
