import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.HashMap;
import java.util.Map;

public class Server {
    private ServerSocket serverSocket;
    private Map<String, Socket> clients;

    public Server() {
        try {
            serverSocket = new ServerSocket(8080);
            clients = new HashMap<>();
            System.out.println("\n\u001B[35mWelcome to Server\u001B[0m");
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public void broadcast(String message, Socket sender) {
        for (Socket client : clients.values()) {
            if (client != sender) {
                try {
                    PrintWriter writer = new PrintWriter(client.getOutputStream(), true);
                    writer.println(message);
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
        }
    }

    public void handle(String username) {
        Socket client = clients.get(username);

        try {
            BufferedReader reader = new BufferedReader(new InputStreamReader(client.getInputStream()));
            String message;

            while ((message = reader.readLine()) != null) {
                if (message.equals("CLOSE")) {
                    System.out.println(username + " \u001B[33mS'ha desconnectat\u001B[0m");
                    PrintWriter writer = new PrintWriter(client.getOutputStream(), true);
                    writer.println("CLOSE");
                    client.close();
                    clients.remove(username);
                    break;
                } else {
                    broadcast(message, client);
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public void acceptConnections() {
        while (true) {
            try {
                Socket client = serverSocket.accept();
                System.out.println("\u001B[35mConnexio nova amb " + client.getRemoteSocketAddress() + "\u001B[0m");

                PrintWriter writer = new PrintWriter(client.getOutputStream(), true);
                writer.println("USERNAME");

                BufferedReader reader = new BufferedReader(new InputStreamReader(client.getInputStream()));
                String username = reader.readLine();

                clients.put(username, client);
                System.out.println("\u001B[33mUsuari: " + username);

                broadcast(username + " s'ha unit al chat!\n", client);

                Thread thread = new Thread(() -> handle(username));
                thread.start();
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
    }

    public static void main(String[] args) {
        Server server = new Server();
        server.acceptConnections();
    }
}
