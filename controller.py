import sqlite3 as sql

from colorama import Cursor


def createDB():
    conn = sql.connect("inventario.db") #creo conexion con db
    conn.commit() #guardo los cambios
    conn.close() #cierro la conexion


#creo tablas    
def createTable():
    conn = sql.connect("inventario.db")
    cursor = conn.cursor()
    cursor.execute(
        """CREATE TABLE inventario (
            id integer,
            name text,
            cant integer,
            service text
            )"""
        )
    conn.commit()
    conn.close()

#inserto filas
def insertRow(id, name, cant, service):
    conn = sql.connect("inventario.db")
    cursor = conn.cursor()
    instruccion = f"INSERT INTO inventario VALUES ('{id}','{name}',{cant},'{service}') "
    cursor.execute(instruccion)
    conn.commit()
    conn.close()


#leo filas
def readRows():
    conn = sql.connect("inventario.db")
    cursor = conn.cursor()
    instruccion = f"SELECT * FROM inventario"
    cursor.execute(instruccion)
    datos = cursor.fetchall()    
    conn.commit()
    conn.close()
    print(datos)
    
    

#escribo variasfilas a la vez
def insertRows(inventarioList):
    conn = sql.connect("inventario.db")
    cursor = conn.cursor()
    instruccion = f"INSERT INTO inventario VALUES (?, ?, ?, ?)"
    cursor.executemany(instruccion, inventarioList)
    conn.commit()
    conn.close()



#leer datos ordenados
def readOrdered(field):
    conn = sql.connect("inventario.db")
    cursor = conn.cursor()
    instruccion = f"SELECT * FROM inventario ORDER BY {field}"
    cursor.execute(instruccion)
    datos = cursor.fetchall()
    conn.commit()
    conn.close()
    print(datos)
    

#buscar datos de la db
def search():
    conn = sql.connect("inventario.db")
    cursor = conn.cursor()
    instruccion = f"SELECT * FROM inventario WHERE cant=0"
    cursor.execute(instruccion)
    datos = cursor.fetchall()
    conn.commit()
    conn.close()
    print(datos)


#llamo la funcio pàra crear base de datos
#if __name__ == "__main__":
#    createDB() #creo db



#llamo al funcion para crear tablas
#if __name__ == "__main__":
#    createTable()



#funcion para insertar datos
#if __name__ == "__main__":
    #insertRow(1, "450", 0, "maternidad")
    #insertRow(2,"2360", 0, "tomografia")
#


#funcion para leer los datos de las filas
#if __name__ == "__main__":
#    readRows()


#llamo la funcion para insertar varios valores por fila a la vez
#if __name__ == "__main__":
#    inventario = [
#       (3,"1060",0,"ecografia"),
#        (4,"83A", 0, "salud laboral"),
#        (5, "85A", 0, "guardia")
#    ]
#    insertRows(inventario)

#funcion para ver lista ordenadodas
#if __name__=="__main__":
#   readOrdered("cant")

#funcion para buscar datos especificos
if __name__=="__main__":
    search()