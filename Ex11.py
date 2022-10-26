import sqlite3
import os


db_name = "Ex1.db"

mydb = sqlite3.connect( db_name )
mycursor = mydb.cursor()


# Select the longest Song off each Album:
mycursor.execute( """SELECT albums.name AS Name, albums.release_year, MAX(songs.length) AS Duration FROM albums
					INNER JOIN songs ON albums.id = songs.album_id 
					GROUP BY albums.name
					ORDER BY albums.id
					;""")
res = mycursor.fetchall()
for r in res:
	print( r)

mydb.commit()
mydb.close()
print( "Done" ) 