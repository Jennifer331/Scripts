import java.util.*;

// remove all the duplicate numbers among the given numbers
// output numbers that only show once
public void DuplicateRemove {
    private List<Integer> remove(int[] arr) {
        Set<Integer> set = new HashSet<>();
        Set<Integer> dupSet = new HashSet<>();

        for (int n : arr) {
            if (!set.add(n)) {
                dupSet.add(n);
            }
        }

        List<Integer> ans = new LinkedList<>();
        for (int n : set) {
            if (!dupSet.contains(n)) {
                ans.add(n);
            }
        }

        return ans;
    }
}
