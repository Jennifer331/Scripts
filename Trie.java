import java.io.*;
import java.util.*;

/*
    https://practice.geeksforgeeks.org/problems/trie-insert-and-search/0
*/
public class Trie {
    static final int ALPHABET_SIZE = 26;
    static class TrieNode {
        boolean isWord;
        TrieNode[] children;
        TrieNode(boolean isEnd) {
            isWord = isEnd;
            children = new TrieNode[ALPHABET_SIZE];
        }
    }

    private static int find(String[] words, String target) {
        TrieNode root = new TrieNode(false);
        for (String word : words) {
            insert(word, root);
        }
        boolean exist = search(root, target);
        return exist ? 1 : 0;
    }

    private static void insert(String word, TrieNode root) {
        for (char c : word.toCharArray()) {
            if (null == root.children[c - 'a'])
                root.children[c - 'a'] = new TrieNode(false);
            root = root.children[c - 'a'];
        }
        root.isWord = true;
    }

    private static boolean search(TrieNode root, String word) {
        for (char c : word.toCharArray()) {
            root = root.children[c - 'a'];
            if (null == root)
                break;
        }
        if (null != root && root.isWord)
            return true;
        return false;
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(new BufferedReader(new InputStreamReader(System.in)));
        int t = in.nextInt();
        while (t-- > 0) {
            int n = in.nextInt();
            in.nextLine();
            String s = in.nextLine();
            String[] words = s.split(" ");
            String target = in.nextLine();
            int ans = find(words, target);
            System.out.println(ans);
        }
    }
}
