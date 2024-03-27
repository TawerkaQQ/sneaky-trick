# 1. Сбор данных
## HtmlManager
Задача класса - обработать html со всеми матчами и выдать список url-адресов для парсинга.  
- Вход: файл html/xml.  
- Выход: список url-адресов.

Работа класса:
```
file_name = 'all_match_xml.xml'

html_manager = HtmlManager()
html_manager.work_with_html(file_name)
urls = html_manager.get_all_url_matches()
```
На вход html_manager.work_with_html подается путь к файлу html/xml

Допольнительная проверка подключения:
```
html_manager._all_url_connection_check()
```
Выбрасывает исключение, если хотя бы к одному (а значит и к остальным) адресам нет подключения.
#
## UrlParser
Задача класса - получить все html из полученных с HtmlParser() url-адресов.  
- Вход: список url-адресов
- Выход: список супов bs4.BeautifulSoup

Работа класса:
```
folder = 'matches_html'

url_parser = UrlParser('firefox')
url_parser.parse_htmls(urls, folder)
```
Конструктор класса UrlParser получает название браузера пользователя:
- firefox
- chrome

На вход url_parser.parse_htmls(urls, folder):
- список url
- название папки, куда будут записаны html
#
# 2. Хранение и обработка данных
## StorageController
Задача класса - управлять классом Storage.  
К задачам управления могут относиться:
- Заполнение Storage, его дочерних классов и прочих структур (Match)
- Очистка Storage (если потребуется в будущем)
- Передача данных на класс-интерфейс для БД
- Преобразование данных а датафрейм

## Storage
Задача класса - хранить промежуточные данных и объекты различных сущностей.

Работа класса:
```
storage = Storage('basketball')
storage.set_basket_soups(soups)
storage.get_all_basket_matches()
```
Конструктор класса Storage получает название вида спорта:
- basketball
- football
- tenis
  
Сейчас реализован только 1 вид спорта - Баскетбол.
Конструктор класса basketball вмещает в себя объекты класса матч в виде списка.

## Match
Задача класса - хранить результы одного матча.

Работа класса:
```
match = Match(soup)
match.set_features()
match.set_columns()
```
На вход Match подается soup (список), а на выходе получаем статистику матча в виде списка [[Значение команды 1, Фича, Значение команды 2]...]
# 2.5 База данных
## create_db.py
Скрипт создает базу данных SQLite в директории.  
Следует запустить единожды.  

## DBConnector
Задача класса - иметь возможность в любой момент выполнения программы получить сессию/подключение к базе данных.  
Методы get_engine(self) и get_session(self) возвращают подключение(engine) и сессию(Session) соответственно.  

## db_changer.py
Файл содержит функции:
- Создания таблицы:
```
table_name = 'test_table'

columns = {'id': 'int',
          'name': 'varchar(255)',
          'age': 'int'}
create_table(table_name, columns)
```
- Добавления строк в таблицу:
```
table_name = 'test_table'

row = [{'name': 'Kekis', 'age': 82}]
add_rows_to_table(table_name, row)
```
## object_creator.py
Задача класса - вернуть объект Table и DataFrame любой таблицы базы данных. На вход класса подается коннектор DBConnector
Содержит методы:
- get_object_from_table(table_name) - получение объекта Table
- get_dataframe_from_table() - получение объекта DataFrame

## models.py
Файл содержит метаданные базы данных. 
