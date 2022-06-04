#include<stdio.h>

void exercise1_2() {
    // printf("\c");
}

void eof() {
    printf("%%d: %d\n", EOF);
    printf("%%f: %f\n", EOF);
    printf("%%x: %x\n", EOF);
}

void get_put_char() {
    int c;
    while ((c = getchar()) != EOF)
        putchar(c);
}

void longint() {
    int x = 50;
    printf("%%ld: %ld\n", x);
}

void assign();

int main() {
    assign();
}

void assign() {
    int x, y, z;
    x = y = z = 11;
    printf("%d, %d, %d\n", x, y, z);
}