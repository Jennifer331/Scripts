import java.util.*;
import java.io.*;

public class Solution {
    private static int[] possiblePermutation(int n, int a, int b, int c) {
        List<Integer> heights = new LinkedList<>();
        int l = a - c;
        for (int i = n - l; i < n; i++) {
            heights.add(i);
        }
        for (int i = 0; i < c; i++) {
            heights.add(n);
        }
        int r = b - c;
        for (int i = n - 1; i >= n - r; i--) {
            heights.add(i);
        }
        int[] ans = new int[n];
        if (heights.size() > n)
            return null;
        else if (heights.size() < n) {
            int padding = n - heights.size();
            int insertP = 1;
            for (int i = 1; i < heights.size(); i++) {
                if (heights.get(i) != 1 && heights.get(i - 1) != 1) {
                    insertP = i - 1;
                    break;
                }
            }
            int p = 0;
            for (int i = 0; i < heights.size(); i++) {
                ans[p++] = heights.get(i);
                if (i == insertP) {
                    while (padding-- > 0) {
                        ans[p++] = 1;
                    }
                }
            }
        } else {
            for (int i = 0; i < n; i++) {
                ans[i] = heights.get(i);
            }
        }
        return ans;
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(new BufferedReader(new InputStreamReader(System.in)));
        int t = in.nextInt();

        for (int i = 1; i <= t; i++) {
            int n = in.nextInt();
            int a = in.nextInt();
            int b = in.nextInt();
            int c = in.nextInt();

            int[] heights = possiblePermutation(n, a, b, c);
            StringBuilder sb = new StringBuilder();
            if (null == heights)
                sb.append(" IMPOSSIBLE");
            else {
                for (int h : heights) {
                    sb.append(" " + h);
                }
            }
            System.out.println("Case #" + i + ":" + sb.toString());

        }
    }
}
