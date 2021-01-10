import java.io.*;
import java.util.*;

public class Solution {

    private static int maxBeauty(ArrayList<LinkedList<Integer>> children, int[] brights) {
        return 1;
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(new BufferedReader(new InputStreamReader(System.in)));
        int t = in.nextInt();

        for (int i = 1; i <= t; i++) {
            int v = in.nextInt();
            int[] brights = new int[v];
            for (int j = 0; j < v; j++) {
                brights[j] = in.nextInt();
            }

            ArrayList<LinkedList<Integer>> children = new ArrayList<LinkedList<Integer>>(v);
            for (int j = 0; j < v; j++) {
                children.add(new LinkedList<>());
            }

            for (int j = 0; j < v - 1; j++) {
                int x = in.nextInt();
                int y = in.nextInt();
                children.get(x - 1).add(y - 1);
                children.get(y - 1).add(x - 1);
            }

            int y = maxBeauty(children, brights);
            System.out.println("Case #" + i + ": " + y);
        }
    }
}
