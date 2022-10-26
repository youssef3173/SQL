import sqlite3
import os


db_name = "Ex1.db"

mydb = sqlite3.connect( db_name )
mycursor = mydb.cursor()



# Insert a record for your favorite Band and one of their Albums:


mycursor.execute( "SELECT * FROM bands;")
print( mycursor.fetchall())
mycursor.execute( "SELECT * FROM albums;")
print( mycursor.fetchall())

mydb.commit()
mydb.close()
print( "Done" ) 