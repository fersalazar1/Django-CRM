import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'Nandito12',
)


#Prepare a cursor object

cursorObject = dataBase.cursor()

#Create DB

cursorObject.execute("CREATE DATABASE crmp")

print("Ready!")