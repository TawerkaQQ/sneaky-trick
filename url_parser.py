import os

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
        pass


    def create_target_folder(self, folder):
        current_dir = os.getcwd()
        path = os.path.join(current_dir, folder)
        try:
            os.mkdir(path)
        except:
            pass
        return self

    def get_html_from_url(self, url):
        pass

class UrlParserFirefox(UrlParser):
    def __init__(self, browser):
        super().__init__(self)
        self.options = Options()
        self.options.headless = True
        self.service = Service(GeckoDriverManager().install())
        self.driver = webdriver.Firefox(service=self.service,
                                        options=self.options)

    def get_html_from_url(self, url, folder, file_name = 'one_match.html'):
        self.create_target_folder(folder)
        self.driver.get(url)
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "myDynamicElement"))
            )
        finally:
            html_content = self.driver.page_source
            self.driver.quit()

            with open(os.path.join(os.getcwd(), folder, file_name), 'w', encoding='utf-8') as f:
                f.write(html_content)
        return self

class UrlParserChrome(UrlParser):
    def __init__(self, browser):
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('--headless')
        self.driver = webdriver.Chrome(options=self.options)
        
    def get_html_from_url(self, url, folder, file_name = 'one_match_Chrome.html'):
        self.create_target_folder(folder)
        self.driver.get(url)
        try:
            html_content = self.driver.page_source
            with open(os.path.join(os.getcwd(), folder, file_name), 'w', encoding='utf-8') as f:
                f.write(html_content)
        except:
            print("Something bad")

        return self
