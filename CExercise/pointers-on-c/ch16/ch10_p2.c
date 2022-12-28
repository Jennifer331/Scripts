#include <stdlib.h>
#include <stdio.h>
#include <time.h>

#define MAX_OK_RAND (((RAND_MAX + 1) / 6) * 6 - 1)
int throwDie() {
    int value;
    do {
        value = rand();
    } while (value > MAX_OK_RAND);
    return value % 6 + 1;
}
void main() {
    srand((unsigned int)time(0));
    for (int i = 0; i < 10; i++) {
        printf("%d, ", throwDie());
    }
}