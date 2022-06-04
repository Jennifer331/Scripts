#include<stdio.h>

void main() {
    // printf("please input:\n");
    // char c = getchar();
    // putchar(c);

    int day, year;
    char monthname[20];

    scanf("%d%s%d", &day, monthname, &year);

    printf("%d %s %d\n", day, monthname, year);
}
