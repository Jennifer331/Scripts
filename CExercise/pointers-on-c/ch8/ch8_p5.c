void matrix_multiply(int *m1, int *m2, int *r, int x, int y, int z)
{
    register int *m1p;
    register int *m2p;

    for (int row = 0; row < x; row++) {
        for (int col = 0; col < z; col++) {
            m1p = m1 + row * y;
            m2p = m2 + col;
            for (int k = 0; k < y; k++) {
                *r += *m1p * *m2p;
                m1p++;
                m2p += z;
            }
            r++;
        }
    }
}