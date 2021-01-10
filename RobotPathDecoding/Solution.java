import java.util.*;
import java.io.*;

/*
  2020 Round B Robot Path Decoding
*/
public class Solution {
    private static int[] maneuver(String s) {
        char[] ops = s.toCharArray();
        Stack<Integer> times = new Stack<>();
        Stack<Integer[]> cnts = new Stack<>();

        int N = 0;
        int S = 0;
        int W = 0;
        int E = 0;

        for (char op : ops) {
            if (Character.isDigit(op)) {
                times.add(op - '0');
                cnts.add(new Integer[]{N, S, W, E});
                N = 0; S = 0; W = 0; E = 0;
            } else if (Character.isLetter(op)) {
                switch(op) {
                    case 'N': N++; break;
                    case 'S': S++; break;
                    case 'W': W++; break;
                    case 'E': E++; break;
                }
            } else if (op == ')') {
                int time = times.pop();
                Integer[] history = cnts.pop();
                N = N * time + history[0];
                S = S * time + history[1];
                W = W * time + history[2];
                E = E * time + history[3];
            }
        }

        int x = 1 + E - W;
        int y = 1 + S - N;
        if (x <= 0) {
            x = (int)Math.pow(10, 9) + x;
        }
        if (y <= 0) {
            y = (int)Math.pow(10, 9) + y;
        }
        return new int[]{x, y};
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(new BufferedReader(new InputStreamReader(System.in)));
        int t = in.nextInt();
        in.nextLine();
        for (int i = 1; i <= t; i++) {
            String ops = in.nextLine();
            int[] ans = maneuver(ops);
            System.out.println("Case #" + i + ": " + ans[0] + " " + ans[1]);
        }
    }
}
