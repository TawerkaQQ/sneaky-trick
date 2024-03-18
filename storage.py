import os

from bs4 import BeautifulSoup
from match import Match


class Storage:
    def __new__(cls, sport_type):
        if sport_type == 'basketball':
            return super().__new__(BasketballStorage)
        if sport_type == 'football':
            return super().__new__(FootballStorage)
        if sport_type == 'tenis':
            return super().__new__(TenisStorage)
        
    def __init__(self, sport_type):
        self.matches = []
        
    def set_basket_matches(self):
        for i in range(len(self.soups)):
            match = Match(self.soups)
            match.set_columns()
            self.matches.append(match.set_features())
        return self
    
    def get_basket_matches(self):
        return self.matches
        


class BasketballStorage(Storage):
    def __init__(self, sport_type):
        super().__init__(self)
        self.soups = []

    def set_basket_soups(self, soups):
        self.soups = soups
        return self
    
    def get_basket_soups(self):
        return self.soups

        
        
        
        
class FootballStorage (Storage):
    pass

class TenisStorage (Storage):
    pass
        
        
        
        
    