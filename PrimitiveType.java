public class PrimitiveType {
    public static void main(String[] args) {
        int x = Integer.MAX_VALUE;
        long y = x * x;

        long x1 = Integer.MAX_VALUE;
        long y1 = x1 * x1;

        System.out.println("x: " + x + ", y: " + y);
        System.out.println("x1: " + x1 + ", y1: " + y1);
    }
}
