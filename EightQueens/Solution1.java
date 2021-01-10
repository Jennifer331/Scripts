
public class Solution1 {
static int cnt = 0;
    public static void main(String[] args) {
        int[][] board = new int[8][8];
        put(board, 0);
        System.out.println(cnt + " Solutions in total");
    }

    private static void put(int[][] board, int row) {
        if (row >= board.length) {
            cnt++;
            print(board, cnt);
        } else {
            for (int i = 0; i < board.length; i++) {
                if (safe(board, row, i)) {
                    board[row][i] = 1;
                    put(board, row + 1);
                    board[row][i] = 0;
                }
            }
        }
    }

    private static boolean safe(int[][] board, int r, int c) {
        int n = board.length;
        for (int i = 0; i < n; i++) {
            if (board[i][c] == 1 || board[r][i] == 1)
                return false;
        }
        //rightdown
        for (int x = r, y = c; x < n && y < n; x++, y++) {
            if (board[x][y] == 1)
                return false;
        }
        //leftup
        for (int x = r, y = c; x >= 0 && y >= 0; x--, y--) {
            if (board[x][y] == 1)
                return false;
        }
        //rightup
        for (int x = r, y = c; x < n && y >= 0; x++, y--) {
            if (board[x][y] == 1)
                return false;
        }
        //leftdown
        for (int x = r, y = c; x >= 0 && y < n; x--, y++) {
            if (board[x][y] == 1)
                return false;
        }

        return true;
    }

    private static void print(int[][] board, int cnt) {
        System.out.println("Solution #" + cnt);
        for (int i = 0; i < board.length; i++) {
            for (int j = 0; j < board.length; j++) {
                System.out.print(board[i][j] == 1 ? "|#" : "|_");
            }
            System.out.println();
        }
    }

}
