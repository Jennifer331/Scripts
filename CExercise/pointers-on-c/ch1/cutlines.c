#include<stdio.h>  
#include<stdlib.h>

#define MAX_COLS 20
#define MAX_INPUT 1000

int read_column_numbers(int columns[], int max);
void rearrange(char *output, char const *input, int n_columns, int const columns[]);

void main() {
    #if 0
        printf("#if 0");
    #elif 1
        printf("#elif 1");
    #endif

    int n_columns;
    int columns[MAX_COLS];
    char input[MAX_INPUT];
    char output[MAX_INPUT];

    n_columns = read_column_numbers(columns, MAX_COLS);
    
    while(NULL != gets(input)) {
        printf("Original input: %s\n", input);
        rearrange(output, input, n_columns, columns);
        printf("Rearranged line: %s\n", output);
    }
}

int read_column_numbers(int columns[], int max) {
    int res = 0;

    while (res < MAX_COLS && scanf("%d", &columns[res]) == 1 && columns[res] >= 0)
        res++;

    if (res % 2 != 0) {
        puts("numbers not paired!");
        exit(EXIT_FAILURE);
    }

    int ch;
    while ((ch = getchar()) != '\n')
        ;

    return res;
}

void rearrange(char *output, char const *input, int n_columns, int const columns[]) {
    int p = 0;
    for (int i = 0; i < n_columns; i += 2) {
        for (int q = columns[i]; q <= columns[i + 1]; q++)
            output[p++] = input[q];
    }
    output[p] = '\0';
}