from data_access import PostgresDataAccess, MongoDataAccess
from config import PostgresConfig, MongoConfig
from reporte import Reporte

# Cambia entre las siguientes líneas para usar PostgreSQL o MongoDB
# data_access = PostgresDataAccess(PostgresConfig)
database = MongoDataAccess(MongoConfig)

# Ejemplo de uso
teams = database.get_data()
print("Datos obtenidos:")
for team in teams:
    print(team)


# Ejemplo de crear un nuevo registro
# new_data = {'nombre': 'Borusia Dortmund'}
# database.create_data(new_data)
# print("Nuevo dato creado.")

# Ejemplo de actualizar un registro existente (asumiendo que tienes el _id o id adecuado)
# update_data = {'_id': 'id_del_registro_a_actualizar', 'column1': 'DatoActualizado'}
# database.update_data(update_data)
# print("Dato actualizado.")

# Ejemplo de eliminar un registro existente (asumiendo que tienes el _id o id adecuado)
# data_id_to_delete = 'id_del_registro_a_eliminar'
# database.delete_data(data_id_to_delete)
# print("Dato eliminado.")
