from basket_match import BasketMatch


class Storage:
    def __new__(cls, sport_type):
        if sport_type == 'basketball':
            return super().__new__(BasketballStorage)
        if sport_type == 'football':
            return super().__new__(FootballStorage)
        if sport_type == 'tennis':
            return super().__new__(TennisStorage)
        
    def __init__(self, sport_type):
        self.matches = []

    def set_basket_soups(self, soups):
        pass

    def get_all_basket_matches(self):
        pass
        

class BasketballStorage(Storage):
    def __init__(self, sport_type):
        super().__init__(self)
        self.soups = []
        self.matches = []

    def set_basket_soups(self, soups):
        self.soups = soups
        return self
    
    def get_all_basket_matches(self):
        for soup in self.soups:
            match = BasketMatch(soup)
            match.set_features()
            match.set_columns()
            self.matches.append(match)
        return self.matches
        
        
class FootballStorage (Storage):
    pass


class TennisStorage (Storage):
    pass
        
        
        
        
    