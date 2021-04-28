import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="tanson7899@mgail.com",
  password="MYpassword7899"
)

mycursor = mydb.cursor()

#mycursor.execute("CREATE DATABASE mydatabase")
mycursor.execute("SHOW DATABASES")

for x in mycursor:
  print(x)

  