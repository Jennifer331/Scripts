#include <stdio.h>
#include <string.h>

#define MAX_LEN 1000

int main(void)
{
    char input[MAX_LEN];
    char longest[MAX_LEN];
    int maxLen = 0;

    while (fgets(input, MAX_LEN, stdin) != NULL) {
        int len = strlen(input);
        if (len > maxLen) {
            maxLen = len;
            strcpy_s(longest, MAX_LEN * sizeof(char), input);
        }
    }

    printf("%s\n", longest);
    return 0;
}