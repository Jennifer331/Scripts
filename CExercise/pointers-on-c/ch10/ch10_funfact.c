#include <stdio.h>
#include <stddef.h>

typedef struct {
    int a;
    int b[3];
} Ex;
int main(void) {
    Ex x = {1, {2, 3, 4}};
    printf("offset of b: %d\n", offsetof(Ex, b));
    Ex *px = &x;
    printf("%d\n", px->b[2]);
}