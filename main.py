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

    def setup_config_json(self):
        with open('config.json', 'r') as f:
            data = json.load(f)
        return data

    def save_basketball_matches_df(self):
        number_of_urls = int(self.data['nums_url'])
        urls = self.html_manager.get_all_url_matches()
        self.html_manager.work_with_html(self.file_name)
        
        self.url_parser.parse_htmls(urls[:number_of_urls], self.folder)
        soups = self.url_parser.get_all_soups()
        self.storage.set_basket_soups(soups)
        matches = self.storage.get_all_basket_matches()
        
        df_res = pd.DataFrame()
        for mat in matches:
            data = mat.get_features_list()
            df = mat.to_dataframe(data)
            df_res = pd.concat([df_res, df], ignore_index=True)
        df_res.to_csv('all_match.csv', index=False)  
        return self
            
        
if __name__ == '__main__':
    
    facade = MainController()
    facade.save_basketball_matches_df()
    