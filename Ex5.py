import sqlite3
import os


db_name = "Ex1.db"

mydb = sqlite3.connect( db_name )
mycursor = mydb.cursor()



# Bands >> Albums >> Songs
# Get all Bands that have No Albums:
mycursor.execute("""SELECT bands.name AS 'Band Name' FROM bands
					LEFT JOIN albums ON bands.id = albums.band_id
					GROUP BY bands.id
					HAVING COUNT(albums.id) = 0
					;""")
print( mycursor.fetchall(), "\n") 



mydb.commit()
mydb.close()
print( "Done" ) 