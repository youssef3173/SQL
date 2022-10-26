import sqlite3
import os


db_name = "Ex1.db"

mydb = sqlite3.connect( db_name )
mycursor = mydb.cursor()



# Change the name of the column the data returns to Band Name
mycursor.execute(""" SELECT name AS 'Band Name'
					FROM bands
					;""")

list_bands = mycursor.fetchall() 
for bname in list_bands:
	print( bname)

mydb.commit()
mydb.close()
print( "Done" )