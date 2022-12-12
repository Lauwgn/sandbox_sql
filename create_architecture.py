import mysql.connector

# Creating connection object
mydb = mysql.connector.connect(
    host = "localhost",
    user = "lau",
    password = "mdp"
)

cursor = mydb.cursor()

# Creation database
cursor.execute("CREATE DATABASE IF NOT EXISTS Azimut ")


# Création des tables
cursor.execute("USE Azimut")

cursor.execute("SHOW TABLES")
for x in cursor:
    print(x)

command_sql = (
    "CREATE TABLE IF NOT EXISTS `essais` ("
    " `champ_1` varchar(255)"
    ")"

               )
cursor.execute(command_sql)

cursor.execute("SHOW TABLES")
for x in cursor:
    print(x)
