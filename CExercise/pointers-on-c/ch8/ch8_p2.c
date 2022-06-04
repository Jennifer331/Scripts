#include<stdio.h>

float single_tax(float income)
{
    float limits[] = {0, 23350, 56550, 117950, 256500};
    float bases[] = {0, 3502.5, 12798.5, 31832.5, 81710.5};
    float rates[] = {0.15, 0.28, 0.31, 0.36, 0.398};
    
    int type = 4;
    while (limits[type] > income)
        type--;
    return bases[type] + (income - limits[type]) * rates[type];
}

int main()
{
    printf("%f\n", single_tax(56550));
}