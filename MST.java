import java.util.*;

public class MST {
    static int spanningTree(int V, int E, ArrayList<ArrayList<Integer>> graph) {
        // Add your code here
        Set<Integer> visited = new HashSet<>();
        visited.add(0);
        int ans = 0;

        while (visited.size() < V) {
            int next = -1;
            int min = Integer.MAX_VALUE;
            for (int n : visited) {
                List<Integer> out = graph.get(n);
                for (int i = 0; i < out.size(); i++) {
                    if (!visited.contains(i) && out.get(i) < min) {
                        next = i;
                        min = out.get(i);
                    }
                }
            }

            if (next == -1)
                break;

            visited.add(next);
            ans += min;
        }

        return ans;
    }
}
