#include <stdio.h>
#include <ctype.h>

int main(void)
{
    int ch;
    while ((ch = getchar()) != EOF) {
        // if (ch >= 'A' && ch <= 'Z')
        //     ch += 'a' - 'A';
        ch = tolower(ch);
        putchar(ch);
    }   
    return 0;
}