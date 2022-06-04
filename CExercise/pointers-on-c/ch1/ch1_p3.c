#include<stdio.h>

#define LINE_BREAK '\n'

int main(void)
{
    signed char checkSum = -1;
    char ch;
    while ((ch = getchar()) != LINE_BREAK) {
        putchar(ch);
        checkSum += ch;
    }
    checkSum += ch;
    printf("\n%d", checkSum);
    return 0;
}