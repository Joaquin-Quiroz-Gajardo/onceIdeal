"""
En este documento se crea la tabla Players_new, junto con incializarza, agregando a todos los jugadores, con todas sus estadísticas en 0
"""

from sqlPlayerPerMatch import DataBase

database = DataBase()

# Crear la tabla player_new
database.create_table_players_new()

# Agregar una base de datos vacia
for i in database.select_players_all_id():
    database.insert_players_new(
                        i[0],
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0
    )
