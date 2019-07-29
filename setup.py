#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['Click>=6.0', ]

setup_requirements = ['pytest-runner', ]

test_requirements = ['pytest', ]

from pygoza import __version__

setup(
    author="Jaime Ibar",
    author_email='jim2k7@gmail.com',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Framework :: Scrapy',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Utilities'
    ],
    description='ics calendar file with Real Zaragoza matches times and dates.',
    entry_points={
        'console_scripts': [
            'pygoza=pygoza.cli:main',
        ],
    },
    install_requires=requirements,
    license='GNU General Public License v2',
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='pygoza',
    name='pygoza',
    packages=find_packages(include=['pygoza']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/jim3k1/pygoza',
    version=__version__,
    zip_safe=False,
)
