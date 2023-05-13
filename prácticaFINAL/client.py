import io
import socket
import pickle
import time

#def main():
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 8000))
mazos = []
# Enviar la solicitud de mazos al servidor
s.sendall(pickle.dumps('download'))
# Recibir los datos del servidor
data = s.recv(4096)

print(data)
    # Deserializar el objeto Mazos
mazos = pickle.loads(data)
    # Hacer algo con el objeto recibido
print('Se ha recibido el objeto: {}'.format(mazos))
# Hacer algo con los mazos recibidos
s.close()
mazos.append(1)
time.sleep(2)
print(mazos)
# Enviar los mazos al servidor
# Serializar el objeto Mazos
datos = pickle.dumps(mazos)
print(datos)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 8000))
# Crear un mensaje que indique que se está enviando un objeto Mazos
#mensaje = 'upload:{}'.format(datos.decode('utf-8'))
# Enviar el mensaje al servidor
s.sendall(datos)
s.close()
print("conexion cerrada")