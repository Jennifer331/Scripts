#include <stdio.h>
#include <stdlib.h>

void reverse_string(char *string)
{
    char *last_char = string;
    while (*last_char != '\0') {
        last_char++;
    }
    last_char--;
    while (string < last_char) {
        char temp = *string;
        *string++ = *last_char;
        *last_char-- = temp;
    }
}
int main()
{
    char input[255];
    scanf("%s", input);
    reverse_string(input);
    printf("%s\n", input);
}