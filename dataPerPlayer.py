"""
En este documento se agregara la información a la tabla Players_new
"""

from sqlPlayerPerMatch import DataBase

database = DataBase()
dataMatch = DataBase()

# Loop que extrae información por cada partido
for i in database.select_match_extended_all_id():
    dataMatch.reset() # Hacer que todas las propiedades del objeto tengan valor None
    dataMatch.select_match_extended(i[0]) # Extraer información del partido
    lstHomePlayer = [
        dataMatch.homePlayer1,
        dataMatch.homePlayer2,
        dataMatch.homePlayer3,
        dataMatch.homePlayer4,
        dataMatch.homePlayer5,
        dataMatch.homePlayer6,
        dataMatch.homePlayer7,
        dataMatch.homePlayer8,
        dataMatch.homePlayer9,
        dataMatch.homePlayer10,
        dataMatch.homePlayer11,
        ]
    
    lstAwayPlayer = [
        dataMatch.awayPlayer1,
        dataMatch.awayPlayer2,
        dataMatch.awayPlayer3,
        dataMatch.awayPlayer4,
        dataMatch.awayPlayer5,
        dataMatch.awayPlayer6,
        dataMatch.awayPlayer7,
        dataMatch.awayPlayer8,
        dataMatch.awayPlayer9,
        dataMatch.awayPlayer10,
        dataMatch.awayPlayer11,
    ]

    ### Poniendo los datos del resultado del partido ###

    # victoria local
    if dataMatch.homeTeamGoal > dataMatch.awayTeamGoal:

        for single_player in lstHomePlayer:
            if single_player == None:
                continue
            dataMatch.update_players_new_plusOne(single_player, "win")

        for single_player in lstAwayPlayer:
            if single_player == None:
                continue
            dataMatch.update_players_new_plusOne(single_player, "loss")
    
    # empate
    elif dataMatch.homeTeamGoal == dataMatch.awayTeamGoal:

        for single_player in lstHomePlayer:
            if single_player == None:
                continue
            dataMatch.update_players_new_plusOne(single_player, "tie")

        for single_player in lstAwayPlayer:
            if single_player == None:
                continue
            dataMatch.update_players_new_plusOne(single_player, "tie")

    # victoria visitante
    elif dataMatch.homeTeamGoal < dataMatch.awayTeamGoal:

        for single_player in lstHomePlayer:
            if single_player == None:
                continue
            dataMatch.update_players_new_plusOne(single_player, "loss")

        for single_player in lstAwayPlayer:
            if single_player == None:
                continue
            dataMatch.update_players_new_plusOne(single_player, "win")

    # agregando goleadores
    if dataMatch.goal == None:
        pass
    else:
        for j in dataMatch.goal:
            if j == None:
                continue
            dataMatch.update_players_new_plusOne(j, "goals") 

    # agregando shotOn
    if dataMatch.shotOn == None:
        pass
    else:
        for j in dataMatch.shotOn:
            if j == None:
                continue
            dataMatch.update_players_new_plusOne(j, "shotOn") 

    # agregando shotOff
    if dataMatch.shotOff == None:
        pass
    else:
        for j in dataMatch.shotOff:
            if j == None:
                continue
            dataMatch.update_players_new_plusOne(j, "shotOff") 

    # agregando foul
    if dataMatch.foulCommit == None:
        pass
    else:
        for j in dataMatch.foulCommit:
            if j == None:
                continue
            dataMatch.update_players_new_plusOne(j, "foul") 

    # agregando cards
    yellow, red = dataMatch.card
    if yellow == None:
        pass
    else:
        for j in yellow:
            if j == None:
                continue
            dataMatch.update_players_new_plusOne(j, "cardsYellow") 

    if red == None:
        pass
    else:
        for j in red:
            if j == None:
                continue
            dataMatch.update_players_new_plusOne(j, "cardsRed") 

    # agregando cross
    if dataMatch.cross == None:
        pass
    else:
        for j in dataMatch.cross:
            if j == None:
                continue
            dataMatch.update_players_new_plusOne(j, "cross")

    # agregando corner
    if dataMatch.corner == None:
        pass
    else:
        for j in dataMatch.corner:
            if j == None:
                continue
            dataMatch.update_players_new_plusOne(j, "corner") 
