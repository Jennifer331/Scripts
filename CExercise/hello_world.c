#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

int main()
{
    char *p = NULL;
    if (p)
        printf("true");
    else
        printf("false");
}