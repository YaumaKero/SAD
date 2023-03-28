import java.io.IOException;
import java.io.InputStreamReader;

import javax.sound.midi.MidiSystem;
import java.io.InputStreamReader;



public class EchoClient{
    public static void main(String[] args) {
        MySocket sc = new MySocket(args[0], Integer.parseInt(args[1]));

        //output
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
    
            
        
    }
}





