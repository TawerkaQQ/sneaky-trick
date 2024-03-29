import os
import time

from tqdm import tqdm
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options


class UrlParser:
    def __new__(cls, browser):
        if browser == 'firefox':
            return super().__new__(UrlParserFirefox)
        if browser == 'chrome':
            return super().__new__(UrlParserChrome)

    def __init__(self, browser):
        self.driver = None
        self.options = None
        self.service = None
        self.soups = []

    def parse_htmls(self, urls, folder):
        self.get_all_htmls_from_urls(urls, folder)
        self.set_all_soups_from_html(folder)
        return self

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
        if not os.path.exists(path):
            os.mkdir(path)
        return self

    def get_all_htmls_from_urls(self, url_list, folder):
        progress_bar = tqdm(enumerate(url_list), unit_scale=True, total=len(url_list), leave=True,
                            bar_format='{desc} Осталось {remaining}')
        for i, url in progress_bar:
            self.get_html_from_url(url, folder, i)
            progress_bar.set_description(f"Записано {i+1}/{len(url_list)} html")
        return self

    def get_html_from_url(self, url, folder, file_number):
        self.create_target_folder(folder)
        self.setup_options()
        self.driver.get(url)
        time.sleep(10)
        html_content = self.driver.page_source
        with open(os.path.join(os.getcwd(), folder, f'{file_number+1}_match.html'), 'w+', encoding='utf-8') as f:
            f.write(html_content)
        self.driver.quit()
        return self

    def setup_options(self):
        pass

    def get_all_soups(self):
        return self.soups


class UrlParserFirefox(UrlParser):
    def __init__(self, browser):
        super().__init__(self)
        self.setup_options()

    def setup_options(self):
        self.options = Options()
        self.options.headless = True
        driver_path = os.path.join(os.getcwd(), 'geckodriver.exe')
        self.service = Service(driver_path)
        self.driver = webdriver.Firefox(service=self.service,
                                        options=self.options)
        return self


class UrlParserChrome(UrlParser):
    def __init__(self, browser):
        super().__init__(self)
        self.setup_options()

    def setup_options(self):
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('--headless')
        self.driver = webdriver.Chrome(options=self.options)
        return self
