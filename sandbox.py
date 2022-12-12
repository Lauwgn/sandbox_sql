"""
see jupyter notebook
"""

# Importing module
import mysql.connector

# Creating connection object
mydb = mysql.connector.connect(
    host = "localhost",
    user = "lau",
    password = "mdp"
)

# Printing the connection object
print(mydb)

cursor = mydb.cursor()

cursor.execute("SHOW DATABASES")
for x in cursor:
    print(x)

cursor.execute("SELECT 'mysql_python';")
print(cursor)
for x in cursor:
    print(x)

cursor.execute("SHOW TABLES")

for x in cursor:
    print(x)

