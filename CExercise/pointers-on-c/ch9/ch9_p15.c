#include <string.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void dollarsShuai(char *dest, char *src) {
    // part1 Decimal Part
    char decimal[] = ".00";
    int srcLen = strlen(src);
    if (srcLen > 0)
        decimal[2] = src[srcLen - 1];
    if (srcLen > 1)
        decimal[1] = src[srcLen - 2];

    // part2 Whole number
    char reverseWholeNum[24];
    int idx = 0;
    if (srcLen < 3) {
        reverseWholeNum[idx++] = '0';
    } else {
        for (int i = 3; i <= srcLen; i++) {
            reverseWholeNum[idx++] = src[srcLen - i];
            if ((i - 2) % 3 == 0 && i < srcLen) {
                reverseWholeNum[idx++] = ',';
            }
        }
    }

    int destIdx = 0;
    dest[destIdx++] = '$';
    for (int i = 0; i < idx; i++) {
        dest[destIdx++] = reverseWholeNum[idx - i - 1];
    }
    dest[destIdx] = '\0';
    strcat(dest, decimal);
}

void dollarsLei(char *dest, char *src) {
    int destIdx = 0;
    int srcIdx = 0;

    // part1 Dollar Sign
    dest[destIdx++] = '$';

    // part2 Whole Number
    bool bgt0 = strlen(src) > 2;
    if (bgt0) {
        int length = strlen(src) - 2;
        int offset = 0;
        while ((length + offset) % 3 != 0)
            offset++;
        for (int i = offset; i < length + offset; i++) {
            if (i > 0 && i % 3 == 0) {
                // printf("%c: ", dest[destIdx - 1]);
                dest[destIdx++] = ',';
            }
            dest[destIdx++] = src[srcIdx++];
        }
    } else {
        dest[destIdx++] = '0';
    }

    //part3 Decimal Point
    dest[destIdx++] = '.';

    //part4 Decimal Part
    for (int i = 0; strlen(src) < 2 && i < 2 - strlen(src); i++) {
        dest[destIdx++] = '0';
    }
    while(src[srcIdx] != '\0') {
        dest[destIdx++] = src[srcIdx++];
    }
    
    //part5 Terminator
    dest[destIdx] = '\0';
}

void dollars(register char *dest, register char const *src)
{
    int len = strlen(src);
    *dest++ = '$';
    if (len >= 3) {
        for (int i = len - 2; i > 0; ) {
            *dest++ = *src++;
            if (--i > 0 && i % 3 == 0)
                *dest++ = ',';
        }
    } else {
        *dest++ = '0';
    }
    *dest++ = '.';
    *dest++ = len < 2 ? '0' : *src++;
    *dest++ = len < 1 ? '0' : *src++;
    *dest = '\0';
}

int main() {
    clock_t tic = clock();
    char src[255];
    char dest[255];
    for (int i = 1; i < 20000000; i++) {
        itoa(i, src, 10);
        char destLei[255];
        char destShuai[255];
        // dollarsShuai(destShuai, src);
        dollarsLei(destLei, src);
        dollars(dest, src);
        if (strcmp(destLei, dest) != 0) {
            printf("!!!!!!! Diff !!!!!!!\n i = %d\n Lei: %s\n Shuai: %s\n", i, destLei, dest);
        }
    }
    clock_t toc = clock();
    printf("Elapsed: %f seconds\n", (double)(toc - tic) / CLOCKS_PER_SEC);
}