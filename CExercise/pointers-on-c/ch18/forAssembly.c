#include <stdio.h>
static int staticInt =5;
void f() {
    register int i1, i2, i3, i4, i5, i6, i7, i8;
    i1 = 1;
    i2 = 2;
    i3 = 3;
    i4 = 4;
    i5 = 5;
    i6 = 6;
    i7 = 7;
    i8 = 8;
    printf("%d, %d, %d, %d, %d, %d, %d, %d\n", i1, i2, i3, i4, i5, i6, i7, i8);
}
void main() {
    printf("Test for assembly");
}