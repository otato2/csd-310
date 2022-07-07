# Nicholas Werner
# CSD 310 Assignment 9.2
# 07/07/2022

import mysql.connector
from mysql.connector import errorcode

config = {
	"user": "pysports_user",
	"password": "seasprite",
	"host": "127.0.0.1",
	"database": "pysports",
	"raise_on_warnings": True
}


db = mysql.connector.connect(**config)
cursor = db.cursor()
print("-- DISPLAYING PLAYER RECORDS --")
cursor.execute("SELECT player.player_id, player.first_name, player.last_name, team.team_name\nFROM player\nINNER JOIN team\n\tON player.team_id = team.team_id");
ret = cursor.fetchall()

for rec in ret:
    print("Player ID: {}\nFirst Name: {}\nLast Name: {}\nTeam Name: {}\n".format((rec[0]),(rec[1]),(rec[2]),(rec[3])))

db.close()