import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Scanner;

import javax.sound.midi.MidiSystem;
import java.io.InputStreamReader;



public class EchoClient{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Escribe tu nombre: ");
        String nick = sc.nextLine();

        MySocket mysc = new MySocket(nick);

        Thread receivThread = new Thread(mysc.rcv_message);

        
        
        
        
        
        /*
        MySocket sc = new MySocket(args[0], Integer.parseInt(args[1]));
        //input
        new Thread(){
            public void run(){
                String line;
                BufferedReader kbd = new BufferedReader(new InputStreamReader(System.in));
                try{
                    while(line = kbd.readLine() != null){
                        sc.println(line);
                    }
                    
                }catch(IOException ex){
                    ex.printStackTrace();
                }
                sc.close();
                
            }
        }.start();
        //output
        new Thread(){
            public void run(){
                String line;
                while(line = sc.readLine() != null){
                    s.println(line);
                }
                sc.close();
            }
        }.start();
        */
            
        
    }
}




