#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
    int a[] = {3,30,34,5,9};
    int *p = a;
    printf("%p, %p\n", a, &a);
    printf("%p, %p\n", p, &p);
    printf("%d\n", 2[a]);
}