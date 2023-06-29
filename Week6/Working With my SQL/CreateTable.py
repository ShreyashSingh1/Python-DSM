import mysql.connector


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Lookinto@12"
)


mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE if not exists test1.test_table(c1 INT)")

mydb.close()
