import socket
import pickle
import deck

mazos = [deck.Deck("Example deck")]
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('localhost', 8000))
s.listen()

while True:
    print("---Esperando conexión...---")
    conn, addr = s.accept()
    print('Conexión establecida con {}'.format(addr))
    # Recibir los datos del cliente
    data = conn.recv(4096)
    mensaje = pickle.loads(data)
    # Verificar si el mensaje es de subida o envío de mazos
    if isinstance(mensaje,str):
        print("---Solicitud de envío recibida---")
        # Serializar el objeto Mazos
        datos = pickle.dumps(mazos)
        # Enviar el mensaje al cliente
        conn.sendall(datos)
        print("---Mazos enviados---")
        conn.close()
    else:
        print("---Solicitud de backup recibida---")
        # Sobreescribir el objeto Mazos
        mazos = mensaje
        print("---Se ha sobrescrito la colección---")
        conn.close()
    print("---Conexión cerrada---")  