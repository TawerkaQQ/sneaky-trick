from html_manager import HtmlManager
from url_parser import UrlParser


if __name__ == "__main__":
    file_name = 'all_match_xml.xml'

    # # Достали url
    # html_manager = HtmlManager()
    # html_manager.work_with_html(file_name)
    # urls = html_manager.get_all_url_matches()
    
    
    # html_manager._all_url_connection_check()
    
    # Создаем объекты класса UrlParser
    parser1 = UrlParser('chrome')
    parser2 = UrlParser('chrome')

    # Проверяем, что оба объекта ссылаются на один и тот же экземпляр
    print(parser1 is parser2)  # Ожидаемый результат: True

    # Меняем состояние одного из объектов
    parser1.create_target_folder("test_folder")

    # Проверяем, что изменение отразилось на другом объекте
    print(parser2.create_target_folder("test_folder").get_html_from_url("example.com"))  # Ожидаемый результат: None`

#     url_list = ['https://www.flashscorekz.com/match/CWVnE6LK/#/match-summary/match-statistics/0',
#  'https://www.flashscorekz.com/match/0tA7xBvJ/#/match-summary/match-statistics/0',
#  'https://www.flashscorekz.com/match/U7trFn6E/#/match-summary/match-statistics/0',
#  'https://www.flashscorekz.com/match/jHsvGSj8/#/match-summary/match-statistics/0',
#  'https://www.flashscorekz.com/match/2e5mg5qe/#/match-summary/match-statistics/0',
#  'https://www.flashscorekz.com/match/pKfhhPb1/#/match-summary/match-statistics/0',
#  'https://www.flashscorekz.com/match/OAgdiqE7/#/match-summary/match-statistics/0',
#  'https://www.flashscorekz.com/match/lh1qfoUl/#/match-summary/match-statistics/0',
#  'https://www.flashscorekz.com/match/I5vCCgpG/#/match-summary/match-statistics/0',]
    
    
    
#     # url_parser = UrlParser('chrome')
#     # folder_to_save = 'test_chrome_html1'
    
#     # url_parser.get_html_from_url(url_list[0], folder_to_save)
    
#     url_parser = UrlParser('firefox')
#     folder_to_save = 'test_firefox_html1'
    
#     url_parser.get_html_from_url(url_list[0], folder_to_save)
    
    

    
    
    