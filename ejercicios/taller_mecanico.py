import os
import mysql.connector

# Limpiar pantalla
os.system('cls' if os.name == 'nt' else 'clear')

# Conexión a la base de datos
conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    port = 3306,
    password="root",
    database="taller_mecanico"
)
cursor = conexion.cursor()

def menu_secundario(nombre_tabla):
    while True:
        print(f"\n--- {nombre_tabla.upper()} ---") # Mostrar el nombre de la tabla en mayúsculas
        print("1 Alta | 2 Baja | 3 Modif | 4 Consulta general | 5 Consulta particular | 6 Volver")
        opcion = input("Seleccione una opción: ")

        if opcion == "1": alta(nombre_tabla)
        elif opcion == "2": baja(nombre_tabla)
        elif opcion == "3": modificacion(nombre_tabla)
        elif opcion == "4": consulta_general(nombre_tabla)
        elif opcion == "5": consulta_particular(nombre_tabla)
        elif opcion == "6": break
        else: print("Opción inválida.")

def alta(tabla):
    print(f"Alta en {tabla}")
    if tabla == "clientes":
        nombre = input("Nombre: ")
        apellido = input("Apellido: ")
        dni = input("DNI: ")
        telefono = input("Teléfono: ")
        direccion = input("Dirección: ")
        # el %s sirve para indicar que se van a insertar valores en esos lugares y el cursor.execute ejecuta la consulta
        cursor.execute("INSERT INTO clientes (nombre, apellido, dni, telefono, direccion) VALUES (%s, %s, %s, %s, %s)", (nombre, apellido, dni, telefono, direccion))
    elif tabla == "empleados":
        nombre = input("Nombre: ")
        apellido = input("Apellido: ")
        dni = input("DNI: ")
        puesto = input("Puesto: ")
        telefono = input("Teléfono: ")
        cursor.execute("INSERT INTO empleados (nombre, apellido, dni, puesto, telefono) VALUES (%s, %s, %s, %s, %s)", (nombre, apellido, dni, puesto, telefono))
    #elif tabla == "proveedores":
    #    empresa = input("Nombre de empresa: ")
    #    contacto = input("Nombre del contacto: ")
    #    telefono = input("Teléfono: ")
    #    direccion = input("Dirección: ")
    #    cursor.execute("INSERT INTO proveedores (nombre_empresa, contacto, telefono, direccion) VALUES (%s, %s, %s, %s)", (empresa, contacto, telefono, direccion))
    #elif tabla == "repuestos":
    #    nombre = input("Nombre: ")
    #    marca = input("Marca: ")
    #    precio = input("Precio: ")
    #    stock = input("Stock: ")
    #    cursor.execute("INSERT INTO repuestos (nombre, marca, precio, stock) VALUES (%s, %s, %s, %s)", (nombre, marca, precio, stock))
    elif tabla == " vehiculos":
        marca = input("Marca: ")
        modelo = input("Modelo: ")
        anio = input("Año: ")
        patente = input("Patente: ")
        id_cliente = input("ID Cliente: ")
        cursor.execute("INSERT INTO  vehiculos (marca, modelo, anio, patente, id_cliente) VALUES (%s, %s, %s, %s, %s)", (marca, modelo, anio, patente, id_cliente))
    elif tabla == "ficha_tecnica":
        id_rodado = input("ID Rodado: ")
        descripcion = input("Descripción: ")
        fecha = input("Fecha: ")
        cursor.execute("INSERT INTO ficha_tecnica (id_rodado, descripcion, fecha) VALUES (%s, %s, %s)", (id_rodado, descripcion, fecha))
    elif tabla == "facturacion":
        id_cliente = input("ID Cliente: ")
        monto = input("Monto total: ")
        fecha = input("Fecha: ")
        cursor.execute("INSERT INTO facturacion (id_cliente, monto_total, fecha) VALUES (%s, %s, %s)", (id_cliente, monto, fecha))
    #elif tabla == "presupuesto":
    #    id_cliente = input("ID Cliente: ")
    #    detalle = input("Detalle: ")
    #    monto = input("Monto estimado: ")
    #    fecha = input("Fecha: ")
    #    cursor.execute("INSERT INTO presupuesto (id_cliente, detalle, monto_estimado, fecha) VALUES (%s, %s, %s, %s)", (id_cliente, detalle, monto, fecha))
    else:
        print("Tabla no válida")
        return
    conexion.commit()
    print("Alta realizada correctamente.")

def baja(tabla):
    id_eliminar = input("ID a eliminar: ")
    cursor.execute(f"DELETE FROM {tabla} WHERE id = %s", (id_eliminar,))
    conexion.commit()
    print("Registro eliminado si existía.")

