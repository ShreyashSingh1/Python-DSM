import mysql.connector

"""mydb is my connection string"""

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Lookinto@12"
)

print(mydb)

"""Cursor is like pointer which points to table ka data
we make cursor with help of connection string"""

mycursor = mydb.cursor()
mycursor.execute(operation="SHOW DATABASES")

"""With help of cursor will able to perform all the operation in sql using py file"""

for i in mycursor:
    print(i)


