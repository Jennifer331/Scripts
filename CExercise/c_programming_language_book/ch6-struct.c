#include<stdio.h>

struct point {
    int x;
    int y;
};

struct key
{
    char *word;
    int count;
} keytab[] = {
    "auto", 0,
    "break", 0,
    "case", 0,
    "continue", 0
};

#define NKEYS (sizeof keytab / sizeof keytab[0])

void main() {
    struct point p = {3, 4};
    struct point *pp = &p;
    printf("pp->x: %d\n", pp->x);

    printf("sizeof keytab: %d\n", sizeof keytab);
    printf("sizeof struct key: %d\n", sizeof(struct key));
}