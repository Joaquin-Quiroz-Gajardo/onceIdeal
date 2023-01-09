"""
En este documento se crea la clase DataBase que permite la extracción de información desde la base de datos. A partir de implementar métodos extraídos desde XmlMatches se procesa la información desde xml a listas.
"""

import sqlite3
from XMLManagment import XmlMatches

xmlMatches = XmlMatches()

class DataBase:
    def __init__(self):
        self.connection = sqlite3.connect("database.sqlite") # Creando coneccion con la base de datos
        self.cursor = self.connection.cursor()

    # Este método permite dejar todos los atributos de la clase en none
    def reset(self):
        self.matchId = None
        self.leagueId = None
        self.homeTeamGoal = None
        self.awayTeamGoal = None
        self.homePlayer1 = None
        self.homePlayer2 = None
        self.homePlayer3 = None
        self.homePlayer4 = None
        self.homePlayer5 = None
        self.homePlayer6 = None
        self.homePlayer7 = None
        self.homePlayer8 = None
        self.homePlayer9 = None
        self.homePlayer10 = None
        self.homePlayer11 = None
        self.awayPlayer1 = None
        self.awayPlayer2 = None
        self.awayPlayer3 = None
        self.awayPlayer4 = None
        self.awayPlayer5 = None
        self.awayPlayer6 = None
        self.awayPlayer7 = None
        self.awayPlayer8 = None
        self.awayPlayer9 = None
        self.awayPlayer10 = None
        self.awayPlayer11 = None
        self.goal = None
        self.shotOn = None
        self.shotOff = None
        self.foulCommit = None
        self.card = None
        self.cross = None
        self.corner = None

    # Este método permite extraer la información de un jugador a partir de su id
    def select_player(self, id):
        sql = f"SELECT * FROM Player WHERE id = {id}"

        try:
            self.cursor.execute(sql)
            return self.cursor.fetchone()

        except Exception as err:
            raise
    
    # Este método permite extraer la información de un partido de la tabla matchExtended
    def select_match_extended(self, id):
        sql = f"SELECT * FROM MatchExtend WHERE id = {id}"

        try:
            self.cursor.execute(sql)
            matchData = self.cursor.fetchone()

            self.matchId = matchData[0]
            self.leagueId = matchData[3]
            self.homeTeamGoal = matchData[5]
            self.awayTeamGoal = matchData[6]
            self.homePlayer1 = matchData[7]
            self.homePlayer2 = matchData[8]
            self.homePlayer3 = matchData[9]
            self.homePlayer4 = matchData[10]
            self.homePlayer5 = matchData[11]
            self.homePlayer6 = matchData[12]
            self.homePlayer7 = matchData[13]
            self.homePlayer8 = matchData[14]
            self.homePlayer9 = matchData[15]
            self.homePlayer10 = matchData[16]
            self.homePlayer11 = matchData[17]
            self.awayPlayer1 = matchData[18]
            self.awayPlayer2 = matchData[19]
            self.awayPlayer3 = matchData[20]
            self.awayPlayer4 = matchData[21]
            self.awayPlayer5 = matchData[22]
            self.awayPlayer6 = matchData[23]
            self.awayPlayer7 = matchData[24]
            self.awayPlayer8 = matchData[25]
            self.awayPlayer9 = matchData[26]
            self.awayPlayer10 = matchData[27]
            self.awayPlayer11 = matchData[28]
            xmlMatches.xmlGoals(matchData[29])
            self.goal = xmlMatches.scorers
            xmlMatches.xmlShotOn(matchData[30])
            self.shotOn = xmlMatches.shotOns
            xmlMatches.xmlShotOff(matchData[31])
            self.shotOff = xmlMatches.shotOffs
            xmlMatches.xmlFault(matchData[32])
            self.foulCommit = xmlMatches.faults
            xmlMatches.xmlCard(matchData[33])
            self.card = [
                xmlMatches.cardsYellow,
                xmlMatches.cardsRed
                ] 
            xmlMatches.xmlCross(matchData[34])
            self.cross = xmlMatches.cross
            xmlMatches.xmlCorner(matchData[35])
            self.corner = xmlMatches.corner

        except Exception as err:
            raise

    # Este método permite extraer la información de cuantos partidos existen en la tabla matchExtended
    def select_match_extended_count(self):
        sql = f"SELECT count(id) from MatchExtend;"

        try:
            self.cursor.execute(sql)
            return self.cursor.fetchone()

        except Exception as err:
            raise

    # Este método permite extraer la información de todos los id del partido matchExtended
    def select_match_extended_all_id(self):
        sql = "SELECT id FROM Match;"

        try:
            self.cursor.execute(sql)
            return self.cursor.fetchall()

        except Exception as err:
            raise
    
    # Este método permite obtener el id de todos los jugadores de la tabla Players
    def select_players_all_id(self):
        sql = "SELECT player_api_id FROM Player;"

        try:
            self.cursor.execute(sql)
            return self.cursor.fetchall()

        except Exception as err:
            raise

    # Este método permite obtener toda la información de Players_new
    def select_players_new(self):
        sql = "SELECT * FROM Player_new;"

        try:
            self.cursor.execute(sql)
            return self.cursor.fetchall()

        except Exception as err:
            raise

    # Este método permite agregar un jugador en players_new
    def insert_players_new(
        self, 
        id, 
        win,
        tie,
        loss,
        goals,
        shotOn,
        shotOff,
        foul,
        cardsYellow,
        cardsRed,
        cross,
        corner):

        sql = f"""INSERT INTO Player_new  
                VALUES ({id}, 
                        {win},
                        {tie},
                        {loss},
                        {goals},
                        {shotOn},
                        {shotOff},
                        {foul},
                        {cardsYellow},
                        {cardsRed},
                        {cross},
                        {corner});"""

        try:
            self.cursor.execute(sql)
            self.connection.commit()

        except Exception as err:
            raise

    # Este método permite crear la tabla Players_new
    def create_table_players_new(self):

        sql = f"""
            CREATE TABLE Player_new (
	id INTEGER PRIMARY KEY,
	win int,
    tie int,
    loss int,
    goals int,
    shotOn int,
    shotOff int,
    foul int,
    cardsYellow int,
    cardsRed int,
    cross int,
    corner int,
    FOREIGN KEY (id) REFERENCES Player(player_api_id)
    );
        """

        try:
            self.cursor.execute(sql)
            self.connection.commit()

        except Exception as err:
            raise
        
    # Este método permite agregar un valor mas a la celda que deseamos, entregando el id del jugador junto con la entidad a actualizar
    def update_players_new_plusOne(self, id, entity):

        sql = f"""
            UPDATE Player_new
            SET {entity} = {entity} + 1
            WHERE id = {id};
        """

        try:
            self.cursor.execute(sql)
            self.connection.commit()

        except Exception as err:
            print(err)