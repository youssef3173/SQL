import sqlite3  
import os

if os.path.isfile( "./record_company_bis.db" ):
	os.remove("./record_company_bis.db") 

# Create or Connect(if already exist) to a database:
mydb = sqlite3.connect( "record_company_bis.db" )
mycursor = mydb.cursor()


# Create a table:
mycursor.execute( """CREATE TABLE bands( 
					id INTEGER PRIMARY KEY AUTOINCREMENT,
					name VARCHAR(255) NOT NULL
					);""" )

mycursor.execute( """CREATE TABLE albums( 
					id INTEGER PRIMARY KEY AUTOINCREMENT,
					name VARCHAR(255) NOT NULL,
					release_year INTEGER,
					band_id INTEGER NOT NULL,  
					FOREIGN KEY (band_id) REFERENCES bands(id) 
					);""" )  


mycursor.execute( "INSERT INTO bands (name) VALUES( 'Band77'), ( 'Band2'), ( 'Band3'), ( 'Band13');" )
mycursor.execute( """INSERT INTO albums (name, release_year, band_id) 
					VALUES ('Beast', 1777, 1), 
					( 'Xion Ri', 1787, 3), 
					( 'Triple', 1987, 2),
					( 'Unknown', NULL, 1)
					;""" )



mycursor.execute( """SELECT bands.id, bands.name, albums.id, albums.name, albums.release_year, albums.band_id FROM albums
					INNER JOIN bands ON albums.id = bands.id
					;""" )
print( "Join albums and bands tables: \n", mycursor.fetchall() )


# # bands RIGHT JOIN albums   <=>  albums LEFT JOIN bands 
# mycursor.execute( """SELECT * FROM albums
# 					LEFT JOIN bands ON albums.id = bands.id
# 					;""" ) # RIGHT JOIN is not supported


# Agregate Functions: AVG, SUM, MAX, MIN
mycursor.execute("""SELECT AVG(release_year) FROM albums;""") 
print( "\nAverage: \n", mycursor.fetchall() )


mycursor.execute("""SELECT band_id, COUNT(band_id) FROM albums
					GROUP BY band_id
					;""") 
print( "\nGROUP BY COUNT(band_id): \n ", mycursor.fetchall() )






mycursor.execute("""SELECT b.name AS band_name, COUNT(a.id) AS num_albums
					FROM bands AS b
					LEFT JOIN albums AS a ON b.id = a.band_id
					GROUP BY b.id
					;""")
print( "\nNum Albums for Every Band_Name: \n", mycursor.fetchall() )



mycursor.execute("""SELECT b.name AS band_name, COUNT(a.id) AS num_albums
					FROM bands AS b
					LEFT JOIN albums AS a ON b.id = a.band_id
					GROUP BY b.id
					HAVING num_albums = 1
					;""")
# WHERE before GROUP BY Does not grow, bc WHRE take place before GROUP BY (therefore num_albums not found)
print( "\nNum Albums for Every Band_Name: \n", mycursor.fetchall() )



mycursor.execute("""SELECT b.name AS band_name, COUNT(a.id) AS num_albums
					FROM bands AS b
					LEFT JOIN albums AS a ON b.id = a.band_id
					WHERE b.name = 'Band13'
					GROUP BY b.id
					;""")
print( "\nNum Albums for Every Band_Name: \n", mycursor.fetchall() )


# Good practice to add this 2 lines
mydb.commit()
mydb.close()

print( "\nDone" )
