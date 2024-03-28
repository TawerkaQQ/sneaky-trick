import json
import pandas as pd

from html_manager import HtmlManager
from url_parser import UrlParser
from storage import Storage
from match import Match


class MainController:
    def __init__(self):
        self.data = self.setup_config_json()
        self.file_name = self.data['file_name']
        self.folder = self.data['folder']
        self.html_manager = HtmlManager()
        self.url_parser = UrlParser(self.data['browser'])
        self.storage = Storage(self.data['sprot_type'])
        self.match = Match(self.get_soups())

    def setup_config_json(self):
        with open('config.json', 'r') as f:
            data = json.load(f)
        return data
    
    def get_urls(self):
        urls = self.html_manager.get_all_url_matches()
        return urls
    
    def get_soups(self):
        soups = self.url_parser.get_all_soups()
        return soups
    
    def load_html_data(self):
        number_of_urls = int(self.data['nums_url'])
        self.html_manager.work_with_html(self.file_name)
        self.url_parser.parse_htmls(self.get_urls()[:number_of_urls], self.folder)
        return self
    
    def get_matches(self):
        self.storage.set_basket_soups(self.get_soups())
        matches = self.storage.get_all_basket_matches()
        return matches
    
    def set_dataframe(self, matches):
        df_res = pd.DataFrame()
        for mat in matches:
            data = mat.get_features_list()
            dict_data = self.match.features_to_dict(data)
            df = self.match.to_dataframe(dict_data)
            df_res = pd.concat([df_res, df], ignore_index=True)
        df_res.to_csv('all_match.csv', index=False)  
        return df_res
            
        
if __name__ == '__main__':
    
    facade = MainController()
    facade.load_html_data()
    matches_basket = facade.get_matches()
    facade.set_dataframe(matches_basket)
    
        
        

    
    
    