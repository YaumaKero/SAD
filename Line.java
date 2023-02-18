import java.io.*;

public class Line{
    
    String text;
    int cursorPos;
    boolean editMode;
    boolean INSERTION=true;
    boolean SUBSTITUTION=false;
    
    Line(){
        this.text = "";
        this.cursorPos = 0;
        this.editMode = INSERTION;
    }
}
