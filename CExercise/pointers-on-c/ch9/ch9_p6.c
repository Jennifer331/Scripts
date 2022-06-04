#include<stdio.h>

char* my_strcpy_end(register char *src, register char *dest) {
    while ((*dest++ = *src++) != '\0')
        ;
    return dest - 1;
}

int main() {
    char src[10];
    char dest[10];
    scanf("%s", src);
    my_strcpy_end(src, dest);
    printf("%s", dest);
}