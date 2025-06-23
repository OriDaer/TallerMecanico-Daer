import os
os.system('Cls')

import mysql.connector #---Importante

try:
   connection=mysql.connector.connect(
                                       host='localhost',
                                       port=3306,
                                       user='root',
                                       password='root',
                                       database='alumnos'
                                       )
   
   if connection.is_connected():
         print('Conexion exitosa')

except Exception as ex:
         print(ex)

cursor=connection.cursor()

def alta():
   insert_query = "INSERT INTO datos_personales (Matricula, Apellido_Nombre) VALUES (%s, %s)"
   matricu_la=int(input('Ingresar Matrícula: '))
   apellidonomb_re=input('Ingrese Apellido y Nombre: ')
   data = (matricu_la, apellidonomb_re)
   cursor.execute(insert_query, data)
   connection.commit()  # Confirmar los cambios en la base de datos

def consulta():
      query = "SELECT Apellido_Nombre, Matricula FROM datos_personales ORDER BY Apellido_Nombre"
      cursor.execute(query)
      # Obtener los resultados
      for row in cursor.fetchall():
            print(row)

def borrar():
   query="DELETE FROM datos_personales WHERE Matricula = %s"
   matricu_la=int(input('Ingresar Matrícula: '))
   data=(matricu_la)
   cursor.execute(query,(data,))
   print('Registro Borrado')
   connection.commit()
   print('')
   print('')
   print('')
   


def consulta_particular():
   query="SELECT Matricula, Apellido_Nombre FROM `datos_personales` WHERE Matricula=%s"
   matricu_la=int(input('Ingresar Matrícula: '))
   data=(matricu_la)
   cursor.execute(query,(data,))
   fila=cursor.fetchone()
   if fila is not None:
   # Acceder a los valores de cada columna
      Matricula       = fila[0]
      Apellido_Nombre = fila[1]
      print('Alumno --------------->',Matricula,Apellido_Nombre)
   else:
      print("No se encontraron resultados.")
      
def menu():
   print('1- Alta')
   print('2- Consulta')
   print('3- Borrar')
   print('4- Consulta Particular')
   print('5- Salir del Sistema')
   print('')
   print('')

#-----Programa---
opc=0
while opc !=5:
      menu()
      opc=int(input('Ingrese Opción: '))
      if opc==1:
         print('Alta')
         alta()
         print('')
         print('')

      if opc==2: 
         print('Consulta')  
         consulta()
         print('')
         print('')

      if opc==3:   
         print('Borrar')
         borrar()
         print('')
         print('')

      if opc==4:
         print('Consulta Particular')
         consulta_particular()
         print('')
         print('') 

      if opc==5:
         print('Salir del Sistema')
         break   
cursor.close()
connection.close()