import java.util.*;
import java.io.*;

public class Generics {
    public static void main(String[] args) {
        // Map<Integer, Integer> m = new HashMap<>(1, 2);
        // for(int key : m.keySet()) {
        //     System.out.println(key + m.get(key));
        // }

        /*
        List<int[]> l = new LinkedList<>();
        l.add(new int[]{1,2,3,4});
        for (int[] arr : l) {
            for (int a : arr)
                System.out.print(a + ",");
        }
        System.out.println("Quit");
        */

        List<Integer> ints = Arrays.<Integer>asList(1, 2, 3);
        for (int i : ints)
            System.out.println(i);
    }
}
