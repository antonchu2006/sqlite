import sqlite3

##conectar
conexion = sqlite3.connect("sqlite3/test.sqlite3")
##cursor
consulta = conexion.cursor()
sql = """
CREATE TABLE IF NOT EXISTS test(
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    cadena_texto VARCHAT(50) NOT NULL,
    entero INTEGER NOT NULL,
    decimal FLOAT NOT NULL,
    fecha DATE NOT NULL)"""

#ejecutar consulta
if(consulta.execute(sql)): print("tabla creada con exito")
else: print("no se pudo crear")

#terminar consulta
consulta.close()

#guardar bases de datos
conexion.commit()
#cerramos conecxión
conexion.close()