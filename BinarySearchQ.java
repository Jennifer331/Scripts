import java.lang.Math;
import java.util.Scanner;

/*
 Split the given array into K sub-arrays such that maximum sum of all sub arrays is minimum
 https://www.geeksforgeeks.org/split-the-given-array-into-k-sub-arrays-such-that-maximum-sum-of-all-sub-arrays-is-minimum/
*/
public class BinarySearchQ{
    public static void main(String[] args) {
        System.out.println("Split the given array into K sub-arrays such that maximum sum of all sub arrays is minimum\n\n  ");
        Scanner in = new Scanner(System.in);
        System.out.println("How many elements in the array?");
        int n = in.nextInt();
        int[] arr = new int[n];
        System.out.println("Please input elements:");
        for (int i = 0; i < n; i++) {
            arr[i] = in.nextInt();
        }

        System.out.println("How many parts do you want to split into?");
        int k = in.nextInt();
        int ans = minMaxSubSum(arr, k);
        System.out.println("Cutted into " + k + " parts, the minimum of maximum sum of all sub arrays is \n" + ans);
    }

    private static int minMaxSubSum(int[] arr, int k) {
        int sum = 0;
        int max = arr[0];
        for (int n : arr) {
            sum += n;
            max = Math.max(n, max);
        }

        return binarySearch(arr, k, max, sum);
    }

    private static int binarySearch(int[] arr, int k, int l, int r) {
        int ans = -1;
        while (l <= r) {
            int mid = l + (r - l) / 2;
            if (check(arr, k, mid)) {
                ans = mid;
                r = mid - 1;
            } else {
                l = mid + 1;
            }
        }
        return ans;
    }

    private static boolean check(int[] arr, int k, int maxSum) {
        int sum = 0;
        int i = 0;
        for (; k > 0 && i < arr.length; i++){
            if (sum + arr[i] <= maxSum) {
                sum += arr[i];
            } else {
                k--;
                sum = arr[i];
            }
        }
        return k > 0;
    }
}
