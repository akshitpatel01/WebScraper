import csv
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from util import Logger


class Scraper(object):

    def __init__(self, browser, website):
        # Initialize Logging
        self.loger = Logger('')
        self.loger.set_level('debug')

        # Initialize browser
        if (browser == 'chrome'):
            # Chrome
            self.driver = webdriver.Chrome(
                            service=Service(ChromeDriverManager().install()))
            self.loger.log('debug', 'Browser is set to chrome')
        else:
            self.loger.log('error', 'Browser not supported')

        # Initialize e-commerce website
        if (website == 'Amazon'):
            self.web = Amazon_scraper()
            self.loger.log('debug', 'Amazon added')
        else:
            self.logger.log('error', 'Website not supported')
            return ''

    def get_url(self, search_item):
        return self.web.get_url(search_item)

    def scraper(self, search_item):
        self.driver.get(
                self.get_url(search_item))


class Amazon_scraper():
    amazon_url = 'https://www.amazon.in/'

    def __init__(self):
        pass

    def get_url(self, search_item):
        return self.amazon_url


scraper = Scraper('chrome', 'Amazon')
scraper.scraper('Ultrawide Monitor')
