# import psycopg2
# import pymongo

# def get_connection():
#     return psycopg2.connect(
#         host="localhost",
#         database="postgres",
#         user="postgres",
#         password="123456789Pp"
#     )

# def get_connection_mongo():
#     # Conexión a la base de datos
#     client = pymongo.MongoClient("mongodb+srv://m_wonder_omar:0GoTo4nhrKaPRy67@cluster0.oikaa.mongodb.net/")

#     # Selección de la base de datos
#     db = client["public"]

#     # Selección de la colección
#     collection = db["equipos_champions"]

#     return collection

import psycopg2
import pymongo

class PostgresConfig:
    @staticmethod
    def get_connection():
        return psycopg2.connect(
            host="localhost",
            database="postgres",
            user="postgres",
            password="123456789Pp"
        )

class MongoConfig:
    @staticmethod
    def get_connection():
        client = pymongo.MongoClient("mongodb+srv://m_wonder_omar:0GoTo4nhrKaPRy67@cluster0.oikaa.mongodb.net/")
        db = client["public"]
        collection = db["equipos_champions"]
        return collection
