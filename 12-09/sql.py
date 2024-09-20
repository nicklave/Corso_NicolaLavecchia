import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "root",
    port = 3306
)

mycursor = mydb.cursor()

db = "create database es_python"

mycursor.execute(db)