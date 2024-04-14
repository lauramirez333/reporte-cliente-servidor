
"""Porgrama para preguntar por lineas de emergencia en un servidor
"""
# librerias
from socket import *
from _thread import * 
import time
import sys
import conectar
import pickle
## Función para inicializar el servidor, solicita la dirección IP del servidor y el puerto.
def ini ():
    host = input("Servidor: ")
    port = int (input("puerto"))
    return host, port
# Función para crear un nuevo socket.

def crearSocket():
    soc = socket(AF_INET, SOCK_STREAM)
    return soc
# Función para ligar el socket a la dirección y puerto especificados.

def ligarSocket(soc,host, port):
    while True:
        try:
            soc.bind((host, port))
            break
        except error as e:
            
            print("ERROR :( ", e)
# Función para aceptar conexiones entrantes.

def conexiones(soc):
    conn, addr = soc.accept()
    print ("\n Conexion establecida. \n El servidor es: ", addr[0] + ":"+ str(addr[1]))
    return conn, addr
# Función para enviar mensajes al cliente.

def  enviar(conn,opcion):
   
    msg = Telefonos(str(opcion))
    msg_serializado = pickle.dumps(msg)
    try:
        conn.send(msg_serializado)
    except:
        print("Algo ha pasado \n Intentalo en  5.. ")
        time.sleep(5)
# Función para recibir mensajes del cliente.
def recibir(conn):
    while True:
        try:
            reply = conn.recv(2048)
            if not reply:
                break
            reply = reply.decode("UTF-8")
            if reply.lower() != "exit":
                    print("Cliente:", reply)
                    start_new_thread(enviar, (conn,reply,))
            else:
                print("Cliente desconectado")
                break
        except:
            print("*********************************************\nNo se puede recibir respuesta\n *********************************************")
            time.sleep(5)
# Función para enviar un cliente especial.

# def enviarEspecial(conn):
#     global lista_de_clientes, client
#     client = lista_de_clientes.pop()
#     conn.send(client.encode("UTF-8"))
# #Usar variables globales
# bandera = False
# lista_de_clientes =["1"]
# client = ""
# Función para manejar los números de teléfono según la solicitud.

def Telefonos(argument):
    if argument.lower() == "admin":
        respuesta = conectar.consultar_base_de_datos_admin()
    elif argument.lower() == "vendedor1":
        respuesta = conectar.consultar_base_de_datos_vendedor("1")
    elif argument.lower() == "vendedor2":
        respuesta = conectar.consultar_base_de_datos_vendedor("2")
    else:
        respuesta = "No se admiten otras opciones"

    return respuesta


# Función principal para la conexión y manejo de los clientes.

def main():
    global bandera
    host, port = ini()
    soc = crearSocket()
    ligarSocket(soc, host, port)
    soc.listen(1) #variable para un cliente
    print("SERVIDOR ESCLAVO, NO ESCRIBIR SI NO HAY UNA PREGUNTA")
    print("Espeando clientes")
    conn, addr = conexiones(soc)
    #enviarEspecial(conn)
    start_new_thread(recibir,(conn,))
    while True:
        conn, addr = conexiones(soc)
        #enviarEspecial(conn)
        start_new_thread(recibir, (conn,))
    

main()

