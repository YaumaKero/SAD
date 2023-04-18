import java.io.*;
import java.net.*;

public class MySocket {

    private Socket socket;
    private BufferedReader input;
    private PrintWriter output;

    public MySocket(String nick/* , int port*/) throws IOException {
        try {
            this.socket = new Socket(nick, 8080/* , port*/);
            this.input = new BufferedReader(new InputStreamReader(socket.getInputStream()));
            this.output = new PrintWriter(socket.getOutputStream(), true);
        } catch (IOException e) {
            throw new IOException("Error al conectar con el host " + nick + " en el puerto 8080", e);
        }
    }

    public MySocket(Socket socket) throws IOException {
        this.socket = socket;
        try {
            this.input = new BufferedReader(new InputStreamReader(socket.getInputStream()));
            this.output = new PrintWriter(socket.getOutputStream(), true);
        } catch (IOException e) {
            throw new IOException("Error al crear los streams de entrada/salida", e);
        }
    }

    public void close() throws IOException {
        try {
            socket.close();
        } catch (IOException e) {
            throw new IOException("Error al cerrar el socket", e);
        }
    }

    public String readLine() throws IOException {
        try {
            return input.readLine();
        } catch (IOException e) {
            throw new IOException("Error al leer una línea del stream de entrada", e);
        }
    }

    public void writeLine(String line) throws IOException {
        try {
            output.println(line);
        } catch (Exception e) {
            throw new IOException("Error al escribir una línea en el stream de salida", e);
        }
    }

    public int readInt() throws IOException {
        try {
            return input.read();
        } catch (IOException e) {
            throw new IOException("Error al leer un entero del stream de entrada", e);
        }
    }

    public void writeInt(int value) throws IOException {
        try {
            output.write(value);
            output.flush();
        } catch (IOException e) {
            throw new IOException("Error al escribir un entero en el stream de salida", e);
        }
    }

    public int rcv_message() {

    }

    public int snd_message() {

    }
    // Implementar los métodos read/write para los tipos básicos que se necesiten
}