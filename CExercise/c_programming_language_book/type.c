#include<stdio.h>
#include<limits.h>
#include<ctype.h>

void main() {
    printf("short max: %d\n int max: %d\n long max: %d\n", SHRT_MAX, INT_MAX, LONG_MAX);

    printf("sizeof(int): %d\n", sizeof(int));

    printf("Hello\011world");
	printf("\n");
	printf("Hello\x09world");
	printf("\n");

    int a, b, c;
    for(int i = 0; i < 10; i++) {
        a = i, b = i + 1, c = i + 2;
    }
    printf("%d, %d, %d", a, b, c);
}