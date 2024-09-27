#include <stdio.h>

int main() {
    FILE *file;
    int x = 2;
    int y = -4;

    file = fopen("line_data.txt", "w");
    if (file == NULL) {
        printf("Error opening file.\n");
        return 1;
    }

    // Generate line data (only one point for a horizontal line)
    fprintf(file, "%d,%d\n", x, y);

    fclose(file);

    return 0;
}
