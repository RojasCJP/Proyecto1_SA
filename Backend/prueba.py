import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt

# Configuración de la conexión a la base de datos
config = {
    'user': 'root',
    'password': 'root',
    'host': 'mysqldb',
    'database': 'employees',
}

# Conexión a la base de datos
try:
    cnx = mysql.connector.connect(**config)
    print("Conexión exitosa a la base de datos")
    
    # Obtención de las tablas de la base de datos
    cursor = cnx.cursor()
    cursor.execute("SHOW TABLES")
    tables = cursor.fetchall()
    print("Tablas:")
    for table in tables:
        print(table[0])
        
except mysql.connector.Error as err:
    print("Error de conexión a la base de datos: {}".format(err))

finally:
    if 'cnx' in locals():
        cnx.close()
        print("Conexión cerrada")
