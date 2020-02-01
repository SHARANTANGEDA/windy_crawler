import scrapy
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.firefox.options import Options
import sys
from selenium.webdriver.common.keys import Keys
import time
from tabulate import tabulate
from selenium.common.exceptions import SessionNotCreatedException
import logging
from selenium.webdriver.remote.remote_connection import LOGGER


class ForecastSpider(scrapy.Spider):
    name = "windy"
    allowed_domains = ["https://www.windy.com"]
    start_urls = ["https://www.windy.com"]
    place_selected = ''
    
    def __init__(self, path_to_firefox_binary='/usr/bin/firefox', **kwargs):
        logging.getLogger('scrapy').propagate = False
        try:
            super().__init__(**kwargs)
            options = Options()
            options.add_argument('-headless')
            # logging.getLogger('scrapy').setLevel(logging.WARNING)
            binary = FirefoxBinary(firefox_path=path_to_firefox_binary)
            self.driver = webdriver.Firefox(firefox_binary=binary, options=options)
            self.place_selected = input(
                'Now select the place for weather forecast(ex. chennai, hyderabad, delhi etc... :\n')
        except SessionNotCreatedException as s:
            print('Firefox binary path entered is invalid... Try Again!')
            sys.exit(0)
    
    def get_forecast_data(self, days_xpath, hours_xpath, temps_xpath, winds_xpath, airport):
        days_and_dates = self.driver.find_elements_by_xpath(xpath=days_xpath)
        times = self.driver.find_elements_by_xpath(xpath=hours_xpath)
        temperatures = self.driver.find_elements_by_xpath(xpath=temps_xpath)
        winds = self.driver.find_elements_by_xpath(xpath=winds_xpath)
        days_list, times_list, temps_list, winds_list = [], [], [], []
        for els in days_and_dates:
            data = els.find_element_by_tag_name('div')
            print('data:', data.text)
            days_list.append(data.text)
        for els in temperatures:
            if airport:
                max_temp, min_temp = str(els.text).split('\n')
                temps_list.append(min_temp + '-' + max_temp)
            else:
                temps_list.append(els.text)
        for els in winds:
            if airport:
                trash, min_speed, max_speed = str(els.text).split('\n')
                winds_list.append(min_speed + '-' + max_speed)
            else:
                winds_list.append(els.text)
        for els in times:
            times_list.append(els.text)
        print('#########################Weather Forecast for 5 days##############################')
        for day in days_list:
            print('=>' + day)
            ind = times_list.index('0AM')
            if ind == 0:
                ind = 8
            current_times, times_list = times_list[:ind], times_list[ind:]
            current_temps, temps_list = temps_list[:ind], temps_list[ind:]
            current_winds, winds_list = winds_list[:ind], winds_list[ind:]
            display_list = []
            for i in range(0, len(current_times)):
                display_list.append([current_times[i], current_temps[i], current_winds[i]])
            if airport:
                print(tabulate(display_list, headers=['Time of Day', 'Min Temp-Max Temp(C)', 'Min Wind Speed-Max Wind '
                                                                                             'Speed(Kt)'],
                               tablefmt='orgtbl'))
            else:
                print(tabulate(display_list, headers=['Time of Day', 'Temp(C)', 'Wind Speed(Kt)'], tablefmt='orgtbl'))
    
    def parse(self, response):
        self.driver.get(response.url)
        search = self.driver.find_element_by_xpath(xpath='//*[@id="q"]')
        search.send_keys(self.place_selected)
        print('Sending Search Data and retrieving suggestions, Please wait...')
        time.sleep(2)
        results = self.driver.find_elements_by_xpath(xpath='//*[@id="search"]/div[4]/div[1]/*')
        airports = self.driver.find_elements_by_class_name('type-aerodrome')
        wxs = self.driver.find_elements_by_class_name('type-wx')
        suggestions_index, view_bar, suggestions_places = [], [], []
        index_results = 0
        for res in results:
            flag = False
            for element in wxs:
                if res.text == element.text:
                    index_results += 1
                    wxs.remove(element)
                    flag = True
                    break
            if flag:
                continue
            for element in airports:
                if res.text == element.text:
                    view_bar.append(True)
                    airports.remove(element)
                    break
            view_bar.append(False)
            suggestions_index.append(index_results + 1)
            suggestions_places.append([res.text])
            index_results += 1
        print(tabulate(suggestions_places, headers=['Place Name'], tablefmt='orgtbl', showindex='always'))
        select_index = 0
        while True:
            try:
                select_index = int(input('Please Select the Index from above table: '))
                if 0 < suggestions_index[select_index] <= len(results):
                    break
            except ValueError:
                print('You have entered an invalid index. Try Again... ')
        for i in range(0, suggestions_index[select_index]):
            search.send_keys(Keys.ARROW_DOWN)
        time.sleep(2)
        search.send_keys(Keys.ENTER)
        time.sleep(2)
        if view_bar[suggestions_index[select_index] - 1]:
            self.get_forecast_data(days_xpath='//*[@id="plugin-airport"]/section[2]/section/section[2]/div[2]/div['
                                              '8]/div[2]/div[2]/table/tbody/tr[1]/*',
                                   hours_xpath='//*[@id="plugin-airport"]/section[2]/section/section['
                                               '2]/div[2]/div[8]/div[2]/div[2]/table/tbody/tr[2]/*',
                                   temps_xpath='//*[@id="plugin-airport"]/section[2]/section/section[2]/div[2]/div['
                                               '8]/div[2]/div[2]/table/tbody/tr[4]/*',
                                   winds_xpath='//*[@id="plugin-airport"]/section[2]/section/section['
                                               '2]/div[2]/div[8]/div[2]/div[2]/table/tbody/tr[5]/*',
                                   airport=view_bar[suggestions_index[select_index] - 1])
        else:
            self.get_forecast_data(days_xpath='//*[@id="detail-data-table"]/tbody/tr[1]/*',
                                   hours_xpath='//*[@id="detail-data-table"]/tbody/tr[2]/*',
                                   temps_xpath='//*[@id="detail-data-table"]/tbody/tr[4]/*',
                                   winds_xpath='//*[@id="detail-data-table"]/tbody/tr[6]/*',
                                   airport=view_bar[suggestions_index[select_index] - 1])
        time.sleep(2)
        self.driver.quit()
