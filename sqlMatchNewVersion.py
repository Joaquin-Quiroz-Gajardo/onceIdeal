import sqlite3
import pandas as pd
import sqlalchemy

# Creando el database engine
engine = sqlalchemy.create_engine("sqlite:///database.sqlite")

query = """
SELECT Match.id, 
	League.name,
	Country.name,
	Match.country_id, 
	league_id, 
	home_team_api_id,
	home_team_goal, 
	away_team_goal, 
	home_player_1,
	home_player_2,
	home_player_3,
	home_player_4,
	home_player_5,
	home_player_6,
	home_player_7,
	home_player_8,
	home_player_9,
	home_player_10,
	home_player_11,
	away_player_1,
	away_player_2,
	away_player_3,
	away_player_4,
	away_player_5,
	away_player_6,
	away_player_7,
	away_player_8,
	away_player_9,
	away_player_10,
	away_player_11,
	goal,
	shoton,
	shotoff,
	foulcommit,
	card,
	Match.cross,
	corner,
	possession,
	team_long_name
FROM Match
INNER JOIN Team on Match.home_team_api_id = Team.team_api_id
INNER JOIN League on Match.league_id = League.id
INNER JOIN Country on League.id = Country.id;
"""

# Metodo de importacion realizado con una query
df = pd.read_sql(query, engine)

# Guardar cambios en la base de datos hechos en pandas
# if_exists="append" permite que en caso de existir la tabla solo se agregen los datos
# if_exists="replace" hace que si se da la coincidencia de nombre se reemplaza toda la tabla
# index=False elimina el indice, lo que es necesario dado que no existe dicha entidad en la tabla

# print(df.head(10))
df.to_sql("MatchExtend", engine, if_exists="append", index=False)
