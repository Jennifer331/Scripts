#include <stdio.h>

int ascii_to_integer(char *string)
{
    int num = 0;
    while (*string >= '0' && *string <= '9') {
        num *= 10;
        num += *string++ - '0';
    }
    if (*string != '\0')
        num = 0;
        
    return num;
}

int main()
{
    char input[255];
    scanf("%s", input);
    printf("%d", ascii_to_integer(input));
}