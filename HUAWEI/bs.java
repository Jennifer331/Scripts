import java.util.*;


public class bs {
    private static int[] findNum(int[] arr, int number) {
        int n = arr.length;

        int p1 = binarySearch(arr, number);
        if (arr[p1] != number) {
            return new int[]{-1, -1};
        }

        int start = p1;
        int end = p1;

        while(start >= 0) {
            if (arr[start] != number)
                break;
            start--;
        }

        while (end < n) {
            if (arr[end] != number)
                break;
            end++;
        }

        return new int[]{start + 1, end - 1};
    }

    private static int binarySearch(int[] arr, int number) {
        int n = arr.length;
        int lo = 0;
        int hi = n - 1;
        while (lo < hi) {
            int mid = lo + (hi - lo) / 2;
            if (arr[mid] == number) {
                return mid;
            } else if (arr[mid] < number) {
                lo = mid + 1;
            } else {
                hi = mid - 1;
            }
        }
        return lo;
    }

    public static void main(String[] args) {
        int[] test1 = new int[]{1,2,3,3,3,5,6,7};
        int[] ans1 = findNum(test1, 3);
        int[] ans2 = findNum(test1, 5);
        int[] ans3 = findNum(test1, 1000);

        System.out.println(ans1);
    }
}
