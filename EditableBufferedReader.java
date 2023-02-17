import java.io.*;
import jline.Terminal;


public class EditableBufferedReader extends BufferedRead {

    private Console console;
    String str = null;
    
    //Opcion 1---------------------
    public void setRaw(){
        console.setRawMode(true);
        console.setEchoEnabled(false);
    }
    public void unsetRaw(){
        terminal.setEchoEnabled(true);
        terminal.setCookedMode();
    }
    //Opcion 2-----------------
    public void setRaw(){
        String[] cmd = {"/bin/sh", "-c", "stty raw </dev/tty"};
        Runtime.getRuntime().exec(cmd);
    }
    public void unsetRaw(){
        String[] cmd = {"/bin/sh", "-c", "stty cooked </dev/tty"};
        Runtime.getRuntime().exec(cmd);     
    }
    
    public void read(){
        Scanner scanner = new Scanner(System.in);
        char character = scanner.next().charAt(0);
    }
    public void readLine(){
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        Line line = new Line();
        char x;
        while(line.text.charAt(line.cursorPos)=='\n'){
            x=(char)in.read();
            switch(x){
                case '\n':
                    break;
                
                case 27:
                    in.read();
                    x=(char)in.read();
                    if(x==68)
                        line.cursorPos--;
                    else if(x==67)
                        line.cursorPos++;
                    else if(x==72)
                        line.cursorPos=0;
                    else if(x==70)
                        line.cursorPos=line.text.length();
                    else if(x==50){                              //puede dar problemas pq hay un caracter mas que en las otras teclas
                        line.editMode=!line.editMode;
                        in.read();                               //esto debería arreglarlo
                    }
                    break;
                
                
                default:
                    if(line.editMode==line.SUBSTITUTION){
                        StringBuilder sb = new StringBuilder(line.text);
                        sb.setCharAt(line.cursorPos, x);
                        line.text=sb.toString();
                    }
                    else if(line.editMode==line.INSERTION){
                        StringBuilder stringBuilder= new StringBuilder(line.text);
                        stringBuilder.insert(line.cursorPos,x);
                        line.text=stringBuilder.toString();
                    }
            
                    line.cursorPos++;
            }
        
        }
    }  
}


-------------------------------------------------------------------------------------






