# -*- coding: utf-8 -*-

"""Console script for pygoza."""

import logging
import logging.config
from pathlib import Path
import sys

import click

from pygoza.logconfig import logging_config
from pygoza import __version__
from pygoza import settings as pygozasettings

from pygoza.pipelines import PygozaPipeline  # noqa: I202
from pygoza.spiders.matches import MatchesSpider

from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings


logging.config.dictConfig(logging_config)
logger = logging.getLogger('scrapy')


@click.command()
@click.version_option(version=__version__)
@click.option('-o', '--output', 'foutput', type=click.File('wb'),
              default='pygoza.ics', show_default=True,
              help='File name of the ics file')
@click.option('-p', '--path', 'fpath', type=click.Path(exists=True, writable=True),
              default=Path.cwd(), show_default=True,
              help='Path where the ics file will be saved. Default current path.')
@click.option('-d', '--debug', type=click.BOOL, default=False, is_flag=True,
              help='Enable debug mode.')
def main(foutput, fpath, debug):
    """Console script for pygoza."""
    fpath = Path(fpath) if not isinstance(fpath, Path) else fpath
    if debug:
        logger.setLevel(logging.DEBUG)
        logger.debug('Output file name: {}'.format(foutput.name))
        logger.debug('Path: {}'.format(fpath.as_posix()))
        logger.debug('Full path and filename: {}'.format(fpath.joinpath(foutput.name)))
    setattr(PygozaPipeline, 'pygozaoutputfile', foutput)
    setattr(PygozaPipeline, 'pygozaoutputfilepath', fpath)
    pygoza_crawler_settings = Settings()
    pygoza_crawler_settings.setmodule(pygozasettings)
    process = CrawlerProcess(settings=pygoza_crawler_settings)
    process.crawl(MatchesSpider)
    process.start()
    return 0


if __name__ == '__main__':
    sys.exit(main())
