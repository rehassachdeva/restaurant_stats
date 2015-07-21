#!/usr/bin/env python2

from restaurant_stats import __version__

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages

setup (
    name = 'restaurant_stats',
    version = __version__,
    author = 'Rehas Sachdeva',
    author_email = 'aquannie@gmail.com',
    description = ('Scrape restaurant, rating and cost data from zomato.com'),
    long_description = open('README.rst').read() + '\n\n' + \
    open('CHANGELOG.rst').read(),
    license = 'MIT',
    keywords = 'restaurant, rating, cost data scrape crawl',
    url = 'http://github.com/rehassachdeva/restaurant_stats',
    packages=find_packages(),
    scripts=['scripts/restaurant_stats'],
    install_requires = ['beautifulsoup4', 'numpy', 'matplotlib'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Environment :: Console',
        'Natural Language :: English',
        'Programming Language :: Python :: 2.7',
    ],
)
