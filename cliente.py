import socket
import sys
import time
import pickle
from tabulate import tabulate

def main():    # Solicita al usuario la dirección IP del servidor y el puerto.

    host = input("Ingresa la dirección IP del servidor: ")
    port = int(input("Ingresa el puerto del servidor: "))

    try:        # Crea un socket del cliente y se conecta al servidor.

        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((host, port))
        print("Conexión establecida con el servidor.")
        
        while True:        # Bucle principal para enviar mensajes al servidor.

            message = input("Ingrese su usuario (escribe 'exit' para salir): ")
            
            client_socket.send(message.encode())
            if message.lower() == 'exit':
                break
            # Espera la respuesta del servidor y la imprime.

            reply = client_socket.recv(2048)
            if len(reply) < 44:
                print ("***************************************************")
                print(f'*Sr {message} ud no tiene permisos para ver tablas*')
                print ("***************************************************")
            else:
                print ("*********************************************")
                print(f'*Sr {message} ud puede ver la siguiente tabla*')
                print ("*********************************************")
                print(tabulate(pickle.loads(reply), headers=['Producto', 'Descripción', 'Valor', 'Cantidad', 'Fecha de compra', 'Categoria'], tablefmt='grid'))
                
         # Cierra el socket del cliente después de terminar la comunicación.

        client_socket.close()
        print("Conexión cerrada.")
        
    except socket.error as e:
        print("Error al conectar:", e)
        sys.exit()

if __name__ == "__main__":
    main()
