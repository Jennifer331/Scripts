#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void printCycFreq(int divisor, double **cfs)
{
    for (int i = 0; i < divisor; i++) {
        for (int j = 0; j < divisor; j++) {
            printf("%f ", cfs[i][j]);
        }
        printf("\n");
    }
}

double** cylicFreq(int *arr, int n, int divisor)
{
    double **ans = malloc(sizeof(double *) * divisor);
    for (int i = 0; i < divisor; i++) {
        ans[i] = malloc(sizeof(double) * divisor);
        for (int j = 0; j < divisor; j++) {
            ans[i][j] = 0;
        }
    }
    for (int i = 1; i < n; i++) {
        ans[arr[i - 1] % divisor][arr[i] % divisor]++;
    }
    for (int i = 0 ; i < divisor; i++) {
        for (int j = 0; j < divisor; j++) {
            ans[i][j] /= ((n - 1) * 1.0);
        }
    }
    return ans;
}

void printFreq(int divisior, double *freqs)
{
    printf("mod %d: ", divisior);
    for (int i = 0; i < divisior; i++) {
        printf("%d: %f, ", i, freqs[i]);
    }
    printf("\n");
}

double* freq(int *arr, int n, int divisor)
{
    double *ans = malloc(sizeof(double) * divisor);
    for (int i = 0; i < divisor; i++)
        ans[i] = 0;
    for (int i = 0; i < n; i++) {
        ans[arr[i] % divisor]++;
    }
    for (int i = 0; i < divisor; i++) {
        ans[i] /= (n * 1.0);
    }
    return ans;
}
int* generateRandArr(int n)
{
    srand(time(0));
    int *arr = malloc(sizeof(int) * n);
    for (int i = 0; i < n; i++) {
        arr[i] = rand();
    }
    return arr;
}

void main()
{
    int n = 10000;
    int *arr = generateRandArr(n);
    for (int divisor = 2; divisor <= 10; divisor++) {
        double *fs = freq(arr, n, divisor);
        printFreq(divisor, fs);
        free(fs);
    }

    for (int divisor = 2; divisor <= 10; divisor++) {
        double **cfs = cylicFreq(arr, n, divisor);
        printCycFreq(divisor, cfs);
        for (int i = 0; i < divisor; i++) {
            free(cfs[i]);
        }
        free(cfs);
    }

    free(arr);
}
