import sqlite3, datetime

print("**** Programa para insertar registros en la tabla de pruebas ****")

cadena_texto = input("Introduzca texto: ")
entero = input("Introduzca un numero entero: ")
decimal = input("Introduce un numero decimal: ")

try: entero = int(entero)
except ValueError:
    print(entero, "no es entero")
    exit()

try: decimal = float(decimal) or int(decimal)
except ValueError:
    print(decimal, "no es un numero decimal")
    exit()

#aync
conexion = sqlite3.connect("sqlite3/test.sqlite3")

#cursor
consulta = conexion.cursor()

#valor de los argumentos
argumentos = (cadena_texto, entero, decimal, datetime.date.today())

sql = """
INSERT INTO test(cadena_texto, entero, decimal, fecha)
VALUES (?, ?, ?, ?)
"""

#consulta
if(consulta.execute(sql, argumentos)):
    print("Guardado con exito")
else: ("ha ocurrido un error!")


consulta.close()
conexion.commit()
conexion.close()