def modificacion(tabla):
    id_modificar = input("ID a modificar: ")
    #if tabla == "proveedores":
    #    empresa = input("Nombre de empresa: ")
    #    contacto = input("Nombre del contacto: ")
    #    telefono = input("Teléfono: ")
    #    direccion = input("Dirección: ")
    #    cursor.execute("UPDATE proveedores SET nombre_empresa = %s, contacto = %s, telefono = %s, direccion = %s WHERE id = %s", (empresa, contacto, telefono, direccion, id_modificar))
    #    conexion.commit()
    if tabla == "clientes":
        nombre = input("Nombre: ")
        apellido = input("Apellido: ")
        dni = input("DNI: ")
        telefono = input("Teléfono: ")
        direccion = input("Dirección: ")
        cursor.execute("UPDATE clientes SET nombre = %s, apellido = %s, dni = %s, telefono = %s, direccion = %s WHERE id = %s", (nombre, apellido, dni, telefono, direccion, id_modificar))
        conexion.commit()
    elif tabla == "empleados":
        nombre = input("Nombre: ")
        apellido = input("Apellido: ")
        dni = input("DNI: ")
        telefono = input("Teléfono: ")
        direccion = input("Dirección: ")
        cursor.execute("UPDATE empleados SET nombre = %s, apellido = %s, dni = %s, telefono = %s, direccion = %s WHERE id = %s", (nombre, apellido, dni, telefono, direccion, id_modificar))
        conexion.commit()
    #elif tabla == "repuestos":
    #    nombre = input("Nombre: ")
    #    marca = input("Marca: ")
    #    precio = input("Precio: ")
    #    stock = input("Stock: ")
    #    cursor.execute("UPDATE repuestos SET nombre = %s, marca = %s, precio = %s, stock = %s WHERE id = %s", (nombre, marca, precio, stock, id_modificar))
    #    conexion.commit()
    elif tabla == " vehiculos":
        marca = input("Marca: ")
        modelo = input("Modelo: ")  
        anio = input("Año: ")
        patente = input("Patente: ")
        id_cliente = input("ID Cliente: ")
        cursor.execute("UPDATE  vehiculos SET marca = %s, modelo = %s, anio = %s, patente = %s, id_cliente = %s WHERE id = %s", (marca, modelo, anio, patente, id_cliente, id_modificar))
        conexion.commit()

    elif tabla == "ficha_tecnica":
        id_rodado = input("ID Rodado: ")    
        descripcion = input("Descripción: ")
        fecha = input("Fecha: ")
        cursor.execute("UPDATE ficha_tecnica SET id_rodado = %s, descripcion = %s, fecha = %s WHERE id = %s", (id_rodado, descripcion, fecha, id_modificar))
        conexion.commit()
    elif tabla == "facturacion":
        id_cliente = input("ID Cliente: ")
        monto = input("Monto total: ")
        fecha = input("Fecha: ")
        cursor.execute("UPDATE facturacion SET id_cliente = %s, monto_total = %s, fecha = %s WHERE id = %s", (id_cliente, monto, fecha, id_modificar))
        conexion.commit()
    #elif tabla == "presupuesto":
    #    id_cliente = input("ID Cliente: ")
    #    detalle = input("Detalle: ")
    #    monto = input("Monto estimado: ")
    #    fecha = input("Fecha: ")
    #    cursor.execute("UPDATE presupuesto SET id_cliente = %s, detalle = %s, monto_estimado = %s, fecha = %s WHERE id = %s", (id_cliente, detalle, monto, fecha, id_modificar))
    #    conexion.commit()

    print("Modificación realizada correctamente.")
def consulta_general(tabla):
    cursor.execute(f"SELECT * FROM {tabla}")
                #cursor.fetchall() obtiene todas las filas de la consulta
    for fila in cursor.fetchall():
        print(fila)

def consulta_particular(tabla):
    id_buscar = input("ID a buscar: ")
    cursor.execute(f"SELECT * FROM {tabla} WHERE id = %s", (id_buscar,))
    fila = cursor.fetchone()
    if fila:
        print(fila)
    else:
        print("No encontrado.")

while True:
    print("""
---Menú Principal---
1 Clientes
2 Empleados
5  vehiculos
6 Ficha Técnica
9 Salir
""") #los """ permiten crear cadenas de texto multilínea"
    opcion = input("Seleccione una opción: ")
    if opcion == "1": menu_secundario("clientes")
    elif opcion == "2": menu_secundario("empleados")
    #elif opcion == "3": menu_secundario("proveedores")
    #elif opcion == "4": menu_secundario("repuestos")
    elif opcion == "5": menu_secundario(" vehiculos")
    elif opcion == "6": menu_secundario("ficha_tecnica")
    elif opcion == "7": menu_secundario("facturacion")
    #elif opcion == "8": menu_secundario("presupuesto")
    elif opcion == "9":
        print("Saliendo...")
        break
    else:
        print("Opción inválida.")

cursor.close()
conexion.close()

# abilitar el modulo d carga q un cliente tiene muchosrepuestos y dbeer cargar patente tipo de vehiculo y codigo d marca , tip de vehiculo

# un cliente tiene muchosrepuestos

#truncat table elimina de raiz los indices internos que tiene la tabla, por lo que no se puede usar en tablas que tengan relaciones con otras tablas
