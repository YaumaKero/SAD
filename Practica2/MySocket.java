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
        try {
        while (true) {
            String missatge = new BufferedReader(new InputStreamReader(sc.getInputStream())).readLine();
            if (missatge.equals("CLOSE")) {
                System.out.println("Conexió tancada" + "\033[0m");
                sc.close();
                break;
            }
            if (missatge.equals("USERNAME")) {
                sc.getOutputStream().write((username + "\n").getBytes("ASCII"));
            } else {
                System.out.println(missatge);
            }
        }
    } catch (Exception e) {
        System.out.println(e);
        System.out.println("\033[2;31m" + "Hi ha hagut algun error" + "\033[0m");
        try {
            sc.close();
        } catch (IOException ex) {
            ex.printStackTrace();
        }
    }


    }

    public int snd_message() {
        try {
        while (true) {
            Scanner scanner = new Scanner(System.in);
            String missatge = scanner.nextLine();
            if (missatge.equals(bye)) {
                System.out.println("\n\033[6;31m" + "Tancant conexió..." + "\033[0m");
                sc.getOutputStream().write("CLOSE\n".getBytes("ASCII"));
                scanner.close();
                System.exit(0);
            } else {
                String missatge_f = "\033[1;36m" + username + ": " + "\033[3;33m" + missatge + "\033[0m";
                sc.getOutputStream().write((missatge_f + "\n").getBytes("ASCII"));
            }
        }
    } catch (Exception e) {
        System.out.println(e);
        System.out.println("\033[2;31m" + "Hi ha hagut algun error" + "\033[0m");
        try {
            sc.close();
        } catch (IOException ex) {
            ex.printStackTrace();
        }
    }  
    }
    // Implementar los métodos read/write para los tipos básicos que se necesiten
}
