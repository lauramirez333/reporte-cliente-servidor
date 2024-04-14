import pymysql
from tabulate import tabulate
import pickle
def conexionsql():
    try:
        conexion = pymysql.connect(host='localhost', user='root', passwd='motorola', db='supermercado')
       
        return  conexion
        # cursor =conexion.cursor()
        # cursor.execute("Select * from usuarios;")
        # row = cursor.fetchone()
        # print(row)
    except Exception as Ex:
        print(Ex)

def consultar_base_de_datos_admin():
    miConexion = conexionsql()
    cur = miConexion.cursor()
    cur.execute("SELECT producto, descripcion, cantidad, fecha, categoria FROM productos ")
    resultados = cur.fetchall()
    miConexion.close()
    return resultados

def consultar_base_de_datos_vendedor(vendedor):
    miConexion = conexionsql()
    cur = miConexion.cursor()
    consulta = "SELECT producto, descripcion, valor, cantidad, fecha, categoria FROM productos where categoria = " + vendedor
    cur.execute(consulta)
    resultados = cur.fetchall()
    miConexion.close()
    return resultados
# def consultar_base_de_datos_vendedor2():
#     miConexion = conexionsql()
#     cur = miConexion.cursor()
#     cur.execute("SELECT producto, descripcion, valor, cantidad, fecha, categoria FROM productos where categoria = 2")
#     resultados = cur.fetchall()
#     miConexion.close()
#     return resultados
# msg = "hola"
# msg_serializado = pickle.dumps(msg)
# print(msg_serializado)
# print(pickle.loads(msg_serializado))
#print(tabulate(consultar_base_de_datos(), headers=['Producto', 'Descripción'], tablefmt='grid'))