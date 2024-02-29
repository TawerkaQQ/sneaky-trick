from html_manager import HtmlManager
from url_parser import UrlParser


if __name__ == "__main__":
    file_name = 'all_match_xml.xml'

    # # Достали url
    html_manager = HtmlManager()
    html_manager.work_with_html(file_name)
    urls = html_manager.get_all_url_matches()
    
    
    html_manager._all_url_connection_check()
    
    
    # # На текущий момент только сохраняется html по url.
    # url_parser = UrlParser('firefox')
    # folder_to_save = 'all_match_html'
    # url_parser.get_html_from_url(urls[0], folder_to_save)

    
    
    