#include <stdio.h>
#include <stdlib.h>

#define DELTA 2

void printArr(int *arr, int size) {
    for (int i = 0; i < size; i++) {
        printf("%d, ", arr[i]);
    }
}

int main() {
    int capab = DELTA;
    int *arr = malloc(sizeof(int) * capab);
    int size = 0;
    int value;
    while (scanf("%d", arr + ++size) == 1) {
        if (size + 1 == capab) {
            capab += DELTA;
            arr = realloc(arr, capab * sizeof(int));
        }
    }
    arr[0] = size - 1;
    printArr(arr, size);
    return 0;
}