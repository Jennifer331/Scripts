import java.util.*;

public class Polymorphism{
    public static void main(String[] args) {
        //conc2, map2 and map9 are false which are counterintuitive
        //Is List<Dog> a subclass of List<Animal>? Why are Java generics not implicitly polymorphic?
        //https://stackoverflow.com/questions/2745265/is-listdog-a-subclass-of-listanimal-why-are-java-generics-not-implicitly-po
        List<List<Integer>> abs = new ArrayList<>(4);
        // List<List<Integer>> abs1 = new ArrayList<List<>>(4);//x
        List<ArrayList<Integer>> abs2 = new ArrayList<>(4);
        // List<ArrayList<Integer>> abs4 = new ArrayList<ArrayList<>>(4);//x
        List<ArrayList<Integer>> abs3 = new ArrayList<ArrayList<Integer>>(4);
        // ArrayList<List<Integer>> conc1 = new ArrayList<ArrayList<Integer>>(4);//x
        ArrayList<List<Integer>> conc = new ArrayList<>(4);
        // ArrayList<List<Integer>> conc1 = new ArrayList<ArrayList<>>(4);//x
        // ArrayList<List<Integer>> conc2 = new ArrayList<ArrayList<Integer>>(4);//x
        // ArrayList<ArrayList<Integer>> conc3 = new ArrayList<ArrayList<>>(4);//x
        ArrayList<ArrayList<Integer>> conc4 = new ArrayList<ArrayList<Integer>>(4);
        System.out.println("----------------");

        SortedMap<Integer, List<String>> map = new TreeMap<>();
        // SortedMap<Integer, List<String>> map1 = new TreeMap<Integer, LinkedList<>>();//x
        // SortedMap<Integer, List<String>> map2 = new TreeMap<Integer, LinkedList<String>>();//x
        SortedMap<Integer, List<String>> map3 = new TreeMap<Integer, List<String>>();
        SortedMap<Integer, LinkedList<String>> map4 = new TreeMap<Integer, LinkedList<String>>();

        Map<Integer, List<String>> map5 = new HashMap<>();
        // Map<Integer, List<String>> map6 = new HashMap<Integer, List<>>();//x
        Map<Integer, List<String>> map7 = new HashMap<Integer, List<String>>();
        // Map<Integer, List<String>> map8 = new HashMap<Integer, LinkedList<>>();//x
        // Map<Integer, List<String>> map9 = new HashMap<Integer, LinkedList<String>>();//x

        System.out.println("Quit");
    }
}
