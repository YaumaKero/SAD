import socket
import pickle
    
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(('localhost', 8000))
    mazos = [1,2,3]
    s.listen()
        
    while True:
        print("esperando aceptación")
        conn, addr = s.accept()
    
        print('Conexión establecida con {}'.format(addr))
    
        # Recibir los datos del cliente
        data = conn.recv(4096)
        # Decodificar los datos como una cadena
        mensaje = pickle.loads(data)
        #mensaje = data.decode('utf-8')
        print(mensaje)
        # Verificar si el mensaje es de subida o envío de mazos
        if isinstance(mensaje,str):
            # Serializar el objeto Mazos
            datos = pickle.dumps(mazos)
            print(datos)
            # Crear un mensaje que indique que se está enviando un objeto Mazos
            mensaje = 'mazos:{}'.format(datos)
            # Enviar el mensaje al cliente
            conn.sendall(datos)
            conn.close()
        else:
            print("He recibido: ")
            print(mensaje)
            # Quitar el prefijo del mensaje
            #datos = mensaje[len('upload:'):]
            # Deserializar el objeto Mazos
            mazos = mensaje
            # Sobreescribir el objeto Mazos
            print('Se ha sobrescrito el objeto: {}'.format(mazos))
            print(mazos)
            conn.close()
                