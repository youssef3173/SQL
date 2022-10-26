import sqlite3
import os


db_name = "Ex1.db"

mydb = sqlite3.connect( db_name )
mycursor = mydb.cursor()


# Get the Average Length of all Songs:
mycursor.execute( "SELECT AVG(length) FROM songs;")
print( mycursor.fetchall())

mydb.commit()
mydb.close()
print( "Done" ) 