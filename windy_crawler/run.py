import scrapy
from windy_crawler.spiders.forecast_spider import ForecastSpider
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
import logging


def windy_crawler():
    print('Welcome to Windy Web Crawler')
    firefox_binary_path = input(
        'Please enter your full path to firefox binary in your system(default: /usr/bin/firefox) :\n')
    if not firefox_binary_path:
        firefox_binary_path = '/usr/bin/firefox'
    print('Path taken:', firefox_binary_path)
    # place = input('Now select the place for weather forecast(ex. chennai, hyderabad, delhi etc... :\n')
    # spider = ForecastSpider(place=place, firefox_binary_path=firefox_binary_path)
    process = CrawlerProcess(get_project_settings())
    logging.getLogger('scrapy').propagate = False
    process.crawl(ForecastSpider, path_to_firefox_binary=firefox_binary_path)
    process.start()
    print('Created by Sai Sharan Tangeda')


