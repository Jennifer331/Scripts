public class Solution2 {
    static final int N = 8;

    static int[] inCol = new int[N];
    static int[] inDiag = new int[2 * N];
    static int[] inReDiag = new int[2 * N];
    static int[][] hasQueue = new int[N][N];
    static int cnt = 0;

    private static void put(int i) {
        if (i == N) {
            cnt++;
            print();
            return;
        }

        for (int j = 0; j < N; j++) {
            if (inCol[j] == 0 && inDiag[i + j] == 0 && inReDiag[j - i + N] == 0) {
                inCol[j] = 1;
                inDiag[i + j] = 1;
                inReDiag[j - i + N] = 1;
                hasQueue[i][j] = 1;

                put(i + 1);

                inCol[j] = 0;
                inDiag[i + j] = 0;
                inReDiag[j - i + N] = 0;
                hasQueue[i][j] = 0;
            }
        }
    }
    public static void main(String[] args) {
        put(0);
    }

    private static void print() {
        System.out.println("Solution #" + cnt);
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if (1 == hasQueue[i][j])
                    System.out.print("|#");
                else
                    System.out.print("|_");
            }
            System.out.println();
        }
    }
}
