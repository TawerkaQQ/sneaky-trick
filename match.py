import pandas as pd

from bs4 import BeautifulSoup


class Match:
    def __init__(self, soup):
        self.soup = soup
        self.features_list = []
        self.columns = []

    def set_features(self):
        features = [self.soup.find_all('strong')[x].text for x in range(len(self.soup.find_all('strong')))]
        structured_features = [features[i:i+3] for i in range(0, len(features), 3)]
        structured_features.append([self.soup.find('title').text, self.soup.find('title').text, self.soup.find('title').text])
        self.features_list = structured_features
        return self 
        
    def set_columns(self):
        self.columns = [x[1] for x in self.features_list]
        self.columns.append('Название')
        return self

    def get_features_list(self):
        return self.features_list

    def __str__(self):
        for feature in self.features_list:
            print(feature)
        return ''
    
    def to_dataframe(self):
        pass
    