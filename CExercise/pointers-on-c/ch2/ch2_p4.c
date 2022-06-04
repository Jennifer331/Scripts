#include <stdlib.h>
#include <stdio.h>

#define MIN(x, y) ((x) < (y) ? (x) : (y))
void copy_n(char dst[], char src[], int n)
{
    int srcIndex = 0;
    for (int desIndex = 0; desIndex < n; desIndex++) {
        dst[desIndex] = src[srcIndex];
        if (src[srcIndex] != 0)
            srcIndex++;
    }
}

int main() {

}