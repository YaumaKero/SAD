import java.io.*;
import java.net.*;

public class MyServerSocket {

    private ServerSocket serverSocket;

    public MyServerSocket(int port) throws IOException {
        try {
            this.serverSocket = new ServerSocket(port);
        } catch (IOException e) {
            throw new IOException("Error al crear el socket del servidor en el puerto " + port, e);
        }
    }

    public MySocket accept() throws IOException {
        try {
            Socket socket = serverSocket.accept();
            return new MySocket(socket);
        } catch (IOException e) {
            throw new IOException("Error al aceptar una conexión entrante", e);
        }
    }

    public void close() throws IOException {
        try {
            serverSocket.close();
        } catch (IOException e) {
            throw new IOException("Error al cerrar el socket del servidor", e);
        }
    }
}