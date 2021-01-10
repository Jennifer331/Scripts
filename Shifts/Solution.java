import java.io.*;
import java.util.*;

/*
  2019 Round G Shifts
*/
public class Solution {
    static int n;
    static int h;
    static int[] a = new int[20];
    static int[] b = new int[20];

    //Test set 1 passed, Test set 2 TLE
    //double needed
    private static int dfs(double aCur, double bCur, int day) {
        if (day == n) {
            if (aCur >= h && bCur >= h)
                return 1;
            return 0;
        }

        int ans = dfs(aCur + a[day], bCur, day + 1);
        ans += dfs(aCur + a[day], bCur + b[day], day + 1);
        ans += dfs(aCur, bCur + b[day], day + 1);

        return ans;
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(new BufferedReader(new InputStreamReader(System.in)));
        int t = in.nextInt();

        for (int i = 1; i <= t; i++) {
            n = in.nextInt();
            h = in.nextInt();
            for (int j = 0; j < n; j++) {
                a[j] = in.nextInt();
            }
            for (int j = 0; j < n; j++) {
                b[j] = in.nextInt();
            }
            int y = dfs(0, 0, 0);
            System.out.println("Case #" + i + ": " + y);
        }
    }
}
