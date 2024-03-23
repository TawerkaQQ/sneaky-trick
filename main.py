from html_manager import HtmlManager
from url_parser import UrlParser
from storage import Storage
from match import Match

import json



        
class MainController:
    def __init__(self):
        self.data = self.setup_config_json()
        self.file_name = self.data['file_name']
        self.folder = self.data['folder']
        self.html_manager = HtmlManager()
        self.url_parser = UrlParser(self.data['browser'])
        self.storage = Storage(self.data['sprot_type'])
        self.urls = []
        self.soups = []

    def setup_config_json(self):
        with open('config.json', 'r') as f:
            data = json.load(f)
        return data

    # # Достали url
    def get_url_from_file(self):
        self.html_manager.work_with_html(self.file_name)
        self.urls = self.html_manager.get_all_url_matches()
        return self

    # Проверка подключения
    def check_url_connection(self):
        self.html_manager._all_url_connection_check()
        return self

    # Записиали html
    def set_html_from_ulr(self):
        self.url_parser.parse_htmls(self.urls[:int(self.data['nums_url'])], self.folder)
        return self

    def set_soups(self):
        self.soups = self.url_parser.get_all_soups()[:int(self.data['nums_url'])]
        return self
    # url_parser.get_all_htmls_from_urls(urls[:3], folder)
    # url_parser.get_soup_from_html('matches_html', )
    # test = url_parser.set_all_soups_from_html(folder)
    
    def set_matches(self):
        self.storage.set_basket_soups(self.soups)
        matches = self.storage.get_all_basket_matches()
        return matches
        
        
if __name__ == '__main__':
    
    
    main = MainController()
    main.get_url_from_file()
    main.set_html_from_ulr()
    main.set_soups()
    matches_basket = main.set_matches()
    print(matches_basket)
    
        
        

    
    
    