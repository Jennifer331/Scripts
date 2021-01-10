public class Not{

    public static void main(String[] args) {
        int cnt = 0;

        for (int i = -50; i <= 50; i++) {
            if (~i != -1-i)
                System.out.println(i + "");
            else
                cnt++;
        }
        System.out.println(cnt + " QUIT");
    }
}
