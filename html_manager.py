import requests
import tqdm
import json

from bs4 import BeautifulSoup


class Singleton(object):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not isinstance(cls._instance, cls):
            cls._instance = super().__new__(cls)
        return cls._instance


class HtmlManager(Singleton):
    def __init__(self):
        with open('config.json', 'r', encoding='utf-8') as f:
            self.url_sample = json.load(f)['url_sample']
        self.html_soup = None
        self.teams_ids = []
        self.url_list = []

    def work_with_html(self, file_name):
        self.read_file(file_name)
        self.set_teams_ids_list()
        self.set_all_url_matches()
        return self

    def read_file(self, file_name):
        with open(file_name, 'r', encoding='utf-8') as f:
            contents = f.read()
        self.html_soup = BeautifulSoup(contents, 'html.parser')
        return self

    def set_teams_ids_list(self):
        all_ids_tags = self.html_soup.find_all(id=True)
        self.teams_ids = [element['id'][4:] for element in all_ids_tags]
        return self

    def set_all_url_matches(self):
        for ids in self.teams_ids:
            url_list = self.url_sample.split('/')
            url_list[4] = ids
            self.url_list.append('/'.join(url_list))
        return self

    def get_all_url_matches(self):
        return self.url_list
    
    def _url_connection_check(self, url):
        try:

            response = requests.get(url)
            if not response.status_code == 200:
                raise Exception
        except Exception:
            print(f'Error connection to {url}, error code: {response.status_code}')
        return self

    def _all_url_connection_check(self):
        for url in tqdm.tqdm(self.url_list):
            self._url_connection_check(url)
        return self
