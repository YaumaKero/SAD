
//VERSION ACTUALIZADA CON CONSTANTES

import java.io.*;

public class EditableBufferedReader extends BufferedReader {

    String str = null;
    public static final int ESC = 27;
    public static final int HOME = 72;
    public static final int END = 70;
    public static final int RIGHT = 67;
    public static final int LEFT = 68;
    public static final int DELETE = 51;
    public static final int BACKSPACE = 127;
    public static final int TOGGLE = 50;
    public static final int RETURN = 13;
    Runtime runtime = Runtime.getRuntime();
    EditableBufferedReader(InputStreamReader in){
       super(in);      
    }
    
    public void setRaw(){
        String[] cmd = {"/bin/sh", "-c", "stty raw </dev/tty"};  
        try{
            runtime.exec(cmd);
        } catch (IOException e) { 
            e.printStackTrace(); 
        }        
    }
    public void unsetRaw(){
        String[] cmd = {"/bin/sh", "-c", "stty cooked </dev/tty"}; 
        try{
            runtime.exec(cmd);
        } catch (IOException e) { 
            e.printStackTrace(); 
        }     
    } 
    
    public String readLine(){
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        Line line = new Line();
        setRaw();
        char x;
        boolean exit = false;
        while(exit==false){
            try{
                x=(char)in.read();
            switch(x){
                case RETURN:
                    System.out.print("\b \b\b \b");
                    exit=true;
                    break;
                
                case BACKSPACE:
                    if(line.cursorPos==0){
                        System.out.print("\b \b\b \b");
                        for(int i=0;i<line.text.length();i++)
                            System.out.print(line.text.charAt(i));
                        for(int i=0;i<line.text.length();i++)
                            System.out.print("\b");
                        break;
                    }
                    System.out.print("\b \b\b \b\b \b");
                    StringBuilder MyString = new StringBuilder(line.text);
                    MyString = MyString.deleteCharAt(line.cursorPos-1);
                    line.text=MyString.toString();
                    for(int i=line.cursorPos-1;i<line.text.length();i++)
                            System.out.print(line.text.charAt(i));
                    for(int i=line.cursorPos-1;i<line.text.length();i++)
                            System.out.print("\b");
                    line.cursorPos--;
                    break;

                case ESC:
                    in.read();
                    x=(char)in.read();
                    if(x==LEFT){
                        if(line.cursorPos==0){
                            System.out.print("\b \b\b \b\b \b\b \b");
                            for(int i=0;i<line.text.length();i++)
                                System.out.print(line.text.charAt(i));
                            for(int i=0;i<line.text.length();i++)
                                System.out.print("\b");
                            break;
                        }
                        System.out.print("\b \b\b \b\b \b\b \b");
                        for(int i=line.cursorPos;i<line.text.length();i++)
                            System.out.print(line.text.charAt(i));
                        for(int i=line.cursorPos;i<line.text.length();i++)
                            System.out.print("\b");
                        System.out.print("\b");
                        line.cursorPos--;
                    }
                    else if(x==RIGHT){
                        System.out.print("\b \b\b \b\b \b\b \b");
                        if(line.insertionMode){
                            if(line.cursorPos+1<line.text.length()){
                                for(int i=line.cursorPos;i<line.text.length();i++)
                                    System.out.print(line.text.charAt(i));
                                for(int i=line.cursorPos+1;i<line.text.length();i++)
                                    System.out.print("\b");
                                line.cursorPos++;
                            }
                        }
                        else{
                            if(line.cursorPos<line.text.length()){
                                for(int i=line.cursorPos;i<line.text.length();i++)
                                    System.out.print(line.text.charAt(i));
                                for(int i=line.cursorPos+1;i<line.text.length();i++)
                                    System.out.print("\b");
                                line.cursorPos++;
                            }
                        }
                    }
                    else if(x==HOME){
                        System.out.print("\b \b\b \b\b \b\b \b");
                        for(int i=line.cursorPos;i<line.text.length();i++)
                            System.out.print(line.text.charAt(i));
                        for(int i=0;i<line.text.length();i++)
                            System.out.print("\b");
                        line.cursorPos=0;
                    }
                    else if(x==END){
                        System.out.print("\b \b\b \b\b \b\b \b");
                        for(int i=line.cursorPos;i<line.text.length()-1;i++)
                                System.out.print(line.text.charAt(i));
                        line.cursorPos=line.text.length()-1;
                    }
                    else if(x==TOGGLE){ 
                        line.insertionMode=!line.insertionMode;
                        in.read();  
                        System.out.print("\b \b\b \b\b \b\b \b\b \b"); 
                        for(int i=line.cursorPos;i<line.text.length();i++)
                            System.out.print(line.text.charAt(i));
                        for(int i=line.cursorPos;i<line.text.length();i++)
                            System.out.print("\b");
                    }
                    else if(x==DELETE){                       
                        in.read();  
                        System.out.print("\b \b\b \b\b \b\b \b\b \b");
                        StringBuilder sb = new StringBuilder(line.text);
                        if(line.cursorPos+1<line.text.length()){
                            sb.deleteCharAt(line.cursorPos);
                            line.text=sb.toString();
                            for(int i=line.cursorPos;i<line.text.length();i++)
                                System.out.print(line.text.charAt(i));
                            for(int i=line.cursorPos;i<line.text.length();i++)
                                System.out.print("\b");
                        }
                    }
                    break;                
                
                default:
                    if(line.insertionMode == false){
                        if(line.cursorPos==line.text.length()){
                            line.text=line.text+x;
                        }
                        else{
                            StringBuilder sb = new StringBuilder(line.text);
                            sb.setCharAt(line.cursorPos, x);
                            line.text=sb.toString();
                        }
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
            }catch (IOException e) { e.printStackTrace(); }                      
        }
        this.unsetRaw();
        return line.text;
    }  
}
