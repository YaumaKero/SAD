import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.Socket;

public class Client {
    private String username;
    private Socket socket;
    private String bye;

    public Client(String username) {
        this.username = username;
        this.bye = "adeu";

        try {
            this.socket = new Socket("127.0.0.1", 8080);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public void receiveMessage() {
        try {
            BufferedReader reader = new BufferedReader(new InputStreamReader(socket.getInputStream()));
            String message;

            while ((message = reader.readLine()) != null) {
                if (message.equals("CLOSE")) {
                    System.out.println("\u001B[31mConexió tancada\u001B[0m");
                    socket.close();
                    break;
                }
                if (message.equals("USERNAME")) {
                    PrintWriter writer = new PrintWriter(socket.getOutputStream(), true);
                    writer.println(username);
                } else {
                    System.out.println(message);
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
            System.out.println("\u001B[31mHi ha hagut algun error\u001B[0m");
            try {
                socket.close();
            } catch (IOException ex) {
                ex.printStackTrace();
            }
        }
    }

    public void sendMessage() {
        try {
            BufferedReader userInput = new BufferedReader(new InputStreamReader(System.in));
            PrintWriter writer = new PrintWriter(socket.getOutputStream(), true);
            String message;

            while ((message = userInput.readLine()) != null) {
                if (message.equals(bye)) {
                    System.out.println("\u001B[31mTancant conexió...\u001B[0m");
                    writer.println("CLOSE");
                    socket.close();
                    System.exit(0);
                } else {
                    String formattedMessage = "\u001B[36m" + username + ": " + "\u001B[33m" + message + "\u001B[0m";
                    writer.println(formattedMessage);
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public static void main(String[] args) {
        BufferedReader userInput = new BufferedReader(new InputStreamReader(System.in));
        String username;

        System.out.print("\n\u001B[35mEscriu el teu nom d'usuari: \u001B[0m");
        try {
            username = userInput.readLine();
            username = username + (int)(Math.random() * 9) + (int)(Math.random() * 9) + (int)(Math.random() * 9);
            System.out.println("\u001B[37mUsuari: \u001B[34m" + username + "\u001B[0m\n");

            Client client = new Client(username);

            Thread receiveThread = new Thread(client::receiveMessage);
            receiveThread.start();

            Thread writeThread = new Thread(client::sendMessage);
            writeThread.start();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
