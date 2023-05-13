import socket
import pickle
import TkMenu

## CONEXIÓN 1
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 8000))
# Enviar la solicitud de mazos al servidor
s.sendall(pickle.dumps('download'))
# Recibir los datos del servidor
data = s.recv(4096)
# Deserializar el objeto Mazos
mazos = pickle.loads(data)
s.close()

## EJECUCIÓN GRÁFICA
TkMenu.exec(mazos)

## CONEXIÓN 2
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 8000))
# Serializar el objeto Mazos
datos = pickle.dumps(mazos)
# Enviar el mensaje al servidor
s.sendall(datos)
s.close()