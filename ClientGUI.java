import javax.swing.*;
import javax.swing.text.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.Socket;

public class ClientGUI extends JFrame {
    private String username;
    private Socket socket;
    private PrintWriter writer;
    private BufferedReader reader;
    private JTextPane chatPane;
    private JTextField messageField;
    private SimpleAttributeSet receivedStyle;
    private SimpleAttributeSet sentStyle;

    public ClientGUI(String username) {
        this.username = username;

        // Configuración de la ventana
        setTitle("Chat Client");
        setDefaultCloseOperation(EXIT_ON_CLOSE);
        setSize(400, 300);
        setLocationRelativeTo(null);

        // Crear componentes de la interfaz
        chatPane = new JTextPane();
        chatPane.setEditable(false);
        JScrollPane scrollPane = new JScrollPane(chatPane);
        messageField = new JTextField();
        JButton sendButton = new JButton("Send");

        // Agregar componentes a la ventana
        getContentPane().setLayout(new BorderLayout());
        getContentPane().add(scrollPane, BorderLayout.CENTER);
        getContentPane().add(messageField, BorderLayout.SOUTH);
        getContentPane().add(sendButton, BorderLayout.EAST);

        // Configurar acciones del botón de enviar
        sendButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                sendMessage();
            }
        });

        // Establecer el enfoque en el campo de mensaje
        messageField.requestFocus();

        // Establecer estilos para los mensajes recibidos y enviados
        receivedStyle = new SimpleAttributeSet();
        StyleConstants.setForeground(receivedStyle, Color.BLACK);
        sentStyle = new SimpleAttributeSet();
        StyleConstants.setForeground(sentStyle, Color.BLUE);

        // Conectar al servidor
        connectToServer();

        // Iniciar el hilo para recibir mensajes
        Thread receiveThread = new Thread(this::receiveMessage);
        receiveThread.start();
    }

    private void connectToServer() {
        try {
            socket = new Socket("127.0.0.1", 8080);
            writer = new PrintWriter(socket.getOutputStream(), true);
            reader = new BufferedReader(new InputStreamReader(socket.getInputStream()));

            // Enviar el nombre de usuario al servidor
            writer.println(username);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    private void receiveMessage() {
        try {
            String message;
            while ((message = reader.readLine()) != null) {
                appendToChatPane(message, receivedStyle);
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    private void sendMessage() {
        String message = messageField.getText();
        if (!message.isEmpty()) {
            writer.println(message);
            appendToChatPane(username + ": " + message, sentStyle);
            messageField.setText("");
        }
    }

    private void appendToChatPane(String message, AttributeSet style) {
        Document doc = chatPane.getDocument();
        try {
            doc.insertString(doc.getLength(), message + "\n", style);
        } catch (BadLocationException e) {
            e.printStackTrace();
        }
    }

    public static void main(String[] args) {
        String username = JOptionPane.showInputDialog(null, "Enter your username:");
        if (username == null || username.isEmpty()) {
            return;
        }

        SwingUtilities.invokeLater(() -> {
            ClientGUI client = new ClientGUI(username);
            client.setVisible(true);
        });
    }
}

