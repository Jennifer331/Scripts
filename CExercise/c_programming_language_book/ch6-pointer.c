#include<stdio.h>

void main() {
    int a = 1, b = 2;
    int *pa = &a;
    int *pb = &b;
    printf("pa + pb = %d", pa - pb);
}