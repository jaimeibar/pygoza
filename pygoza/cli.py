# -*- coding: utf-8 -*-

import argparse
import os
import logging

from scrapy import cmdline

from pygoza import __version__
from pygoza.spiders.matches import MatchesSpider


logger = logging.getLogger(__name__)


def _parse_arguments():
    parser = argparse.ArgumentParser(description='Get ics file from match events')

    parser.add_argument('-v', '-version', action='version', version=__version__, help='Display the version')
    parser.add_argument('-n', '--name', action='store', dest='name',
                        default='zgzcalendar', help='Output file name')
    parser.add_argument('-p', '--path', action='store', dest='path',
                        default=os.getcwd(),
                        help='Path where the output file will be stored')
    parser.add_argument('-d', '--debug', action='store_true', help='Enable debug')

    return parser


def main():
    """
    Main function
    :return:
    """
    parser = _parse_arguments()
    arguments = parser.parse_args()
    fname = arguments.name
    fpath = arguments.path
    debugmode = arguments.debug
    crawlername = getattr(MatchesSpider, 'name')
    scrapycommand = 'scrapy crawl --nolog'
    if debugmode:
        scrapycommand = 'scrapy crawl'
    cmdline.execute((scrapycommand + ' ' + crawlername).split())


if __name__ == '__main__':
    main()
