#include<stdio.h>

struct {
    unsigned int is_keyword: 1;
    unsigned int is_extern: 1;
    unsigned int is_static: 1;
} flags;

void main() {
    printf("default value in is_keyword: %d\n", flags.is_keyword);
    flags.is_keyword = 1;
    printf("is_keyword set to 1: %d\n", flags.is_keyword);
    flags.is_keyword = 2;
    printf("is_keyword set to 2: %d\n", flags.is_keyword);
    
}