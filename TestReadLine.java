import java.io.*;

class TestReadLine {
  public static void main(String[] args) {
    BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
    String str = null;
    int a = 0;
    try {
      //str = in.readLine();
      a = in.read();
    } catch (IOException e) { e.printStackTrace(); }
    System.out.println("\nline is: " + str);
  }
}
