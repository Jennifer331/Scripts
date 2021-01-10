import java.io.*;
import java.util.*;

public class InputTest {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    int t = in.nextInt();
    while (t-- > 0) {
      String s = in.nextLine();
      System.out.println(s);
    }
  }
}
