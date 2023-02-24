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
        setRaw();
        char x;
        boolean exit = false;
        System.out.println("modo de escritura: "+ line.insertionMode);
        while(exit==false){
            try{
                x=(char)in.read();
                //int asciival = x;
                //System.out.println(asciival);
            switch(x){
                case 13://valor del enter
                    System.out.print("\b \b\b \b");
                    exit=true;
                    break;
                
                case 127://valor del backspace
                    System.out.print("\b \b\b \b\b \b");
                    StringBuilder MyString = new StringBuilder(line.text);
                    MyString = MyString.deleteCharAt(line.cursorPos-1);
                    line.cursorPos--;
                    line.text=MyString.toString();
                    break;

                case 27:
                    in.read();
                    x=(char)in.read();
                    if(x==68){
                        System.out.print("\b \b\b \b\b \b\b \b");
                        for(int i=line.cursorPos;i)
                        line.cursorPos--;
                    }
                    else if(x==67){
                        System.out.print("\b \b\b \b\b \b\b \b");
                        line.cursorPos++;
                    }
                    else if(x==72){
                        System.out.print("\b \b\b \b\b \b\b \b");
                        line.cursorPos=0;
                    }
                    else if(x==70){
                        System.out.print("\b \b\b \b\b \b\b \b");
                        line.cursorPos=line.text.length();
                    }
                    else if(x==50){                              //puede dar problemas pq hay un caracter mas que en las otras teclas
                        line.insertionMode=!line.insertionMode;
                        in.read();  
                        System.out.print("\b \b\b \b\b \b\b \b\b \b");                             //esto debería arreglarlo
                    }
                    break;                
                
                default:
                    if(line.insertionMode == false){
                        StringBuilder sb = new StringBuilder(line.text);
                        sb.setCharAt(line.cursorPos, x);
                        line.text=sb.toString();
                    }
                    else if(line.insertionMode == true){
                        StringBuilder stringBuilder= new StringBuilder(line.text);
                        stringBuilder.insert(line.cursorPos,x);
                        line.text=stringBuilder.toString();
                        for(int i=line.cursorPos+1;i<line.text.length();i++)
                            System.out.print(line.text.charAt(i));
                        for(int i=line.cursorPos+1;i<line.text.length();i++)
                            System.out.print("\b");
                    }            
                    line.cursorPos++;
            }
            //System.out.println(line.text+line.cursorPos);                
            }catch (IOException e) { e.printStackTrace(); }                      
        }
        this.unsetRaw();
        return line.text;
    }  
}
