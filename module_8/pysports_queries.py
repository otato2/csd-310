# Nicholas Werner
# CSD 310 Assignment 8.3
# 06/29/2022

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
print("-- DISPLAYING TEAM RECORDS --")
cursor.execute("SELECT team_id, team_name, mascot FROM team")
ret = cursor.fetchall()

for rec in ret:
    print("Team ID: {}\nTeam Name: {}\nMascot: {}\n".format((rec[0]),(rec[1]),(rec[2])))


print("\n-- DISPLAYING TEAM RECORDS --")
cursor.execute("SELECT player_id, first_name, last_name, team_id FROM player")
lst = cursor.fetchall()

for ent in lst:
    print("Player ID: {}\nFirst Name: {}\nLast Name: {}\nTeam ID: {}\n".format((ent[0]),(ent[1]),(ent[2]),(ent[3])))

db.close()