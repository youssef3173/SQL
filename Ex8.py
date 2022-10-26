import sqlite3
import os


db_name = "Ex1.db"

mydb = sqlite3.connect( db_name )
mycursor = mydb.cursor()



# Insert a record for your favorite Band and one of their Albums:
mycursor.execute( "INSERT INTO bands(name) VALUES ('NewBand');")
mycursor.execute( "SELECT id FROM bands WHERE name = 'NewBand';")
band_id = mycursor.fetchone()[0]
mycursor.execute( "INSERT INTO albums(name, release_year, band_id) VALUES (?, ?, ?);", ('NewAlbum', 2022, band_id))

mycursor.execute( "SELECT * FROM bands;")
print( mycursor.fetchall())
mycursor.execute( "SELECT * FROM albums;")
print( mycursor.fetchall())

mydb.commit()
mydb.close()
print( "Done" ) 