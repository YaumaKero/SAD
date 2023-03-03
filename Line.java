import java.io.*;

public class Line{
    
    String text;
    int cursorPos;
    boolean insertionMode;
    
    Line(){
        this.text = " ";
        this.cursorPos = 0;
        this.insertionMode = true;
    }
}
