from sqlalchemy import MetaData, Table, select

class ObjectCreator:
    def __init__(self, connector):
        self.connector = connector
        self.metadata = self.create_metadata()

    def create_metadata(self):
        metadata = MetaData()
        return metadata

    def get_object_from_table(self, table_name):
        table = Table(table_name, self.metadata, autoload_with=self.connector.get_engine())
        return table

    def get_dataframe_from_table(self):
        pass