import java.io.*;
import java.util.*;


public class EditableBufferedReader extends BufferedReader {

    String str = null;
    Runtime runtime = Runtime.getRuntime();
    EditableBufferedReader(InputStreamReader in){
       super(in);      
    }
    
    public void setRaw(){
        String[] cmd = {"/bin/sh", "-c", "stty raw </dev/tty"};  //talvez es otro  comando pero la estructura esta bien
        try{
            runtime.exec(cmd);
        } catch (IOException e) { 
            e.printStackTrace(); 
        }        
    }
    public void unsetRaw(){
        String[] cmd = {"/bin/sh", "-c", "stty cooked </dev/tty"}; //talvez es otro  comando pero la estructura esta bien
        try{
            runtime.exec(cmd);
        } catch (IOException e) { 
            e.printStackTrace(); 
        }     
    }    
    // Por ahora no hace falta modificar read()

    // public char read(){  
    //     Scanner scanner = new Scanner(System.in);
    //     char character = scanner.next().charAt(0);
    // }
    public String readLine(){
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        Line line = new Line();
        char x;
        while(line.text.charAt(line.cursorPos)=='\n'){
            try{
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
            }catch (IOException e) { e.printStackTrace(); }                      
        }
        return null;
    }  
}


-------------------------------------------------------------------------------------






