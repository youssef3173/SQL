import sqlite3
import os


db_name = "Ex1.db"

mydb = sqlite3.connect( db_name )
mycursor = mydb.cursor()



# Delete the Band and Album you added in #Ex8:
mycursor.execute( "SELECT MAX(id) FROM bands;")
band_id = mycursor.fetchone()[0]
mycursor.execute( "DELETE FROM albums WHERE band_id = :band_id;", {'band_id': band_id})
mycursor.execute( "DELETE FROM bands WHERE id = :band_id;", {'band_id': band_id})

mycursor.execute( "SELECT * FROM bands;")
print( mycursor.fetchall())
mycursor.execute( "SELECT * FROM albums;")
print( mycursor.fetchall())

mydb.commit()
mydb.close()
print( "Done" ) 