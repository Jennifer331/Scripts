#include<stdio.h>

int main(void)
{
    int lineNo = 0;
    int newline = 1;
    char c;
    while ((c = getchar()) != EOF) {
        if (newline == 1) {
            printf("%d ", lineNo);
            lineNo++;
            newline = 0;
        }
        putchar(c);
        if (c == '\n') {
            newline = 1;
        }
    }
    return 0;
}