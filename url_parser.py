import os
import pandas as pd
import tqdm


from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.firefox import GeckoDriverManager


class Singleton(object):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not isinstance(cls._instance, cls):
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance


class UrlParser(Singleton):
    def __new__(cls, browser):
        if browser == 'firefox':
            return super().__new__(UrlParserFirefox)
        if browser == 'chrome':
            return super().__new__(UrlParserChrome)

    def __init__(self, browser):
        self.soups = []

    def parse_htmls(self, urls, folder):
        pass

    def get_soup_from_html(self, folder, file_name):
        path = os.path.join(os.getcwd(), folder, file_name)
        with open(path, 'r', encoding='utf-8') as f:
            contents = f.read()
        soup = BeautifulSoup(contents, 'html.parser')
        return soup

    def set_all_soups_from_html(self, folder):
        path = os.path.join(os.getcwd(), folder)
        files = os.listdir(path)
        for file in files:
            soup = self.get_soup_from_html(folder, file)
            self.soups.append(soup)
        return self

    def create_target_folder(self, folder):
        current_dir = os.getcwd()
        path = os.path.join(current_dir, folder)
        try:
            os.mkdir(path)
        except:
            pass
        return self

    def setup_firefox_options(self):
        pass
    def get_html_from_url(self, url):
        pass
    def get_soup(self):
        return self.soups

class UrlParserFirefox(UrlParser):
    def __init__(self, browser):
        super().__init__(self)
        self.setup_firefox_options()

    def parse_htmls(self, urls, folder):
        self.get_all_htmls_from_urls(urls, folder)
        self.set_all_soups_from_html(folder)
        return self

    def setup_firefox_options(self):
        self.options = Options()
        self.options.headless = True
        self.service = Service(GeckoDriverManager().install())
        self.driver = webdriver.Firefox(service=self.service,
                                        options=self.options)
        return self

    def get_all_htmls_from_urls(self, url_list, folder):
        for i, url in tqdm.tqdm(enumerate(url_list)):
            self.setup_firefox_options()
            self.get_html_from_url(url, folder, i)
        return self

    def get_html_from_url(self, url, folder, file_number):
        self.create_target_folder(folder)
        self.driver.get(url)
        html_content = self.driver.page_source
        self.driver.quit()

        with open(os.path.join(os.getcwd(), folder, f'{file_number+1}_match'), 'w', encoding='utf-8') as f:
            f.write(html_content)
        return self


class UrlParserChrome(UrlParser):
    def __init__(self, browser):
        super().__init__(self)
        self.setup_chrome_options()

    def parse_htmls(self, urls, folder):
        self.get_all_htmls_from_urls(urls, folder)
        self.set_all_soups_from_html(folder)
        return self

    def setup_chrome_options(self):
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('--headless')
        self.driver = webdriver.Chrome(options=self.options)

    def get_all_htmls_from_urls(self, url_list, folder):
        for i, url in tqdm.tqdm(enumerate(url_list)):
            self.setup_chrome_options()
            self.get_html_from_url(url, folder, i)
        return self

    def get_html_from_url(self, url, folder, file_name):
        self.create_target_folder(folder)
        self.driver.get(url)
        html_content = self.driver.page_source

        with open(os.path.join(os.getcwd(), folder, str(file_name) + '.html'), 'w', encoding='utf-8') as f:
            f.write(html_content)

        return self
