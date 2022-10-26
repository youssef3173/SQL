import sqlite3
import os


db_name = "Ex1.db"

mydb = sqlite3.connect( db_name )
mycursor = mydb.cursor()


# Get the number of Songs for each Band: Double Join
mycursor.execute( """SELECT bands.name AS Band, COUNT(songs.name) AS 'Number of Songs' FROM bands
					INNER JOIN albums ON bands.id = albums.band_id 
					INNER JOIN songs ON albums.id = songs.album_id
					GROUP BY bands.name
					ORDER BY bands.id
					;""")
res = mycursor.fetchall()
for r in res:
	print( r)

mydb.commit()
mydb.close()
print( "Done" ) 