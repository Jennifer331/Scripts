#include<stdio.h>

// void foo1();
// void foo2();

int ex = 10;
#define str1 "1234567"
#define str2 "sdf\
test"
#define dprint(expr) printf(#expr " = %g\n", expr)
#define paste(front, back) front ## back

void main(int argc, char *argv[]) {
    // printf("\n%d\n", ex);
    // char chararr[] = "could";
    // printf("%s", chararr);
    // putchar(3 + '0');
    
    // printf("\n %s, %s\n", str1, str2);

    // dprint(3.5/2.5);
    // char name1[] = "lei";
    // printf("%s\n", paste(name, 1));
    // int x = 10;
    // int *ip = &x;
    // *ip = *ip + 10;
    // printf("%d\n", ip);
    // printf("%d\n", *ip);

    // int a[3] = {1, 2, 3};
    // int *pa = &a[0];
    // pa += 2;
    // printf("%d, %d, last element: %d\n", pa, a, pa[-1]);
    // pa = NULL;

    // char *p;
    // p = "I lov you";
    // printf("test %s test\n", p);

    // while (argc--) {
    //     printf("%s\n", *argv++);
    // }
    int b[] = {1, 2, 3};
    int *a = b;
    if ((*a++ = 3) == 3) {
        printf("old place value");
    } else {
        printf("new place value");
    }
    printf("\ncurrent value:%d", *a);
}