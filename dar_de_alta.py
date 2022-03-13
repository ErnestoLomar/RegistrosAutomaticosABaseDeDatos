import mysql.connector
import random
from datetime import datetime

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="importada"
)

mycursor = mydb.cursor()

nombres = ["Ernesto", "Maria", "Angel", "Ricardo", "Angeles", "Fabio", "Norma",
"Mario", "Fernando", "Daniela", "Ivan", "Rosenda", "Perla", "Arturo", "Ana", "Julissa", "Antonio", "Jose",
"Manuel", "Francisco", "David", "Javier", "Carlos", "Gaspar", "Gerardo", "Luisa", "Luis", "Marcelo",
"Marcos", "Marco"]

apellidos = ["Lopez", "Martinez", "Sanchez", "Gonzales", "Mendoza", "Torres", "Gomez",
"Flores", "Perez", "Espinoza", "Ramirez", "Vargas", "Fernandez", "Gutierrez", "Ruiz", "Reyes", "Morales", "Alvarez",
"Castillo", "Castro", "Cruz", "Salazar", "Rivera", "Hernandez", "Leon", "Ostiguin", "Cordova", "Aguilar",
"Delgado", "Cardenas"]

inicio_uno = datetime(2018, 1, 1)
final_uno =  datetime(2020, 12, 30)

inicio_dos = datetime(2019, 2, 1)
final_dos =  datetime(2021, 12, 30)

print("Creando la base de datos...")

for i in range(500):
  random_date_uno = inicio_uno + (final_uno - inicio_uno) * random.random()
  random_date_dos = inicio_dos + (final_dos - inicio_dos) * random.random()
  sql = "INSERT INTO empleado (id, nombre, apellido1, apellido2, idDepartamento, salario_mensual, fecha_ingreso, fecha_baja, id_status) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
  val = ((i+1), nombres[random.randint(0, 29)], apellidos[random.randint(0, 29)], apellidos[random.randint(0, 29)],
   random.randint(1, 3), random.randint(5000, 30000), str(random_date_uno)[0:10], str(random_date_dos)[0:10], random.randint(1, 2))
  mycursor.execute(sql, val)
  mydb.commit()

print("Se ingresarón correctamente 500 registros")

