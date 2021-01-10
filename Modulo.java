public class Modulo {
    public static void main(String[] args) {
        System.out.println(-58 % 60);
        System.out.println(58 % 60);
        modulo(3);

        String str1 = "hello";
        String str2 = "he" + new String("llo");
        String str3 = "he" + "llo";
        System.err.println(str1 == str2);
        System.err.println(str1 == str3);
    }

    private static void modulo(int n) {
        System.out.println(n);
    }
}
