from data_access import Database

class Reporte():

    def __init__(self, database: Database):
        self.database = database

    def open(self):
        return self.database.get_data()

    def close():
        pass
    