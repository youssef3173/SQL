import sqlite3
import os


db_name = "Ex1.db"

mydb = sqlite3.connect( db_name )
mycursor = mydb.cursor()



# Select the Oldest Album, Display id, name, release_year, band_id
mycursor.execute(""" SELECT id, name, MIN(release_year), band_id
					FROM albums
					;""")

res = mycursor.fetchone() 
print( res)


mydb.commit()
mydb.close()
print( "Done" )