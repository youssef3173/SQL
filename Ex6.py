import sqlite3
import os


db_name = "Ex1.db"

mydb = sqlite3.connect( db_name )
mycursor = mydb.cursor()



# Get the Longest Album:
mycursor.execute("""SELECT albums.name AS Name, albums.release_year AS 'Release Year', SUM(songs.length) AS Duration FROM albums 
					LEFT JOIN songs ON albums.id = songs.album_id
					GROUP BY albums.name
					ORDER BY Duration DESC
					LIMIT 1
					;""")

print( mycursor.fetchall())



mydb.commit()
mydb.close()
print( "Done" ) 