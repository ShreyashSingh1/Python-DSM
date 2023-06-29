import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Lookinto@12"
)

mycursor = mydb.cursor()

"""Saving data to database"""
mycursor.execute("insert into test.test_table values('Shreyash', 123, 1.33, 'Singh')")
mycursor.execute("insert into test.test_table values('Shreyash', 123, 1.33, 'Singh')")
mycursor.execute("insert into test.test_table values('Shreyash', 123, 1.33, 'Singh')")
mycursor.execute("insert into test.test_table values('Shreyash', 123, 1.33, 'Singh')")
mycursor.execute("insert into test.test_table values('Shreyash', 123, 1.33, 'Singh')")
mydb.commit()

"""Fetching data from DB"""
mycursor.execute("SELECT * FROM test.test_table")
for i in mycursor.fetchall():
    print(i)
    
mycursor.execute("SELECT C1 FROM test.test_table")
for i in mycursor.fetchall():
    print(i)

mydb.close()
