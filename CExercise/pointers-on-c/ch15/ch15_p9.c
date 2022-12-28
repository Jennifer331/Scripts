#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_LINE_LENGTH 2048

int main(int argc, char *argv[]) {
    if (argc < 3) {
        fprintf(stderr, "Usage: word_to_find [filename list]\n");
        exit(EXIT_FAILURE);
    }
    for (int i = 2; i < argc; i++) {
        char *filename = argv[i];
        FILE *file = fopen(filename, "r");
        if (file != NULL) {
            char buffer[MAX_LINE_LENGTH];
            while (fgets(buffer, MAX_LINE_LENGTH, file) != NULL) {
                if (strstr(buffer, argv[1]) != NULL) {
                    printf("%s: %s\n", filename, buffer);
                }
            }
            fclose(file);
        } else {
            perror("The following error occured");
        }
    }
    return EXIT_SUCCESS;
}