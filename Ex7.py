import sqlite3
import os


db_name = "Ex1.db"

mydb = sqlite3.connect( db_name )
mycursor = mydb.cursor()

mycursor.execute( """ SELECT * FROM albums
					WHERE release_year IS NULL
					;""" )
print( mycursor.fetchall())

# Update the Release Year of the Album with No Release Year: NULL -> 1986
mycursor.execute( """ UPDATE albums
					SET release_year = 1986
					WHERE release_year IS NULL
					;""" )

mycursor.execute( """ SELECT * FROM albums
					WHERE release_year IS 1986
					;""" )
print( mycursor.fetchall())


mydb.commit()
mydb.close()
print( "Done" ) 