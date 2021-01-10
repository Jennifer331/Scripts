

public class MatrixMultiply{
  int[][] memo;

  private int minMult(Matrix[] a, int l, int r) {
    if (l == r)
      return 0;
    if (memo[l][r] != Integer.MAX_VALUE)
      return memo[l][r];

    for (int i = l + 1; i <= r; i++) {
      int cur = minMult(a, 0, i)
                + a[l].row * a[i].row * a[r].col
                + minMul(1, i + 1, n);

      memo[l][r] = Math.min(memo[l][r], cur);
    }

    return memo[l][r];
  }

  private int dp(Matrix[] a) {
    int n = a.length;
    int[][] dp = new int[n][n];


  }
}
