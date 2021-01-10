import java.io.*;
import java.util.*;

public class Verify {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int dividen = 1;
        while (dividen > 0) {
            dividen = in.nextInt();
            int cnt = 0;
            for (int i = 1; i <= 100; i++) {
                if ((2 * i - 1) % dividen == 0) {
                    System.out.print(i + ", ");
                    cnt++;
                }
            }
            System.out.println("\n in total: " + cnt);
        }
    }
}
