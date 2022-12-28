#include <stdio.h>
#include <ctype.h>
#include <stdlib.h>
#include <string.h>

#define MAX_LEN 100
#define PRINT_FUNC_NAME(func) #func

enum Char_Type {
    CNTRL, WHITE_SPACE, DIGIT, LOWER, UPPER, PUNCT, NONPRINT, TYPE_NUM
};

int isNonPrint(int c) {
    return !isprint(c);
}

static int (*checkFuncs[])(int) = {iscntrl, isspace, isdigit, islower, isupper, ispunct, isNonPrint};
char *label[] = {"control", "white-space", "digit", "lower case", "upper case", "punctuation", "non-printable"};

void main() {

    char ch;
    int total = 0;
    int cnts[TYPE_NUM];
    memset(cnts, 0, sizeof(int) * TYPE_NUM);
    while ((ch = getchar()) != EOF) {
        total++;
        for (int category = 0; category < TYPE_NUM; category++) {
            if (checkFuncs[category](ch)) {
                printf("%c is %s", ch, PRINT_FUNC_NAME(checkFuncs[category]));
                cnts[category]++;
            }
        }
    }

    if (total == 0) {
        printf("No characters in the input!\n");
    } else {
        for (int category = 0; category < TYPE_NUM; category++) {
            printf("%3.0f%% %s charactors\n", cnts[category] * 100.0 / total, label[category]);
        }
    }
}