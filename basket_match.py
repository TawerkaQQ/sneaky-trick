import pandas as pd
import json


class BasketMatch:
    def __init__(self, soup):
        self.all_teams = self.set_all_teams()

        self.soup = soup
        self.features_list = []
        self.columns = []

    def set_all_teams(self):
        with open('all_teams.json', 'r', encoding='utf-8') as f:
            all_teams = json.load(f)['teams']
        return all_teams

    def set_features(self):
        features = [self.soup.find_all('strong')[x].text for x in range(len(self.soup.find_all('strong')))]
        structured_features = [features[i:i+3] for i in range(0, len(features), 3)]
        title = self.soup.find('title').text
        team_names = self.get_teams_names_from_title(title)
        structured_features.append([team_names[0], 'Команды', team_names[1]])
        self.features_list = structured_features
        return self 

    def get_teams_names_from_title(self, title):
        team_pos_dict = {}
        names = []
        for team in self.all_teams:
            ind = title.find(team)
            if ind != -1:
                team_pos_dict[ind] = team
        for key in sorted(team_pos_dict.keys()):
            names.append(team_pos_dict[key])
        return names
    def set_columns(self):
        self.columns = [x[1] for x in self.features_list]
        return self

    def get_features_list(self):
        return self.features_list

    def features_to_dict(self, data):
        feature_dict = {}
        for match in data:
            keys = match[1]
            values = match[0:3:2]
            feature_dict.update({'team1 ' + keys : values[0]})
            feature_dict.update({'team2 ' + keys : values[1]})
        return feature_dict
    
    def to_dataframe(self, data):
        feature_dict = self.features_to_dict(data)
        dataframe = pd.DataFrame([feature_dict])
        return dataframe
    
    def __str__(self):
        for feature in self.features_list:
            print(feature)
        return ''
