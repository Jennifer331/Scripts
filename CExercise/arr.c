#include <stdio.h>
#include <stdlib.h>

void reverse_string(char *string)
{
    char *last_char = string;
    while (*t != '\0') {
        t++;
    }
    t--;
    while (s < t) {
        char temp = *s;
        *s = *t;
        *t = temp;
        s++;
        t--;
    }
}
int main()
{
    char input[255];
    scanf("%s", input);
    reverse_string(input);
    printf("%s\n", input);
}