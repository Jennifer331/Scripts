#include<stdio.h>

int max;

void edit() {
    extern int max;
    max = 4;
}

void main() {
    extern int max;
    printf("Init max: %d\n", max);
    edit();
    printf("Editted max: %d\n", max);
}