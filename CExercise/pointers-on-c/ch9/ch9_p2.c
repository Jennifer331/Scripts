#include <stdio.h>
#define CAPACITY 10

size_t my_strnlen(char *str, int size) {
    register size_t length;
    for (length = 0; length < size; length++) {
        if (*str++ == '\0')
            break;
    }
    return length;
}

int main() {
    char input[CAPACITY];
    scanf("%s", input);
    printf("len: %d", my_strnlen(input, CAPACITY));
}