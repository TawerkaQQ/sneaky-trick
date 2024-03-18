from html_manager import HtmlManager
from url_parser import UrlParser
from storage import Storage
from match import Match


if __name__ == "__main__":
    file_name = 'all_match_xml.xml'

    # # Достали url
    html_manager = HtmlManager()
    html_manager.work_with_html(file_name)
    urls = html_manager.get_all_url_matches()

    # Проверка подключения
    # html_manager._all_url_connection_check()

    # Записиали html
    folder = 'matches_html'
    url_parser = UrlParser('chrome')
    url_parser.parse_htmls(urls[:2], folder)

    soups = url_parser.get_all_soups()
    # print(soups)
    # url_parser.get_all_htmls_from_urls(urls[:3], folder)
    # url_parser.get_soup_from_html('matches_html', )
    # test = url_parser.set_all_soups_from_html(folder)
    matches_futures = []
    
    for soup in soups:
        match = Match(soup)
        match.set_all_features()
        print('ASGFASGAg')
        test = match.get_features_list()
        print(test)
        # matches_futures.append(match.set_features())
        
        
        
    # print(matches_futures)

    
    
    # storage = Storage('basketball')
    # storage.set_basket_soups(soups)
    # storage.set_basket_matches()
    # matches = storage.get_basket_matches()
    # basketSoup = storage.get_basket_soups()
    
    # print(matches)

    
    
    