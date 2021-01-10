import java.io.*;
import java.util.*;

public class Workout {
    private static int minDiff(int[] m, int k) {
        int min = Integer.MAX_VALUE;
        int max = Integer.MIN_VALUE;
        int[] gaps = new int[m.length - 1];
        for (int i = 1; i < m.length; i++) {
            gaps[i - 1] = m[i] - m[i - 1];
            min = Math.min(gaps[i - 1], min);
            max = Math.max(gaps[i - 1], max);
        }
        return binarySearch(gaps, Math.max(1, min), max, k);
    }

    private static int binarySearch(int[] gaps, int l, int r, int k) {
        int ans = -1;
        while (l <= r) {
            int mid = l + (r - l) / 2;
            if (check(gaps, mid, k)) {
                ans = mid;
                r = mid - 1;
            } else {
                l = mid + 1;
            }
        }
        return ans;
    }

    private static boolean check(int[] gaps, int minDiff, int k) {
        for (int gap : gaps) {
            while (gap > minDiff) {
                gap -= minDiff;
                k--;
            }
        }
        return k >= 0;
    }

    private static int minDiff_dataset1(int[] m, int k) {
        PriorityQueue q = new PriorityQueue<Integer>(Collections.reverseOrder());
        for (int i = 1; i < m.length; i++) {
            q.add(m[i] - m[i - 1]);
        }
        while (k-- > 0) {
            int max = (int)q.poll();
            q.add(max / 2);
            q.add(max - max / 2);
        }
        return (int)q.peek();
    }
    public static void main(String[] args) {
        Scanner in = new Scanner(new BufferedReader(new InputStreamReader(System.in)));
        int t = in.nextInt();

        for (int i = 1; i <= t; i++) {
            int n = in.nextInt();
            int k = in.nextInt();

            int[] m = new int[n];
            for (int j = 0; j < n; j++) {
                m[j] = in.nextInt();
            }

            int ans = minDiff(m, k);
            System.out.println("Case #" + i + ": " + ans);
        }
    }
}
