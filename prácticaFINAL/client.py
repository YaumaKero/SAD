import socket
import pickle
import deck

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(('localhost', 8000))
        # Solicitar los mazos al servidor
        with s:
            # Enviar la solicitud de mazos al servidor
            s.sendall('download'.encode())
            # Recibir los datos del servidor
            data = s.recv(4096)
            # Decodificar los datos como una cadena
            mensaje = data.decode()
            # Verificar si el mensaje es de un objeto Mazos
            if mensaje.startswith('mazos:'):
                # Quitar el prefijo del mensaje
                datos = mensaje[len('mazos:'):]
                # Deserializar el objeto Mazos
                mazos = pickle.loads(datos.encode())
                # Hacer algo con el objeto recibido
                print(f'Se ha recibido el objeto: {mazos}')
        # Hacer algo con los mazos recibidos

        #...

        # Enviar los mazos al servidor
        # Serializar el objeto Mazos
        datos = pickle.dumps(deck)
        # Crear un mensaje que indique que se está enviando un objeto Mazos
        mensaje = f'mazos:{datos.decode()}'
        # Enviar el mensaje al servidor
        s.sendall(mensaje.encode())
