
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="escuela"
)

mycursor = mydb.cursor()

sql = "SELECT * FROM estudiantes WHERE materia ='programacion'"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)