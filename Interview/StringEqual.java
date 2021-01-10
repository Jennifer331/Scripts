public class StringEqual {

    private final static String target = "HelloCisco!";
    private final static String target2 = "Hello Cisco!";

    private final static String str1 = "HelloCisco!";
    private final static String str2 = "Hello" + "Cisco!";
    private final static String str3 = target.trim();
    private final static String str4 = target2.trim();

    public static String getString() {
        return "HelloCisco!";
    }

    public static void main(String[] args) {
        System.out.println("Test result is[");
        System.out.print((target == str1) ? "true," : "false,");
        System.out.print((target == str2) ? "true," : "false,");
        System.out.print((target == str3) ? "true," : "false,");
        System.out.print((target == str4) ? "true," : "false,");
        System.out.print((target == getString()) ? "true]" : "false]");
    }
}
