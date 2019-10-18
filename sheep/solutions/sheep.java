import java.io.*;
import java.util.*;

public class sheep {

  public static void main(String[] args) {
    Scanner keyboard = new Scanner(System.in);
    int sheepNum = keyboard.nextInt();
    for (int i = 1; i < sheepNum + 1; i++) {
      System.out.print(i + " sheep... ");
    }

    keyboard.close();
  }
}