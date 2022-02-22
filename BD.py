#Ejemplo de conectividad a una base de datos, MySQL, SQL, SQLite3, SQLite, etc...
#VB

import mysql.connector

conexion1=mysql.connector.connect(host="localhost", 
                                  user="root", 
                                  passwd="", 
                                  database="bd1")
cursor1=conexion1.cursor()
cursor1.execute("show tables")
for tabla in cursor1:
    print(tabla)
conexion1.close()   

---------------------------------------------------------------------------------------------------------------------------------------------------

* Insertar filas en una tabla

import mysql.connector

conexion1=mysql.connector.connect(host="localhost", 
                                  user="root", 
                                  passwd="", 
                                  database="bd1")
cursor1=conexion1.cursor()
sql="insert into articulos(descripcion, precio) values (%s,%s)"
datos=("naranjas", 23.50)
cursor1.execute(sql, datos)
datos=("peras", 34)
cursor1.execute(sql, datos)
datos=("bananas", 25)
cursor1.execute(sql, datos)
conexion1.commit()
conexion1.close()

---------------------------------------------------------------------------------------------------------------------------------------------------

import sqlite3

conexion=sqlite3.connect("bd1.db")
try:
    conexion.execute("""create table articulos (
                              codigo integer primary key autoincrement,
                              descripcion text,
                              precio real
                        )""")
    print("se creo la tabla articulos")                        
except sqlite3.OperationalError:
    print("La tabla articulos ya existe")                    
conexion.close()


---------------------------------------------------------------------------------------------------------------------------------------------------

import sqlite3
 
conn = sqlite3.connect('tutorial3.db')
c = conn.cursor()
 
def create_table():
  c.execute("CREATE TABLE IF NOT EXISTS tabla1(unix REAL, fecha TEXT, palabraclave TEXT, valor REAL)")
 
def data_entry():
  c.execute("INSERT INTO tabla1 VALUES(1452549219,'2018-02-12 16:50:39','Python',6)")
  conn.commit()
  c.close()
  conn.close()
 
create_table()
data_entry()
