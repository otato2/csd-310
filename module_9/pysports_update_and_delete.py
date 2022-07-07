# Nicholas Werner
# CSD 310 Assignment 9.3
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

# Insert record into Player table
cursor.execute("INSERT INTO player (first_name, last_name, team_id) VALUES ('Smeagol', 'Shire Folk', 1)")

# Show new record inside of Player table
print("-- DISPLAYING PLAYERS AFTER INSERT --")
cursor.execute("SELECT player.player_id, player.first_name, player.last_name, team.team_name FROM player INNER JOIN team ON player.team_id = team.team_id;")
lst = cursor.fetchall()

for ent in lst:
    print("Player ID: {}\nFirst Name: {}\nLast Name: {}\nTeam Name: {}\n".format((ent[0]),(ent[1]),(ent[2]),(ent[3])))

# Update the new record to team 2
cursor.execute("UPDATE player SET team_id = 2, first_name = 'Gollum', last_name = 'Ring Stealer' WHERE first_name = 'Smeagol';")

# Show all records inside of Player table after update is completed
print("-- DISPLAYING PLAYERS AFTER UPDATE --")
cursor.execute("SELECT player.player_id, player.first_name, player.last_name, team.team_name FROM player INNER JOIN team ON player.team_id = team.team_id;")
enr = cursor.fetchall()

for ene in enr:
    print("Player ID: {}\nFirst Name: {}\nLast Name: {}\nTeam Name: {}\n".format((ene[0]),(ene[1]),(ene[2]),(ene[3])))

# Delete newly added record
cursor.execute("DELETE FROM player WHERE first_name = 'Gollum';")

# Show all records inside of Player table after delete occurs
print("-- DISPLAYING PLAYERS AFTER DELETE --")
cursor.execute("SELECT player.player_id, player.first_name, player.last_name, team.team_name FROM player INNER JOIN team ON player.team_id = team.team_id;")
inp = cursor.fetchall()

for ine in inp:
    print("Player ID: {}\nFirst Name: {}\nLast Name: {}\nTeam Name: {}\n".format((ine[0]),(ine[1]),(ine[2]),(ine[3])))

db.close()