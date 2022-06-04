#include<string.h>
#include<stdio.h>

int getTheCount(char *input) {
    char whitespaces[] = " \t\f\r\v\n";
    char *token;
    int cnt = 0;
    for (token = strtok(input, whitespaces);
    NULL != token;
    token = strtok(NULL, whitespaces)) {
        if (strcmp(token, "the") == 0)
            cnt++;
    }
    return cnt;
}

int main() {
    char input[100];
    // scanf("%s", input); wrong!!! %s stops at the first white-space
    gets(input);
    printf("%d", getTheCount(input));
}