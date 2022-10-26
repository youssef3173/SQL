import sqlite3  
import os

if os.path.isfile( "./record_company.db" ):
	os.remove("./record_company.db") 

# Create or Connect(if already exist) to a database:
mydb = sqlite3.connect( "record_company.db" )
mycursor = mydb.cursor()


# Create a table:
mycursor.execute( """CREATE TABLE bands( 
					id INTEGER PRIMARY KEY AUTOINCREMENT,
					name VARCHAR(255) NOT NULL
					);""" )

# PRIMARY KEY (id)  # unique identifier " always != NULL"
# Elements of this column vannot take the value NULL


mycursor.execute( """CREATE TABLE albums( 
					id INTEGER PRIMARY KEY AUTOINCREMENT,
					name VARCHAR(255) NOT NULL,
					release_year INTEGER,
					band_id INT NOT NULL,  
					FOREIGN KEY (band_id) REFERENCES bands(id) 
					);""" )  
""" second identifier:
	removing an band implies removing the album related to it too
	bands(id) : first column in the bands table
"""
mycursor.execute( "INSERT INTO bands (name) VALUES( 'Band77');" )
mycursor.execute( "INSERT INTO bands (name) VALUES( 'Band2'), ( 'Band3');" )

mycursor.execute( "SELECT * FROM bands;" )           	# select all(*) from the bands table
mycursor.execute( "SELECT * FROM bands LIMIT 2;" )   	# returns 2 first rows
mycursor.execute( "SELECT id as 'ID', name FROM bands LIMIT 2;" )    	# returns 'id' as 'ID'
mycursor.execute( "SELECT * FROM bands ORDER BY name DESC;" )    		# or ASC (default)
print( "SELECT * FROM bands ORDER BY name DESC: " )
print( mycursor.fetchall()) 
print( "\n" )


mycursor.execute( """INSERT INTO albums (name, release_year, band_id) 
					VALUES ('Beast', 1777, 1), 
					( 'Xion Ri', 1787, 3), 
					( 'Triple', 1987, 2),
					( 'Unknown', NULL, 1);""" )


mycursor.execute( "SELECT DISTINCT band_id FROM albums;" )  	# removes duplicates
print( "SELECT DISTINCT band_id FROM albums: " )
print( mycursor.fetchall())
print( "\n" )

mycursor.execute( """ UPDATE albums
					SET release_year = 1955
					WHERE id = 1
					;""" )

mycursor.execute( """ SELECT * FROM albums
					WHERE release_year < 1955 AND  0 < id < 4 
					;""" )

mycursor.execute( """ SELECT * FROM albums
					WHERE release_year BETWEEN 1755 AND 1955 
					;""" )

mycursor.execute( """ SELECT * FROM albums
					WHERE release_year IS NULL 
					;""" )


mycursor.execute( """ SELECT id, name FROM albums
					WHERE name LIKE '%ri%' OR band_id = 1
					;""" )

print( "SELECT * FROM albums WHERE name LIKE '%ri%' OR band_id = 1: ")
print( mycursor.fetchall())
print( "\n" )


mycursor.execute( """ DELETE FROM albums
					WHERE id = 1
					;""" )

mycursor.execute( """ DELETE FROM albums
					WHERE release_year IS NULL
					;""" )

mycursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
print( "Tables names: " )
print( mycursor.fetchall())





# Good practice to add this 2 lines
mydb.commit()
mydb.close()

print( "Done" )
