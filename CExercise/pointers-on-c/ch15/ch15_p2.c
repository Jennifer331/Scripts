#include <stdio.h>
#include <stdlib.h>

#define BUFSIZE 81
int main() {
    char buffer[BUFSIZE];
    while(fgets(buffer, BUFSIZE, stdin) != NULL)
        fputs(buffer, stdout);
    return EXIT_SUCCESS;
}