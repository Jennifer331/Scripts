#include<stdio.h>
#include<string.h>
#include<ctype.h>

#define MAXTOKEN 100

enum {NAME, PARENS, BRACKETS};

int gettoken();

char token[MAXTOKEN];
int tokentype;
char out[1000];

void main() {
    int type;
    char temp[MAXTOKEN];

    while (gettoken != EOF) {
        strcpy(out, token);
        while ((type = gettoken()) != '\n') {
            if (type == PARENS || type == BRACKETS) {
                strcat(out, token);
            } else if (type == '*') {
                sprintf(temp, "(*%s)", out);
                strcpy(out, temp);
            } else if (type == NAME) {
                sprintf(temp, "%s %s", token, out);
                strcpy(out, temp);
            } else {
                printf("invalid input at %s\n", token);
            }
        }
        
    }
}
int gettoken() {
    char c;
    char *p = token;

    while ((c = getchar()) == ' ' || c == '\t')
        ;
    if (c == '(') {
        if ((c = getchar()) == ')') {
            strcpy(token, "()");
            return tokentype = PARENS;
        } else {
            ungetc(c, stdin);
            return tokentype = '(';
        }
    } else if (c == '[') {
        for (*p++ = c; (*p++ = getchar()) != ']'; )
            ;
        *p = '\0';
        return tokentype = BRACKETS;
    } else if (isalpha(c)) {
        for (*p++ = c; isalnum(c = getchar()); )
            *p++ = c;
        *p = '\0';
        ungetc(c, stdin);
        return tokentype = NAME;
    } else {
        return tokentype = c;
    }
}