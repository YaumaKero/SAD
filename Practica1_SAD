import java.io.*;
import jline.Terminal;


public class EditableBufferedReader extends BufferedRead {

    private Terminal terminal;
    String str = null;
    
    public EditableBufferedReader(){
        terminal = Terminal.setupTerminal();
        try{
            terminal.init();
        }catch(Expetion e){
            e.printStackTrace();
        }
        terminal.setEchoEnabled(false);
    }
    public void setRaw(){
        terminal.setRawMode();
    }
    public void unsetRaw(){
        terminal.setEchoEnabled(true);
        terminal.setCookedMode();
    }
    public void read(){
        Scanner scanner = new Scanner(System.in);
        char character = scanner.next().charAt(0);
    }
    public void readLine(){
        while(true){        
            try {
                str = in.readLine();
            }
        }   
    }  
}


-------------------------------------------------------------------------------------






