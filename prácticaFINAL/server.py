import socket
import pickle
import deck
    
def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('localhost', 8000))
        s.listen()
        while True:
            conn, addr = s.accept()
            with conn:
                print(f'Conexión establecida con {addr}')
                with conn:
                    # Recibir los datos del cliente
                    data = conn.recv(4096)
                    # Decodificar los datos como una cadena
                    mensaje = data.decode()
                    # Verificar si el mensaje es de subida o envío de mazos
                    if mensaje.startswith('upload'):
                        # Quitar el prefijo del mensaje
                        datos = mensaje[len('upload:'):]
                        # Deserializar el objeto Mazos
                        mazos = pickle.loads(datos.encode())
                        # Sobreescribir el objeto Mazos
                        print(f'Se ha sobrescrito el objeto: {mazos}')
                    elif mensaje.startswith('download'):
                        # Serializar el objeto Mazos
                        datos = pickle.dumps(mazos)
                        # Crear un mensaje que indique que se está enviando un objeto Mazos
                        mensaje = f'mazos:{datos.decode()}'
                        # Enviar el mensaje al cliente
                        conn.sendall(mensaje.encode())

