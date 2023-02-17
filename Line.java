import java.io.*;

class Line(){
    
    String text;
    int cursorPos;
    boolean editMode;
    boolean INSERTION=true;
    boolean SUBSTITUTION=false;
    
    Line(text,cursorPos,editMode){
        text="";
        cursorPos=0;
        editMode=INSERTION;
    }
}