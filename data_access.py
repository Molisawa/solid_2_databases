from abc import ABC, abstractmethod

class DataAccess(ABC):
    @abstractmethod
    def get_data(self):
        pass

    @abstractmethod
    def create_data(self, data):
        pass

    @abstractmethod
    def update_data(self, data):
        pass

    @abstractmethod
    def delete_data(self, data_id):
        pass

class PostgresDataAccess(DataAccess):
    def __init__(self, config):
        self.config = config

    def get_data(self):
        conn = self.config.get_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM equipos_champions")
        results = cur.fetchall()
        cur.close()
        conn.close()
        return results

    def create_data(self, data):
        conn = self.config.get_connection()
        cur = conn.cursor()
        cur.execute("INSERT INTO equipos_champions (id, nombre) VALUES (%s, %s)", (data['id'], data['nombre']))
        conn.commit()
        cur.close()
        conn.close()

    def update_data(self, data):
        conn = self.config.get_connection()
        cur = conn.cursor()
        cur.execute("UPDATE equipos_champions SET column1 = %s WHERE id = %s", (data['column1'], data['id']))
        conn.commit()
        cur.close()
        conn.close()

    def delete_data(self, data_id):
        conn = self.config.get_connection()
        cur = conn.cursor()
        cur.execute("DELETE FROM equipos_champions WHERE id = %s", (data_id,))
        conn.commit()
        cur.close()
        conn.close()

class MongoDataAccess(DataAccess):
    def __init__(self, config):
        self.config = config

    def get_data(self):
        return self.config.get_connection().find()

    def create_data(self, data):
        self.config.get_connection().insert_one(data)

    def update_data(self, data):
        self.config.get_connection().update_one({'_id': data['_id']}, {'$set': data})

    def delete_data(self, data_id):
        self.config.get_connection().delete_one({'_id': data_id})
