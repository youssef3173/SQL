import sqlite3
import os


db_name = "Ex1.db"

mydb = sqlite3.connect( db_name )
mycursor = mydb.cursor()


# Bands >> Albums >> Songs
# Get all Bands that have Albums:
mycursor.execute(""" SELECT DISTINCT bands.name AS 'Band Name' FROM albums
					LEFT JOIN bands
					ON bands.id = albums.band_id
					;""")

res = mycursor.fetchall() 
for r in res:
	print( r)


mydb.commit()
mydb.close()
print( "Done" )