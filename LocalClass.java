public class LocalClass {
    public static void main(String[] args) {
        InnerClass1 c = new InnerClass1();
        System.out.println(c.a);
    }

    private void test() {
        class InnerClass1 {
            int a = 1;
        }
    }
}
