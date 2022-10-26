"""
Source: https://www.youtube.com/watch?v=p3qvj9hO_Bo&ab_channel=WebDevSimplified
What is SQL: Structered Query Language
	Language Designed Creating, Reading, Updating, Loading and Deleting data from a Database,
What is a Database:
	A collection of data separated into different tables, and each table (rows and columns) 
	represente a module (User, Product, Orders ... table ) and those tables are 
	linking to each other to create connection between data.

	example of a table: columns -> properties,  rows -> records
	 |   id   |      name    | date of birth |   age    |   blood type  |
	----------------------------------------------------------------------
	 |	 1    |      John    |   07/07/1997  |    26    |       X       |
	 |	 2    |     Suzane   |   07/07/1998  |    25    |       Q       |
	 |	 3    |      Dave    |   07/07/1999  |    24    |       A       |
	 |	 4    |      Bob     |   07/07/2000  |    23    |       J       |

	Relational database: related database, collection of linked tables

	Data is used in nemourous applications, that's why learning to manage databases
	is important, and SQL is one of the best ways to do this task.

Install MySQL connector: (simple way)
	C:/Users/Youssef/Desktop/SublimeText/SQL> python -m pip install mysql-connector-python
	Replace / with \

SQL data types:
	NUL, INTEGER, REAL, TEXT, BLOB
"""



import sqlite3  

# Create or Connect(if already exist) to a database:
mydb = sqlite3.connect( "Demo0.db" )
mycursor = mydb.cursor()


# use triple signle quote if you intend to write multiple lines,
# Create a table:
mycursor.execute( """CREATE TABLE employees(
					firstName TEXT,
					lastName TEXT,
					pay INTEGER
					) """ )


# Create an employee row: 
mycursor.execute( "INSERT INTO employees VALUES( 'John', 'James', 50000 );" )
mycursor.execute( "INSERT INTO employees VALUES( 'Suzane', 'James', 45000 );" )
mycursor.execute( "INSERT INTO employees VALUES( ?, ?, ? );", ( 'Dave', 'James', 40000 ) )
mycursor.execute( "INSERT INTO employees VALUES( :first, :last, :pay );", { 'first':'Bob', 'last':'James', 'pay':35000} )

# Select rows by a property:
mycursor.execute( "SELECT * FROM employees WHERE lastName='James' ")
mycursor.execute( "SELECT * FROM employees WHERE firstName=?", ('Dave',) )
mycursor.execute( "SELECT * FROM employees WHERE lastName=:last", {'last':'James'} )

# Display results of selection:
print( mycursor.fetchone())	 	# first row or None
print( mycursor.fetchmany( 2))   	# 2 first rows or []
print( mycursor.fetchall()) 	   	# all rows or []


# Same Task Using Classes and Functions:
class empc:
	def __init__( self, first, last, pay ):
		self.first = first
		self.last = last
		self.pay = pay

def insert_emp1( emp ):
	mycursor.execute( "INSERT INTO employees VALUES( :first, :last, :pay );", 
		{'first':emp.first, 'last':emp.last, 'pay':emp.pay} )

def insert_emp2( emp ):
	with mydb:
		mycursor.execute( "INSERT INTO employees VALUES( :first, :last, :pay );", 
			{'first':emp.first, 'last':emp.last, 'pay':emp.pay} )

def get_emps_by_last( lastname ):
	mycursor.execute( "SELECT * FROM employees WHERE lastName=:last", {'last':lastname} )
	return mycursor.fetchall()

def update_pay(emp, pay):
    with mydb:
        mycursor.execute("""UPDATE employees SET pay = :pay
                    WHERE firstName = :first AND lastName = :last""",
                  {'first': emp.first, 'last': emp.last, 'pay': pay})

def remove_emp(emp):
    with mydb:
        mycursor.execute("DELETE from employees WHERE firstName = :first AND lastName = :last",
                  {'first': emp.first, 'last': emp.last})

emp_obj = empc( 'Mike', 'Doe', 40000 )
insert_emp1( emp_obj)
update_pay( emp_obj, 42000)
print( get_emps_by_last( 'Doe' ) )
remove_emp( emp_obj)


# Good practice to add this 2 lines
mydb.commit()
mydb.close()

print( "Done" )
