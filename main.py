import pandas as pd
import mysql.connector

from src.add_action_from_tracker import add_action_from_tracker, delete_product

# Import action

df_backup = pd.read_csv('data/backup_azimut_210301_210531_very_short.csv')
# print(df_backup)




# Connection mysql
cnx = mysql.connector.connect(
    host = "localhost",
    user = "lau",
    password = "mdp",
    database = "Azimut"
)

cursor = cnx.cursor()

# for i in range(10):
#     action = df_backup.iloc[i]
#     # print(action)
#
#     add_action_from_tracker(action, cursor)
#     cnx.commit()

delete_product("60ae897c89fe135ad8391b31", cursor)
cnx.commit()

cursor.close()
cnx.close()