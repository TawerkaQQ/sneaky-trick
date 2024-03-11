from db_connector import DBConnector
from sqlalchemy import MetaData, Table, text
from models import *

connector = DBConnector()


def create_table(table_name, columns):
    '''
    Создает таблицу в БД
    columns - {'имя столбца': 'тип'}
    '''
    columns_list = [f'{key} {value}' for key, value in columns.items()]
    columns_text = ', '.join(columns_list)
    query = text(f'CREATE TABLE {table_name} ({columns_text})')
    with connector.get_engine().connect() as connection:
        connection.execute(query)


def add_rows_to_table(table_name, rows):
    '''
    Добавляет строки к таблице БД
    rows - ['название колонки': 'значение', 'название 2 колонки': 'значение']
    '''
    table_class = Base.metadata.tables.get(table_name)
    table = Table(table_name, MetaData(), autoload_with=connector.get_engine())
    with connector.get_engine().connect() as connection:
        for row in rows:
            print(row)
            connection.execute(table.insert().values(**row))
        connection.commit()


if __name__ == "__main__":
    table_name = 'test_table'
    columns = {'id': 'int',
               'name': 'varchar(255)',
               'age': 'int'}
    row = [{'name': 'Kekis', 'age': 82}]
    create_table(table_name, columns)
    add_rows_to_table(table_name, row)
