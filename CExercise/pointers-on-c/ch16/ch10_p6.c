#include <math.h>
#include <stdio.h>

double payment(double amount, double interest, int year)
{
    int n = year * 12;
    double i = interest / (100 * 12);
    return amount * i / (1 - pow(1 + i, -n));
}

void main() {
    printf("%f\n", payment(100000, 8, 20));
}