# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
from pygoza import __version__


setup(name='pygoza',
      version=__version__,
      description='ics calendar file with Real Zaragoza matches times and dates.',
      long_description=open('README.md').read(),
      classifiers=[
          'Development Status :: 4 - Beta',
          'Environment :: Console',
          'Framework :: Scrapy',
          'Intended Audience :: End Users/Desktop',
          'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
          'Natural Language :: English',
          'Operating System :: OS Independent',
          'Programming Language :: Python :: 3.6',
          'Topic :: Utilities'
      ],
      keywords='',
      author='Jaime Ibar',
      author_email='jim2k7@gmail.com',
      url='https://github.com/jim3k1/pygoza',
      license='GPL2',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=[line for line in open('requirements.txt')],
      entry_points={
          'console_scripts': [
              'pygoza = pygoza.cli:main'
          ]

      })
