#include <stdlib.h>
#include <stdio.h>

int main() {
    int num = 5;
    printf("Enter a number: ");
    scanf("%d", &num);

    float last_guess;
    float new_guess = 1;
    do {
        last_guess = new_guess;
        new_guess = (last_guess + num / last_guess) / 2;
        printf("%.15e\n", new_guess);
    } while (last_guess != new_guess);
    printf("Done\n");
    return EXIT_SUCCESS;
}