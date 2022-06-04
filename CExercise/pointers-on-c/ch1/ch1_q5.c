#include<stdio.h>

int main()
{
    int quantity, price;
    char department[100];
    scanf("%d %d %s", &quantity, &price, department);
    printf("%d %d %s\n", quantity, price, department);
}